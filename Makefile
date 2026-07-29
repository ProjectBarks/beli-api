.PHONY: sdks sdk-ts sdk-py sdk-go
sdks: sdk-ts sdk-py sdk-go
sdk-ts:
	# Pin typescript@5.9 and @hey-api version: registry-latest typescript@7 crashes
	# @hey-api/openapi-ts ("Cannot read properties of undefined (reading 'LineFeed')").
	npx -y -p typescript@5.9.3 -p @hey-api/openapi-ts@0.99.0 openapi-ts -f sdkgen/openapi-ts.config.ts
sdk-py:
	uvx openapi-python-client generate --path openapi/beli.yaml --config sdkgen/python-client.yaml --output-path sdks/python --overwrite
sdk-go:
	mkdir -p sdks/go
	go run github.com/oapi-codegen/oapi-codegen/v2/cmd/oapi-codegen@latest -config sdkgen/oapi-codegen.yaml openapi/beli.yaml
