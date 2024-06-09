# Code and Comment Length Standards in Python Projects

## Overview

Maintaining consistent code and comment lengths is crucial for
readability and maintainability. This guide outlines the standards for
line lengths in code and comments and explains how to configure and use
Visual Studio Code (VS Code) to enforce these standards.

## Standards

- **Comments**: Limit comments to 72 characters per line.
- **Code**: Limit code lines to 79 characters.

These standards help ensure that the codebase remains readable and
manageable, particularly when reviewing code in different environments.

## Configuring VS Code

To enforce these standards, we have pre-configured the following files
in the repository:

- `.vscode/settings.json`
- `.vscode/extensions.json`
- `pyproject.toml`

As a developer, you do not need to touch or modify these files. They are
set up to ensure consistent standards across the project.

### Step 1: Pre-configured VS Code Settings

The `.vscode/settings.json` file is set to include rulers at 72 and 79
characters. This provides a visual cue for the character limits.

```json
{
    "editor.rulers": [
        72,
        79
    ],
    "rewrap.wrappingColumn": 72,
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": false
    },
    "rewrap.autoWrap.enabled": true
}
```

### Step 2: Pre-configured Extensions

The `.vscode/extensions.json` file includes the necessary extensions
like Black formatter and Ruff linter to enforce the standards.

```json
{
    "recommendations": [
        "ms-python.black-formatter",
        "ms-python.python",
        "stkb.rewrap"
    ]
}
```

### Step 3: Pre-configured pyproject.toml

The `pyproject.toml` file is configured to use Black and Ruff, adhering
to the line length standards. These libraries have been included under
`[tool.poetry.dev-dependencies]` and this section should not be changed
to maintain consistent formatting and linting across the project.

```toml
[tool.black]
line-length = 79

[tool.ruff]
line-length = 79

[tool.poetry.dev-dependencies]
black = { version = "23.7.0", extras = ["jupyter"] }
ruff = "0.3.2"
# Other dependencies...
```

### Using VS Code Tools

1. **Visual Indicators**: The rulers at 72 and 79 characters will help
   you visually align your code and comments.
2. **Rewrap Extension**: Use the Rewrap extension to format comments
   quickly:
   - Select the comment text.
   - Press `Command + Shift + P` (to open the Command Palette) and
     search for "Rewrap comment/text".

### Example Usage

**Before Rewrap:**

```python
# This is a very long comment that exceeds the recommended 72 characters per line limit and should be wrapped.
def example_function():
    pass
```

**After Rewrap:**

```python
# This is a very long comment that exceeds the recommended 72 characters
# per line limit and should be wrapped.
def example_function():
    pass
```

## Conclusion

By following these standards and using the pre-configured tools provided
in the repository, you can maintain a clean and readable codebase.
Consistent line lengths for code and comments improve readability,
making it easier for team members to understand and review code. The
configurations in `.vscode/settings.json`, `.vscode/extensions.json`,
and `pyproject.toml` enforce these standards automatically, so
developers can focus on writing quality code without worrying about
configuration details. Additionally, the Python libraries Ruff and Black
included in `[tool.poetry.dev-dependencies]` should not be changed to
ensure consistent formatting and linting practices across the project.