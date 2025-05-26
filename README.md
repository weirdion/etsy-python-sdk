# etsy-python-sdk

Python 3 SDK for the Etsy Open API, generated using [OpenAPITools/openapi-generator](https://github.com/OpenAPITools/openapi-generator).

## Features

- Auto-generated Python SDK from the official Etsy OpenAPI spec
- Includes generated tests for SDK validation

## Usage

Add this SDK as a dependency in your Poetry project:

```toml
[tool.poetry.dependencies]
etsy-python-sdk = { git = "https://github.com/weirdion/etsy-python-sdk.git", branch = "main" }
```

## Development

### Install dependencies

```sh
make install
```

### Regenerate the SDK

```sh
make generate
```

### Run tests

```sh
make test
```

### Clean generated code

```sh
make clean
```

## Regeneration Workflow

1. Download the latest Etsy OpenAPI spec and generate the SDK:
    ```sh
    make generate
    ```
2. Run tests to verify:
    ```sh
    make test
    ```

## Repository Structure

- `src/etsy_python_sdk/` — Generated SDK code and tests
- `openapi/` — Downloaded OpenAPI spec
- `generator-config/` — OpenAPI generator configuration
- `Makefile` — Automation commands
- `pyproject.toml` — Poetry configuration

## License

MIT
