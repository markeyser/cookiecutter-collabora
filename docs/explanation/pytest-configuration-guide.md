# Pytest Configuration in VS Code

## Introduction

This document explains the Pytest configuration for a Python project
using VS Code and Poetry. The setup aims to streamline testing, ensure
code quality, and enhance developer productivity by leveraging various
Pytest plugins and settings.

!!! tip "Default Pytest Configuration"
    The Pytest configuration in this guide is the default configuration
    included in the “Cookiecutter Collabora” project. This setup is
    designed to provide a robust starting point for running tests
    efficiently and effectively.

    We invite you to adapt and customize
    this configuration to suit your specific project needs and
    preferences. Modify the settings as needed to optimize your testing
    workflow and achieve the best results.

## Configuration Overview

The Pytest configuration is defined in two key files:

1. `.vscode/settings.json`
2. `pyproject.toml`

## `.vscode/settings.json`

This file configures Pytest to work seamlessly within VS Code. Below is
the configuration used:

```json
{
    "python.testing.pytestArgs": [
        "tests",
        "--cov=src",
        "--cov-report=term-missing",
        "-v",
        "-n",
        "2",
        "--timeout=5"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```

### Explanation

- **`python.testing.pytestArgs`**: An array of arguments passed to Pytest when running tests in VS Code.
  - `"tests"`: Specifies the directory where test files are located.
  - `"--cov=src"`: Enables code coverage measurement for the `src` directory.
  - `"--cov-report=term-missing"`: Displays a coverage report in the terminal, highlighting missing lines.
  - `"-v"`: Enables verbose mode, providing detailed test output.
  - `"-n", "2"`: Utilizes `pytest-xdist` to run tests in parallel using 2 CPU cores.
  - `"--timeout=5"`: Sets a 5-second timeout for each test to prevent hanging tests.

- **`python.testing.unittestEnabled`**: Disables the unittest framework.
- **`python.testing.pytestEnabled`**: Enables the Pytest framework.

## `pyproject.toml`

This file manages the project dependencies and Pytest settings through Poetry.

```toml
[tool.poetry.dev-dependencies]
pytest = "8.2.2"
pytest-benchmark = "4.0.0"
pytest-xdist = "3.6.1"
pytest-cov = "5.0.0"
pytest-mock = "^3.14.0"
pytest-sugar = "1.0.0"
pytest-timeout = "2.3.1"

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --cov=src/fpservicesagemodel --cov-report=term-missing -n 2 --timeout=5"
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"
log_cli = true
log_cli_level = "INFO"
log_format = "%(asctime)s %(levelname)s %(message)s"
log_date_format = "%Y-%m-%d %H:%M:%S"
```

### Explanation

- **`[tool.poetry.dev-dependencies]`**: Specifies the development dependencies required for the project.
  - `pytest`: The core testing framework.
  - `pytest-benchmark`: For benchmarking test performance.
  - `pytest-xdist`: For parallel test execution.
  - `pytest-cov`: For measuring code coverage.
  - `pytest-mock`: For mocking objects in tests.
  - `pytest-sugar`: For a more readable test output.
  - `pytest-timeout`: For setting time limits on tests.

- **`[tool.pytest.ini_options]`**: Configures Pytest options.
  - `testpaths = ["tests"]`: Specifies the directory where test files are located.
  - `addopts = "-v --cov=src/fpservicesagemodel --cov-report=term-missing -n 2 --timeout=5"`: Additional options for running tests.
    - `"-v"`: Enables verbose mode.
    - `"--cov=src/fpservicesagemodel"`: Measures coverage for the specified directory.
    - `"--cov-report=term-missing"`: Displays missing coverage in the terminal.
    - `"-n 2"`: Runs tests in parallel using 2 CPU cores.
    - `"--timeout=5"`: Sets a 5-second timeout for each test.
  - `python_files = "test_*.py"`: Pattern for identifying test files.
  - `python_classes = "Test*"`: Pattern for identifying test classes.
  - `python_functions = "test_*"`: Pattern for identifying test functions.
  - `log_cli = true`: Enables logging to the console during test runs.
  - `log_cli_level = "INFO"`: Sets the log level to INFO.
  - `log_format = "%(asctime)s %(levelname)s %(message)s"`: Specifies the log message format.
  - `log_date_format = "%Y-%m-%d %H:%M:%S"`: Specifies the date format for log messages.

??? question "Why are Pytest extensions under [tool.poetry.dev-dependencies]?"
    Pytest is primarily used during the development phase of a project
    and is not intended for use in production or runtime environments.
    Unit tests, written using Pytest, help developers catch bugs early,
    facilitate code refactoring, and ensure code quality before
    deployment.

    Running Pytest in production can introduce unnecessary
    performance overhead and potential security risks. Instead, unit
    tests are typically executed in CI/CD pipelines to verify code
    functionality and reliability before the code is deployed to
    production. This approach ensures that production environments
    remain optimized for performance and stability.

??? question "Why Configure Both .vscode/settings.json and pyproject.toml?"
    Configuring both `.vscode/settings.json` and `pyproject.toml`
    ensures consistent and integrated testing in your development
    environment.

    - **.vscode/settings.json**: Customizes Pytest behavior
    in Visual Studio Code. With the Python extension installed, the
    beaker iconappears in the Activity bar, opening the Test
    Explorer for running and debugging tests directly in VS Code.
    
    - **pyproject.toml**: Manages project dependencies and centralizes
    Pytest configurations for use across different environments.

## Conclusion

This configuration ensures that tests are run efficiently and
effectively within VS Code, leveraging parallel execution, code
coverage, and timeouts to maintain code quality and performance. By
following these settings, developers can ensure a consistent and
productive testing environment.

## See also

- [Visual Studio Code Testing Documentation](https://code.visualstudio.com/docs/editor/testing)
- [Visual Studio Code Python Testing Documentation](https://code.visualstudio.com/docs/python/testing)