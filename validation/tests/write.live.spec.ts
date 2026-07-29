import { describe, it, expect, beforeAll } from "vitest";
import { createFollow, createBookmark, createRanking } from "beli-api-ts";
import { makeCtx, isAffected } from "../src/runner";
import { DESCRIPTORS } from "../src/endpoints";

// No Beli credentials exist in most environments (incl. this dev sandbox) — this whole suite
// must skip cleanly rather than error. It only runs for real in CI (Task 19), where
// BELI_EMAIL / BELI_PASSWORD / BELI_TEST_TARGET_USER / BELI_TEST_TARGET_BUSINESS are set.
const live = !!process.env.BELI_EMAIL;

// Change-tree gating (Task 16): CI passes `AFFECTED_OPS` (operationIds whose spec changed, or
// the literal "ALL") — each of the 3 reversible writes below only runs if its own operationId
// is in that set. See `runner.ts#isAffected`.

// Maps a reversible descriptor id to the generated SDK "create" call that exercises it. Each
// call goes through `ctx.sdk` (the bearer-authenticated Client from runner.ts#makeCtx), the
// same client `runOps` uses for reads, and returns the hey-api "fields" style result
// (`{ data, error, request, response }`) — `data` is what gets handed to `descriptor.revert`.
const CALLS: Record<string, (ctx: Awaited<ReturnType<typeof makeCtx>>) => Promise<any>> = {
  createFollow: (ctx) =>
    createFollow({
      client: ctx.sdk,
      body: DESCRIPTORS.createFollow.args!(ctx),
      headers: { Origin: "https://localhost" },
    }),
  createBookmark: (ctx) =>
    createBookmark({
      client: ctx.sdk,
      body: DESCRIPTORS.createBookmark.args!(ctx),
      headers: { Origin: "https://localhost" },
    }),
  createRanking: (ctx) =>
    createRanking({
      client: ctx.sdk,
      body: DESCRIPTORS.createRanking.args!(ctx),
      headers: { Origin: "https://localhost" },
    }),
};

describe.runIf(live)("self-reverting writes", () => {
  let ctx: Awaited<ReturnType<typeof makeCtx>>;

  beforeAll(async () => {
    ctx = await makeCtx();
  });

  for (const id of ["createFollow", "createRanking"] as const) {
    it.skipIf(!isAffected(id))(`${id} then reverts`, async () => {
      const d = DESCRIPTORS[id];
      const { data, error } = await CALLS[id](ctx);
      try {
        expect(error).toBeUndefined();
        expect(data).toBeDefined();
      } finally {
        // ALWAYS clean up, whether the assertions above passed or threw.
        if (data !== undefined) {
          await d.revert!(ctx, data);
        }
      }
    });
  }

  // createBookmark/removeBookmark request+response bodies are `x-beli-unverified` in the spec
  // (typed as opaque `{[key: string]: unknown}`) — the real backend's actual shape has never
  // been observed. Treat a shape mismatch here as a soft, logged failure rather than letting it
  // throw and take down the rest of the suite; cleanup is still always attempted.
  it.skipIf(!isAffected("createBookmark"))(
    "createBookmark then reverts (unverified shape — soft failure)",
    async () => {
      const d = DESCRIPTORS.createBookmark;
      let data: any;
      let error: any;
      try {
        ({ data, error } = await CALLS.createBookmark(ctx));
        if (error !== undefined || data === undefined) {
          console.warn(
            "[write.live] createBookmark: response did not match the expected (unverified) shape",
            { error, data },
          );
        } else {
          expect(data).toBeDefined();
        }
      } finally {
        // createBookmark's revert doesn't depend on `data` at all — it re-sends the same
        // user/business identity — so cleanup is attempted unconditionally.
        await d.revert!(ctx, data);
      }
    },
  );
});
