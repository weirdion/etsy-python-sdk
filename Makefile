# Variables
OPENAPI_URL=https://www.etsy.com/openapi/generated/oas/3.0.0.json
OPENAPI_FILE=openapi/etsy-openapi.json
GENERATOR_CONFIG=generator-config/openapi-generator-config.yaml
SDK_DIR=src

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
	rm -rf $(SDK_DIR)/.openapi-generator \
		-f $(SDK_DIR)/.openapi-generator-ignore
	make clean-readme

# Clean generated readme
clean-readme:
	python3 -c "import re; p='src/etsy_python_sdk_README.md'; t=open(p).read(); t=re.sub(r'<div.*?>.*?</div>', '', t, flags=re.DOTALL); open(p, 'w').write(t)"

# Install dependencies using Poetry
install:
	poetry install

# Run tests (assumes generated tests are in src/etsy_python_sdk/test)
test:
	poetry run pytest src/etsy_python_sdk/test

# Clean up generated files
clean:
	rm -rf $(SDK_DIR)/etsy_python_sdk/* $(OPENAPI_FILE)

# Phony targets
.PHONY: all generate clean install test clean-readme
