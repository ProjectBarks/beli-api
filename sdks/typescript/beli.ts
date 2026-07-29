/**
 * Hand-written convenience layer over the generated SDK.
 *
 * `make sdk-ts` only rewrites `src/`, so this file survives regeneration.
 *
 * It handles the things every caller would otherwise repeat: the mandatory
 * headers, routing each operation to the right host, logging in, refreshing the
 * access token, and spacing requests out.
 */
import { createClient, type Client } from "./src/client";
import * as ops from "./src";

export const HOSTS = {
  onboard: "https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app",
  api: "https://backoffice-service-t57o3dxfca-nn.a.run.app",
  recs: "https://backoffice-service-recs-t57o3dxfca-nn.a.run.app",
  activity: "https://activity-service-978733420956.northamerica-northeast1.run.app",
} as const;

/** Operations the backend only serves from a host other than `api`. */
const ONBOARD_OPS = new Set(["login", "refreshToken", "getLoggedIn"]);
const ACTIVITY_OPS = new Set(["createActivity", "createApiError"]);

/**
 * The backend rejects clients that do not look like a browser with
 * `403 {"detail":"You do not have permission to perform this action."}`.
 * Any realistic browser User-Agent passes, so one is picked at random per
 * client rather than pinning a single fingerprint. Override with the
 * `userAgent` option, or plug in a generator such as the `user-agents`
 * package: `createBeliClient({ userAgent: new UserAgent().toString() })`.
 */
export const USER_AGENTS = [
  "Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 16; SM-S928U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.7827.91 Mobile Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15",
];

const randomUserAgent = () => USER_AGENTS[Math.floor(Math.random() * USER_AGENTS.length)];

export type BeliOptions = {
  email?: string;
  password?: string;
  /** Reuse tokens from a previous session instead of logging in again. */
  accessToken?: string;
  refreshToken?: string;
  /** Defaults to a random entry from `USER_AGENTS`. */
  userAgent?: string;
  /** Defaults to `capacitor://localhost`. Any value works, it just has to be present. */
  origin?: string;
  /**
   * Minimum gap between requests. The API publishes no rate limit but does
   * throttle bursts, so this defaults to 350ms.
   */
  minIntervalMs?: number;
};

export type Tokens = { access: string; refresh: string };

const decodeExp = (jwt: string): number =>
  JSON.parse(Buffer.from(jwt.split(".")[1], "base64url").toString()).exp;

/**
 * True once the token is within `skewMs` of expiring. Missing or unparseable
 * tokens count as expired so callers can treat this as "needs renewing".
 */
export const isExpired = (jwt: string | undefined, skewMs = 60_000): boolean => {
  if (!jwt) return true;
  try {
    return decodeExp(jwt) * 1000 - skewMs <= Date.now();
  } catch {
    return true;
  }
};

type AnyFn = (options?: any) => any;
type Bound<T> = T extends (options: infer O) => infer R
  ? (options?: Omit<O, "client" | "headers"> & { headers?: Record<string, string> }) => R
  : never;

export type BeliClient = { [K in keyof typeof ops]: Bound<(typeof ops)[K]> } & {
  /** Current tokens, refreshed in place. */
  tokens: Tokens;
  /** UUID of the logged-in user, read from the access token. */
  userId: string;
};

/**
 * Log in (or reuse tokens) and return a client with every operation pre-bound.
 *
 * ```ts
 * const beli = await createBeliClient({ email, password });
 * const { data } = await beli.searchApp({ query: { term: "coffee" } });
 * ```
 */
export async function createBeliClient(options: BeliOptions = {}): Promise<BeliClient> {
  const userAgent = options.userAgent ?? randomUserAgent();
  const origin = options.origin ?? "capacitor://localhost";
  const minInterval = options.minIntervalMs ?? 350;

  let tokens: Tokens = {
    access: options.accessToken ?? "",
    refresh: options.refreshToken ?? "",
  };

  const clients = Object.fromEntries(
    Object.entries(HOSTS).map(([name, baseUrl]) => {
      const client = createClient({ baseUrl });
      client.interceptors.request.use((request: Request) => {
        request.headers.set("User-Agent", userAgent);
        request.headers.set("Origin", origin);
        if (tokens.access) request.headers.set("Authorization", `Bearer ${tokens.access}`);
        return request;
      });
      return [name, client];
    }),
  ) as Record<keyof typeof HOSTS, Client>;

  const call = (name: string, opts: any = {}) => {
    const host = ONBOARD_OPS.has(name) ? "onboard" : ACTIVITY_OPS.has(name) ? "activity" : "api";
    return (ops as Record<string, AnyFn>)[name]({
      client: clients[host],
      throwOnError: false,
      ...opts,
      headers: { Origin: origin, ...opts.headers },
    });
  };

  /**
   * Make sure `tokens.access` is usable, renewing it in the cheapest way
   * available. Access tokens last 20 minutes; refresh tokens last 7 days and
   * are not rotated, so the same refresh token keeps working all week. Called
   * once at startup (which is what lets you resume from a stored refresh token
   * alone) and again before every request.
   */
  const ensureFreshToken = async (): Promise<void> => {
    if (!isExpired(tokens.access)) return;

    if (!isExpired(tokens.refresh)) {
      const { data } = await call("refreshToken", { body: { refresh: tokens.refresh } });
      if (data?.access) {
        tokens.access = data.access;
        return;
      }
    }

    if (options.email && options.password) {
      const { data, error } = await call("login", {
        body: { email: options.email, password: options.password },
      });
      if (error || !data) throw new Error(`beli: login failed (${JSON.stringify(error)})`);
      tokens = data as Tokens;
      return;
    }

    throw new Error(
      "beli: no usable token. Pass email and password, a live accessToken, " +
        "or a refreshToken issued in the last 7 days.",
    );
  };

  await ensureFreshToken();

  let queue: Promise<unknown> = Promise.resolve();
  const throttled = (name: string) =>
    async (opts: any = {}) => {
      const run = queue.then(async () => {
        await ensureFreshToken();
        const result = await call(name, opts);
        await new Promise((r) => setTimeout(r, minInterval));
        return result;
      });
      queue = run.catch(() => {});
      return run;
    };

  const userId = JSON.parse(
    Buffer.from(tokens.access.split(".")[1], "base64url").toString(),
  ).user_id as string;

  const cache = new Map<string, AnyFn>();
  return new Proxy({ tokens, userId } as any, {
    get(target, prop: string) {
      if (prop in target) return target[prop];
      if (typeof (ops as Record<string, unknown>)[prop] !== "function") return undefined;
      if (!cache.has(prop)) cache.set(prop, throttled(prop));
      return cache.get(prop);
    },
  }) as BeliClient;
}
