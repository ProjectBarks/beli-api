import { describe, it, expect, vi } from "vitest";
import { validAccessToken, isExpired } from "../src/auth";

const future = Math.floor(Date.now()/1000) + 3600;
const jwt = (exp:number)=>`h.${Buffer.from(JSON.stringify({exp})).toString("base64url")}.s`;

describe("token reuse", () => {
  it("returns cached token with no network call when unexpired", async () => {
    const fetchSpy = vi.fn();
    const store = { access: jwt(future), refresh: jwt(future), email:"e", password:"p" };
    const tok = await validAccessToken(store, fetchSpy as any);
    expect(tok).toBe(store.access);
    expect(fetchSpy).not.toHaveBeenCalled();
  });
  it("detects expiry with skew", () => {
    expect(isExpired(jwt(Math.floor(Date.now()/1000)+30))).toBe(true); // within 60s skew
  });
});
