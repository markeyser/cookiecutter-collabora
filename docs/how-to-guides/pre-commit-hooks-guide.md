# Using Pre-Commit Hooks to Enforce Coding Standards

!!! example "Interacting with Pre-Commit Hooks"
    To ensure code quality and adherence to coding standards, you must use the terminal for all Git operations. The pre-commit hooks are automatically triggered during these operations, so it's crucial to follow these steps:

    1. **Install Pre-Commit Hooks** (This step is needed only once, when you clone the repo and follow the installation steps):
    
    ```sh
    pre-commit install
    ```

    2. **Run Pre-Commit Hooks on All Files**:
    
    ```sh
    pre-commit run --all-files
    ```

    3. **Add and Commit Changes**:
    
    After fixing any issues reported by the pre-commit hooks, use the following commands:
    
    ```sh
    git add <fixed_files>
    git commit -m "your commit message"
    ```

    4. **Avoid Using the VS Code Version Control Pane**:
    
    Ensure you perform all Git operations through the terminal to properly trigger and handle pre-commit hooks.

## Introduction

Pre-commit hooks are a powerful tool to enforce coding standards and
ensure code quality before changes are committed to the repository.
These hooks automatically run checks and tasks, such as linting,
formatting, running tests, and verifying branch names. This document
provides an overview of the pre-commit hooks implemented in our project
and how to use them effectively.

## Pre-Commit Hooks Overview

The following table provides a synthetic description of each pre-commit
hook, including whether you need to repeat the `git add` and `git
commit` commands after fixing issues:

| Name                         | Description                                                       | Repeat git add/commit |
|------------------------------|-------------------------------------------------------------------|-----------------------|
| Run PyTest                   | Runs PyTest to execute all tests in the `tests/` directory.       | Yes                   |
| Commit Message Check         | Ensures commit messages follow the specified format.              | No                    |
| Restricted File and Section Check | Prevents modifications to restricted files.                  | Yes                   |
| Filename Snake Case Check    | Verifies that filenames follow the snake_case convention.         | Yes                   |
| Generate Documentation       | Generates project documentation and stages it for commit.         | No                    |
| Branch Name Check            | Validates branch names against the specified pattern.             | No                    |
| ruff-linter                  | Lints Python code using Ruff.                                     | Yes                   |
| black-formatter              | Formats Python code using Black.                                  | Yes                   |
| black-jupyter-formatter      | Formats Jupyter notebooks using Black.                            | Yes                   |
| trailing-whitespace          | Trims trailing whitespace from files.                             | Yes                   |
| end-of-file-fixer            | Ensures files end with a newline.                                 | Yes                   |
| check-added-large-files      | Warns if large files are added to the commit.                     | Yes                   |
| debug-statements             | Detects and prevents debug statements in the code.                | Yes                   |
| detect-private-key           | Prevents private keys from being committed.                       | Yes                   |
| prettier                     | Formats YAML files using Prettier.                                | Yes                   |
| mypy                         | Checks static typing using Mypy.                                  | Yes                   |

## Using the Terminal for Git and Pre-Commit Hooks

To ensure that pre-commit hooks run correctly, it is recommended to use
the terminal for all Git operations. Avoid using the VS Code version
control pane, as it may not properly trigger the hooks.

## Detailed Descriptions and Examples

### 1. Run PyTest

**Description**: Runs all tests in the `tests/` directory using PyTest.

**Example**: If a test fails, you will see an error message indicating
which test failed. Fix the issue, stage the changes, and commit again.

```sh
pre-commit install
pre-commit run --all-files
```

**Error**: 
```plaintext
============================= test session starts ==============================
platform linux -- Python 3.10.0, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /path/to/repo
collected 2 items                                                              

tests/test_sample.py .F                                                  [100%]

=================================== FAILURES ===================================
______________________________ test_function_fail ______________________________

    def test_function_fail():
>       assert 1 == 2
E       assert 1 == 2

tests/test_sample.py:10: AssertionError
```

