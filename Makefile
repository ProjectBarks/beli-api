.PHONY: sdks sdk-ts sdk-py sdk-go
sdks: sdk-ts sdk-py sdk-go
sdk-ts:
	# Uses the LOCAL bin so typescript is pinned to root devDeps (^5.9.3); registry-latest
	# typescript@7 crashes @hey-api ("Cannot read ... 'LineFeed'"). Run `npm install` at repo
	# root first (CI does this; locally too).
	npx openapi-ts -f sdkgen/openapi-ts.config.ts
sdk-py:
	uvx openapi-python-client generate --path openapi/beli.yaml --config sdkgen/python-client.yaml --output-path sdks/python --overwrite
sdk-go:
	mkdir -p sdks/go
	go run github.com/oapi-codegen/oapi-codegen/v2/cmd/oapi-codegen@latest -config sdkgen/oapi-codegen.yaml openapi/beli.yaml
