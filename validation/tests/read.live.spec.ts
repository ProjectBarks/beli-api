import { describe, it, expect, beforeAll } from "vitest";
import { makeCtx, runOps } from "../src/runner";

// No Beli credentials exist in most environments (incl. this dev sandbox) — this whole
// suite must skip cleanly rather than error. It only runs for real in CI (Task 19), where
// BELI_EMAIL / BELI_PASSWORD / BELI_TEST_TARGET_USER / BELI_TEST_TARGET_BUSINESS are set.
const live = !!process.env.BELI_EMAIL;

describe.runIf(live)("live reads", () => {
  let ctx: Awaited<ReturnType<typeof makeCtx>>;

  beforeAll(async () => {
    ctx = await makeCtx();
  });

  it("getLoggedIn returns the current user", async () => {
    const [r] = await runOps(["getLoggedIn"], ctx);
    expect(r.ok).toBe(true);
  });

  it("searchApp returns results", async () => {
    const [r] = await runOps(["searchApp"], ctx);
    expect(r.ok).toBe(true);
  });
});
