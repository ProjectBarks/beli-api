import { describe, it, expect } from "vitest";
import fs from "node:fs";
import yaml from "yaml";
import { DESCRIPTORS } from "../src/endpoints";

const doc = yaml.parse(fs.readFileSync("../openapi/beli.yaml", "utf8"));
const ids = Object.values(doc.paths).flatMap((p: any) =>
  Object.values(p).map((o: any) => o.operationId).filter(Boolean),
);

describe("descriptor coverage", () => {
  it("every operationId has a descriptor", () => {
    const missing = ids.filter((id: string) => !(id in DESCRIPTORS));
    expect(missing).toEqual([]);
  });

  it("covers exactly the 140 known operationIds (no extras drifting silently)", () => {
    expect(ids.length).toBe(140);
  });
});
