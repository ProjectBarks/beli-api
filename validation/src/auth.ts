const ONBOARD = "https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app";

/**
 * The backend rejects non-browser clients with 403
 * ({"detail":"You do not have permission to perform this action."}), so a
 * browser-like User-Agent is required alongside Origin. This is the UA the iOS
 * app sends.
 */
export const USER_AGENT =
  "Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148";
export const ORIGIN = "capacitor://localhost";

const HEADERS = {
  Accept: "application/json",
  "Content-Type": "application/json",
  Origin: ORIGIN,
  "User-Agent": USER_AGENT,
  "Accept-Language": "en-US,en;q=0.9",
};
export type Store = { access?: string; refresh?: string; email?: string; password?: string };

export function decodeExp(jwt: string): number {
  return JSON.parse(Buffer.from(jwt.split(".")[1], "base64url").toString()).exp;
}
export function isExpired(jwt: string, skewMs = 60000): boolean {
  return decodeExp(jwt) * 1000 - skewMs <= Date.now();
}
export async function login(email: string, password: string, f = fetch) {
  const r = await f(`${ONBOARD}/api/token/`, { method:"POST", headers:HEADERS, body: JSON.stringify({ email, password }) });
  if (!r.ok) throw new Error(`login failed ${r.status}`);
  return r.json() as Promise<{ access: string; refresh: string }>;
}
export async function refresh(token: string, f = fetch) {
  const r = await f(`${ONBOARD}/api/token/refresh/`, { method:"POST", headers:HEADERS, body: JSON.stringify({ refresh: token }) });
  if (!r.ok) throw new Error(`refresh failed ${r.status}`);
  return (await r.json()).access as string;
}
export async function validAccessToken(store: Store, f = fetch): Promise<string> {
  if (store.access && !isExpired(store.access)) return store.access;      // reuse, no network
  if (store.refresh && !isExpired(store.refresh)) { store.access = await refresh(store.refresh, f); return store.access; }
  if (store.email && store.password) { const t = await login(store.email, store.password, f); store.access = t.access; store.refresh = t.refresh; return t.access; }
  throw new Error("no valid token and no credentials");
}
