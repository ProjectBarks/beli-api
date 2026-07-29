// Live read runner: dogfoods the generated TypeScript SDK (`sdks/typescript`) against the
// real Beli backoffice API. Only ever exercised with real credentials (CI / Task 19) — see
// `tests/read.live.spec.ts`, which skips this entire module's behavior when creds are absent.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import YAML from "yaml";
import { createClient, type Client } from "beli-api-ts/client";
import * as sdkFns from "beli-api-ts";
import { validAccessToken, type Store } from "./auth";
import { DESCRIPTORS, type Ctx } from "./endpoints";

// Re-export the single canonical `Ctx` — defined in ./endpoints (Task 12) specifically so
// that module has no dependency on this file. This file imports it, it does not redefine it.
export type { Ctx };

const API_BASE_URL = "https://backoffice-service-t57o3dxfca-nn.a.run.app";
const ONBOARD_BASE_URL =
  "https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app";

// The generated SDK emits a single global `client` (see sdks/typescript/src/client.gen.ts)
// bound to one baseUrl, and its per-operation functions do NOT honor per-op `servers`
// overrides from the OpenAPI spec. `getLoggedIn` / `login` / `refreshToken` live on the
// onboarding host — every other read lives on the main API host — so we build two
// independent `Client` instances and route by operationId.
const ONBOARD_OPS = new Set(["getLoggedIn", "login", "refreshToken"]);

/** Extends the Task-12 `Ctx` with the two host-specific SDK clients Task 13 wires up. */
export type RunnerCtx = Ctx & { sdk: Client; onboardSdk: Client };

export type OpResult = {
  id: string;
  ok: boolean;
  status?: number;
  error?: string;
  skipped?: boolean;
  reason?: string;
};

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

function decodeUserId(accessToken: string): string {
  const payload = JSON.parse(
    Buffer.from(accessToken.split(".")[1], "base64url").toString(),
  );
  return payload.user_id;
}

function makeAuthedClient(baseUrl: string, accessToken: string): Client {
  const c = createClient({ baseUrl });
  c.interceptors.request.use((req) => {
    req.headers.set("Origin", "https://localhost");
    req.headers.set("Authorization", `Bearer ${accessToken}`);
    return req;
  });
  return c;
}

export async function makeCtx(): Promise<RunnerCtx> {
  const store: Store = {
    email: process.env.BELI_EMAIL,
    password: process.env.BELI_PASSWORD,
  };
  const access = await validAccessToken(store); // single login for the whole suite

  return {
    sdk: makeAuthedClient(API_BASE_URL, access),
    onboardSdk: makeAuthedClient(ONBOARD_BASE_URL, access),
    userId: decodeUserId(access),
    testTargetUser: process.env.BELI_TEST_TARGET_USER!,
    testTargetBusiness: Number(process.env.BELI_TEST_TARGET_BUSINESS),
  };
}

// --- path-param filling ------------------------------------------------------------------
//
// operationId -> ordered path-param names, sourced straight from openapi/beli.yaml (the
// source of truth) so this stays correct as the spec grows, without hand-maintaining a
// second copy of every route's shape.
const SPEC_PATH = path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  "../../openapi/beli.yaml",
);

function loadPathParams(): Record<string, string[]> {
  const doc = YAML.parse(fs.readFileSync(SPEC_PATH, "utf8"));
  const out: Record<string, string[]> = {};
  for (const methods of Object.values<any>(doc.paths)) {
    for (const op of Object.values<any>(methods)) {
      if (!op?.operationId) continue;
      const names = (op.parameters ?? [])
        .map((p: any) =>
          p.$ref
            ? doc.components.parameters[p.$ref.split("/").pop()]
            : p,
        )
        .filter((p: any) => p.in === "path")
        .map((p: any) => p.name);
      out[op.operationId] = names;
    }
  }
  return out;
}

const PATH_PARAMS: Record<string, string[]> = loadPathParams();

const UNFILLABLE = Symbol("unfillable");

// Only fill path params we can fill *safely* — i.e. unambiguously the logged-in test user.
// Anything else (business ids, a second user id, free-text query segments, ...) is left
// alone; the caller records a skip reason rather than guessing.
function fillPathParams(
  id: string,
  ctx: RunnerCtx,
): Record<string, string> | undefined | typeof UNFILLABLE {
  const names = PATH_PARAMS[id] ?? [];
  if (names.length === 0) return undefined;
  const filled: Record<string, string> = {};
  for (const name of names) {
    if (name === "uuid" || name === "viewer") {
      filled[name] = ctx.userId;
    } else {
      return UNFILLABLE;
    }
  }
  return filled;
}

// --- dispatch ------------------------------------------------------------------------------

const SDK_FNS = sdkFns as unknown as Record<
  string,
  (options: any) => Promise<any>
>;

export async function runOps(
  ids: string[],
  ctx: RunnerCtx,
): Promise<OpResult[]> {
  const out: OpResult[] = [];

  for (const id of ids) {
    const d = DESCRIPTORS[id];
    if (!d || d.kind !== "read") continue;

    const fn = SDK_FNS[id];
    if (typeof fn !== "function") {
      out.push({
        id,
        ok: false,
        skipped: true,
        reason: `no generated SDK function exported for operationId "${id}"`,
      });
      continue;
    }

    const filledPath = fillPathParams(id, ctx);
    if (filledPath === UNFILLABLE) {
      out.push({
        id,
        ok: false,
        skipped: true,
        reason: `path params not safely fillable from Ctx: [${PATH_PARAMS[id]?.join(", ")}]`,
      });
      continue;
    }

    const client = ONBOARD_OPS.has(id) ? ctx.onboardSdk : ctx.sdk;

    try {
      const res: any = await fn({
        client,
        path: filledPath,
        query: d.args?.(ctx),
        throwOnError: false,
      });
      if (res?.error) {
        out.push({
          id,
          ok: false,
          status: res.response?.status,
          error:
            typeof res.error === "string"
              ? res.error
              : JSON.stringify(res.error),
        });
      } else {
        out.push({ id, ok: true, status: res?.response?.status });
      }
    } catch (e: any) {
      out.push({ id, ok: false, error: String(e?.message ?? e) });
    }

    await sleep(350); // rate-limit courtesy
  }

  return out;
}
