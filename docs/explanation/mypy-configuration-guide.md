# Mypy Configuration Guide

## Introduction

Mypy is a static type checker for Python. This guide explains how to
configure Mypy in your project using a `pyproject.toml` file and Visual
Studio Code settings.

!!! tip "Default Mypy Configuration"
    The Mypy configuration in this guide is the default setup included
    in the “Cookiecutter Collabora” project. This configuration aims to
    provide a solid foundation for static type checking in Python,
    enhancing code quality and robustness.

    Feel free to tailor and customize this configuration to fit your 
    specific project requirements. Adjust the settings as needed to 
    improve your type-checking process and achieve the best results for
    your development workflow.

## Configuration

### Visual Studio Code Settings

Add the following configuration to your
`{{cookiecutter.project_slug}}/.vscode/settings.json` file:

```json
{
    "mypy-type-checker.args": [
        "--config-file=pyproject.toml"
    ],
    "mypy-type-checker.cwd": "${workspaceFolder}",
    "mypy-type-checker.importStrategy": "fromEnvironment",
    "mypy-type-checker.preferDaemon": true,
    "mypy-type-checker.reportingScope": "workspace"
}
```

### PyProject Configuration

Add the following Mypy configuration to your
`{{cookiecutter.project_slug}}/pyproject.toml` file:

```toml
[tool.mypy]
python_version = "3.10"
disallow_untyped_defs = true
disallow_untyped_calls = true
ignore_missing_imports = true
```

## Explanation

- **`python_version`**: Specifies the Python version.
- **`disallow_untyped_defs`**: Disallows functions without type annotations.
- **`disallow_untyped_calls`**: Disallows calling functions without type annotations.
- **`ignore_missing_imports`**: Ignores imports that cannot be resolved.

## Running Mypy

To run Mypy, execute the following command in your terminal:

```sh
mypy .
```

This will check your code for type errors based on the configuration
provided.

??? question "Why are Mypy extensions under [tool.poetry.dev-dependencies]?"
    Mypy is primarily used during the development phase to ensure type checking and code quality. Including Mypy and its extensions under `[tool.poetry.dev-dependencies]` ensures they are available during development but not included in the production environment. This helps maintain performance and security in production while allowing thorough type checking during development.

    Running Mypy in production is unnecessary and can introduce performance overhead. Instead, type checks are typically executed in CI/CD pipelines to verify code quality before deployment.

??? question "Why Configure Both .vscode/settings.json and pyproject.toml?"
    Configuring both `.vscode/settings.json` and `pyproject.toml` ensures consistent and integrated type checking in your development environment.

    - **.vscode/settings.json**: Customizes Mypy behavior in Visual Studio Code. This allows for immediate feedback and integration with the editor's features, enhancing the development experience.
    - **pyproject.toml**: Centralizes Mypy configurations and project dependencies, making it easier to maintain consistency across different environments and tools.

## Conclusion

By following this guide, you will have Mypy configured in your project,
ensuring your Python code is type-checked and more robust.
