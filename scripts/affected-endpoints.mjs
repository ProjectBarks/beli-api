import { execSync } from "node:child_process";
import yaml from "yaml";
export function opHashes(doc) {
  const m = {};
  for (const p of Object.values(doc.paths ?? {}))
    for (const op of Object.values(p))
      if (op && op.operationId) m[op.operationId] = JSON.stringify(op);
  return m;
}
export function affectedFromSpecs(base, head) {
  const a = opHashes(base), b = opHashes(head);
  return Object.keys(b).filter(id => a[id] !== b[id]);
}
function specAt(sha) {
  try { return yaml.parse(execSync(`git show ${sha}:openapi/beli.yaml`, { encoding: "utf8" })); }
  catch { return { paths: {} }; }
}
if (process.argv[2]) {
  const [base, head] = [process.argv[2], process.argv[3] || "HEAD"];
  const changedFiles = execSync(`git diff --name-only ${base} ${head}`, { encoding: "utf8" }).split("\n");
  if (changedFiles.some(f => f.startsWith("validation/src/"))) { console.log("ALL"); process.exit(0); }
  console.log(affectedFromSpecs(specAt(base), specAt(head)).join("\n"));
}
