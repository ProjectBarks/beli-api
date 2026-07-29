import { describe, it, expect, beforeAll } from "vitest";
import { makeCtx, runOps, isAffected } from "../src/runner";

// No Beli credentials exist in most environments (incl. this dev sandbox) — this whole
// suite must skip cleanly rather than error. It only runs for real in CI (Task 19), where
// BELI_EMAIL / BELI_PASSWORD / BELI_TEST_TARGET_USER / BELI_TEST_TARGET_BUSINESS are set.
const live = !!process.env.BELI_EMAIL;

// Change-tree gating (Task 16): CI passes `AFFECTED_OPS` (operationIds whose spec changed, or
// the literal "ALL") — only ops in that set are actually exercised, so a spec diff touching one
// endpoint doesn't re-run every live read. `isAffected` reads `AFFECTED_OPS` once at collection
// time via `runner.ts#affectedSet`.
const READ_OPS: { id: string; label: string }[] = [
  { id: "getLoggedIn", label: "getLoggedIn returns the current user" },
  { id: "searchApp", label: "searchApp returns results" },
];

describe.runIf(live)("live reads", () => {
  let ctx: Awaited<ReturnType<typeof makeCtx>>;

  beforeAll(async () => {
    ctx = await makeCtx();
  });

  for (const { id, label } of READ_OPS) {
    it.skipIf(!isAffected(id))(label, async () => {
      const [r] = await runOps([id], ctx);
      expect(r.ok).toBe(true);
    });
  }
});
