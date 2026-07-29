.PHONY: sdks sdk-ts sdk-py sdk-go
sdks: sdk-ts sdk-py sdk-go
sdk-ts:
	npx -y @hey-api/openapi-ts -f sdkgen/openapi-ts.config.ts
sdk-py:
	uvx openapi-python-client generate --path openapi/beli.yaml --config sdkgen/python-client.yaml --output-path sdks/python --overwrite
sdk-go:
	mkdir -p sdks/go
	go run github.com/oapi-codegen/oapi-codegen/v2/cmd/oapi-codegen@latest -config sdkgen/oapi-codegen.yaml openapi/beli.yaml
