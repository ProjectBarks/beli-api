import { defineConfig } from "@hey-api/openapi-ts";
export default defineConfig({
  input: "./openapi/beli.yaml",
  output: { path: "./sdks/typescript/src", format: "prettier" },
  plugins: [
    "@hey-api/client-fetch",     // fetch client; interceptors add Origin + bearer (Task 13)
    "@hey-api/sdk",              // per-operation functions keyed by operationId
    "@hey-api/typescript",      // types
  ],
});
