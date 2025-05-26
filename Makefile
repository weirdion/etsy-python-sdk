# Variables
OPENAPI_URL=https://www.etsy.com/openapi/generated/oas/3.0.0.json
OPENAPI_FILE=openapi/etsy-openapi.json
GENERATOR_CONFIG=generator-config/openapi-generator-config.yaml
SDK_DIR=src/etsy_python_sdk

# Default target
all: generate

# Download the OpenAPI spec
$(OPENAPI_FILE):
	mkdir -p openapi
	curl -sSL $(OPENAPI_URL) -o $(OPENAPI_FILE)

# Generate the SDK
generate: $(OPENAPI_FILE)
	mkdir -p $(SDK_DIR)
	poetry run openapi-generator-cli generate \
		-i $(OPENAPI_FILE) \
		-g python \
		-c $(GENERATOR_CONFIG) \
		-o $(SDK_DIR) \
		--skip-validate-spec

# Install dependencies using Poetry
install:
	poetry install

# Run tests (assumes generated tests are in src/etsy_python_sdk/test)
test:
	poetry run pytest src/etsy_python_sdk/test

# Clean up generated files
clean:
	rm -rf $(SDK_DIR)/* $(OPENAPI_FILE)

# Phony targets
.PHONY: all generate clean install test
