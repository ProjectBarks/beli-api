const ONBOARD = "https://backoffice-service-onboarding-t57o3dxfca-nn.a.run.app";
const HEADERS = { "Content-Type": "application/json", Origin: "https://localhost" };
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