### 2. Commit Message Check

**Description**: Ensures commit messages follow the specified format.

**Example**: If the commit message format is incorrect, you will receive
an error message. Correct the commit message and try again.

```sh
git commit -m "feat(auth): add user authentication feature [#DATA123]"
```

**Error**:
```plaintext
Error: Commit message must follow the format '<type>(<scope>): <subject> [#JIRA-123]'
Example: feat(auth): add user authentication feature [#DATA-123]
```

### 3. Restricted File and Section Check

**Description**: Prevents modifications to restricted files.

**Example**: If a restricted file is modified, an error will be
displayed. Revert the changes to the restricted file and commit again.

```plaintext
Error: Modifications to '.vscode/settings.json' are not allowed.
```

### 4. Filename Snake Case Check

**Description**: Verifies that filenames follow the snake_case
convention.

**Example**: If a filename does not follow the snake_case convention,
you will receive an error. Rename the file accordingly and commit again.

```plaintext
Error: Filename 'MyFile.py' does not follow the snake_case naming convention.
```

### 5. Generate Documentation

**Description**: Generates project documentation and stages it for
commit.

**Example**: If the documentation generation fails, fix the issues and
run the command again.

```sh
pre-commit install
pre-commit run --all-files
```

### 6. Branch Name Check

**Description**: Validates branch names against the specified pattern.

**Example**: If the branch name does not follow the pattern, an error
will be displayed. Create a new branch with the correct naming
convention.

```sh
git checkout -b "feature/add-user-authentication-DATA123"
```

**Error**:
```plaintext
Error: Branch name must follow the pattern '<category>/<description>-<JIRA_KEY>'
Example: feature/user-authentication-DATA-123
Deleting branch: invalid-branch-name
```

### 7. ruff-linter

**Description**: Lints Python code using Ruff.

**Example**: If the linter finds issues, fix them and commit again.

```sh
ruff check --preview --fix project_directory/utils/advanced_parser.py
```

### 8. black-formatter

**Description**: Formats Python code using Black.

**Example**: If the formatter makes changes, stage the changes and
commit again.

```sh
black sample_script.py
```

### 9. black-jupyter-formatter

**Description**: Formats Jupyter notebooks using Black.

**Example**: If the formatter makes changes, stage the changes and
commit again.

```sh
black sample_notebook.ipynb
```

### 10. Trailing Whitespace

**Description**: Trims trailing whitespace from files.

**Example**: If trailing whitespace is found and removed, stage the
changes and commit again.

```sh
pre-commit install
pre-commit run --all-files
```

### 11. End of File Fixer

**Description**: Ensures files end with a newline.

**Example**: If a file does not end with a newline, fix the issue, stage
the changes, and commit again.

```sh
pre-commit install
pre-commit run --all-files
```

### 12. Check Added Large Files

**Description**: Warns if large files are added to the commit.

**Example**: If a large file is detected, you will receive a warning.
Decide whether to proceed with the commit or remove the large file.

```sh
pre-commit install
pre-commit run --all-files
```

### 13. Debug Statements

**Description**: Detects and prevents debug statements in the code.

**Example**: If debug statements are found, remove them and commit
again.

```sh
pre-commit install
pre-commit run --all-files
```

### 14. Detect Private Key

**Description**: Prevents private keys from being committed.

**Example**: If a private key is detected, remove it and commit again.

```sh
pre-commit install
pre-commit run --all-files
```

### 15. Prettier

**Description**: Formats YAML files using Prettier.

**Example**: If the formatter makes changes, stage the changes and
commit again.

```sh
prettier --write config.yaml
```

### 16. Mypy

**Description**: Checks static typing using Mypy.

**Example**: If Mypy finds type errors, fix them and commit again.

```sh
mypy my_script.py
```

By following these guidelines and using the pre-commit hooks, you can
ensure that your code adheres to the project's coding standards and that
any issues are caught early in the development process.