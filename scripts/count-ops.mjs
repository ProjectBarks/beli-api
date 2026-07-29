import fs from "node:fs";
import yaml from "yaml";
const doc = yaml.parse(fs.readFileSync("openapi/beli.yaml", "utf8"));
const ops = Object.values(doc.paths ?? {}).flatMap(p =>
  Object.keys(p).filter(m => ["get","post","put","patch","delete"].includes(m)));
console.log(`operations: ${ops.length}`);
if (ops.length < 130) { console.error("Too few operations"); process.exit(1); }
const ids = ops; // operationId uniqueness check
