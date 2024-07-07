# Introduction to Unit Testing with Pytest

## Introduction

Unit testing is a fundamental practice in software development that
involves testing individual units of code to ensure they work as
intended. This guide introduces you to unit testing with Pytest, a
popular testing framework for Python. We will cover the basics of unit
testing, why it is essential, and how to set up and write unit tests
using Pytest with the configuration provided in our project.

!!! info "Detailed Pytest Configuration Guide"
    For a detailed explanation and setup for Pytest configuration within
    VS Code and Poetry, see the [Pytest Configuration
    Guide](../explanation/pytest-configuration-guide.md).

## What is Unit Testing?

### Definition

Unit testing involves testing the smallest parts of an application,
called units, in isolation. A unit can be a function, method, or class.
The goal is to verify that each unit of the software performs as
expected.

### Importance

- **Early Bug Detection**: Unit tests help catch bugs early in the development cycle.
- **Documentation**: They serve as documentation, explaining what the code is supposed to do.
- **Refactoring Support**: Unit tests make it safer to refactor code since you can quickly verify that your changes didn't break anything.
- **Confidence in Code**: They provide confidence that the code works correctly, leading to more reliable and maintainable software.

## Why Use Pytest?

Pytest is a powerful and flexible testing framework that makes it easy
to write simple and scalable test cases. Here are some reasons to use
Pytest:

- **Simple Syntax**: Pytest's syntax is straightforward, making it easy to write and understand tests.
- **Fixtures**: Pytest provides fixtures for managing setup and teardown code.
- **Plugins**: A rich ecosystem of plugins extends Pytest's functionality.
- **Parameterization**: Easily parameterize tests to run them with different inputs.

## Writing Your First Unit Test

Let's write a simple unit test for a function that adds two numbers.
Create a Python file named `calculator.py` in your `src` directory with
the following content:

```python
# src/calculator.py

def add(a, b):
    return a + b
```

Next, create a test file named `test_calculator.py` in the `tests`
directory with the following content:

```python
# tests/test_calculator.py

from src.calculator import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
```

### Running the Tests

To run the tests, use the following command:

```bash
poetry run pytest
```

You should see output indicating that the tests have passed.

## Advanced Features

### Fixtures

Fixtures are used to manage setup and teardown code. Here’s an example
of using a fixture:

```python
# tests/test_calculator.py

import pytest
from src.calculator import add

@pytest.fixture
def numbers():
    return 2, 3

def test_add(numbers):
    a, b = numbers
    assert add(a, b) == 5
```

### Parameterization

Parameterization allows you to run a test with multiple sets of inputs.
Here’s an example:

```python
# tests/test_calculator.py

import pytest
from src.calculator import add

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (-1, -1, -2)
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

## Conclusion

This guide introduced you to the basics of unit testing with Pytest. We
covered the importance of unit testing, the benefits of using Pytest,
and how to write and run your first unit test. With this foundation, you
can start writing tests for your codebase, ensuring its reliability and
maintainability. As you become more familiar with Pytest, you can
explore its advanced features to further enhance your testing workflow.
Happy testing!
