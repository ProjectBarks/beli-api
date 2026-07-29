import { describe, it, expect } from "vitest";
import { affectedFromSpecs } from "../../scripts/affected-endpoints.mjs";
const base = { paths: { "/api/x/": { get: { operationId: "getX", summary: "a" } } } };
const head = { paths: { "/api/x/": { get: { operationId: "getX", summary: "b" } },
                        "/api/y/": { get: { operationId: "getY" } } } };
describe("affected ops", () => {
  it("flags changed + new operations", () => {
    expect(affectedFromSpecs(base, head).sort()).toEqual(["getX", "getY"]);
  });
});
