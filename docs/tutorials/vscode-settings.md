# Sharing VS Code Settings for Python Projects

## Introduction

Setting norms for developer tasks on a team project is crucial for
maintaining code consistency and readability. Visual Studio Code (VS
Code) allows us to manage distinct user and workspace settings. This
flexibility ensures that while each developer can maintain their custom
settings, the team adheres to the shared settings that ensure
consistency across the project, especially when working with Python.

## How We Share VS Code Settings Across Python Projects

### Workspace Settings

### Remote Development with VS Code

!!! info
    When developing on remote servers, such as AWS, you will encounter a "Remote" configuration in your VS Code settings, similar to the workspace settings you use locally. This "Remote" configuration serves the same purpose, allowing you to enforce consistent coding standards and best practices across your team. Despite the different context, the functionality remains identical, ensuring a seamless and efficient development experience regardless of your code's location.

Workspace settings in VS Code are stored in a `.vscode/settings.json`
file within the project directory. These settings are shared among all
team members and include configurations essential for maintaining coding
standards and best practices in Python. Workspace settings override user
settings.

#### Example of `.vscode/settings.json`

```json
{
  "python.pythonPath": "venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true
  }
}
```

In the example above, the settings ensure:
- The correct Python interpreter is used.
- Linting is enabled using Pylint and Flake8.
- Code is formatted using Black on save.
- Certain files and directories (like `__pycache__` and `.pyc` files)
  are excluded from the file explorer.

#### Location and Management

- The workspace settings file is located under the `.vscode` folder in
  your project’s root directory.
- You can edit the settings directly via the Preferences: Open Workspace
  Settings (JSON) command in the Command Palette.

### User Settings

User settings in VS Code are specific to an individual developer's
environment and are stored outside the project directory. These settings
allow each developer to customize their workspace without affecting the
shared project settings.

#### How to Access User Settings

1. Open VS Code.
2. Navigate to `File` > `Preferences` > `Settings` (or use the shortcut
   `Ctrl + ,` on Windows/Linux or `Cmd + ,` on Mac).
3. In the Settings tab, ensure you are in the `User` settings mode.

#### Example of Customizing User Settings

```json
{
  "workbench.colorTheme": "Visual Studio Dark",
  "editor.fontSize": 14,
  "editor.fontFamily": "Fira Code, monospace"
}
```

In the example above, the settings customize:

- The color theme of the editor.
- The font size and font family for the editor.

## Settings Precedence

VS Code allows configurations to be overridden at multiple levels. The
settings precedence determines which configuration will ultimately apply
when there are conflicts. Here is the order of precedence:

1. **Default settings**: The default, unconfigured setting values.
2. **User settings**: Apply globally to all VS Code instances.
3. **Remote settings**: Apply to a remote machine opened by a user.
4. **Workspace settings**: Apply to the open folder or workspace.
5. **Workspace Folder settings**: Apply to a specific folder of a
   multi-root workspace.
6. **Language-specific default settings**: Default values specific to a
   language, contributed by extensions.
7. **Language-specific user settings**: User settings, but specific to a
   language.
8. **Language-specific remote settings**: Remote settings, but specific
   to a language.
9. **Language-specific workspace settings**: Workspace settings, but
   specific to a language.
10. **Language-specific workspace folder settings**: Workspace folder
    settings, but specific to a language.
11. **Policy settings**: Set by the system administrator and always
    override other setting values.

From this list, it is clear that **workspace settings** override **user
settings**.

## Practical Example

If a setting is configured at multiple levels, the most specific scope
will apply. For instance:

- **User settings** (`settings.json` in the user profile):

  ```json
  {
    "editor.formatOnSave": false,
    "editor.fontSize": 14
  }
  ```

- **Workspace settings** (`.vscode/settings.json` in the project):

  ```json
  {
    "editor.formatOnSave": true,
    "editor.fontSize": 16
  }
  ```

In this scenario:

- The **editor.formatOnSave** setting will be `true` for the workspace,
  overriding the user's global setting of `false`.
- The **editor.fontSize** will be `16` for the workspace, overriding the
  user's global setting of `14`.

## Implications for Our Project

Given the settings precedence, our project uses the
`.vscode/settings.json` file to enforce consistent coding standards.
This file falls under **workspace settings**, which override **user
settings**.

## Steps to Follow

1. **Clone the Repository:** Ensure you clone the repository that
   includes the `.vscode/settings.json` file.

   ```bash
   git clone https://github.com/your-repo.git
   ```

2. **Do Not Ignore `.vscode/settings.json`:** Make sure the
   `.vscode/settings.json` file is not included in the `.gitignore` and
   is shared across the team via GitHub.

3. **Customize User Settings:** Personalize your VS Code experience by
   adding your custom settings to the user settings file without
   altering the workspace settings.

## Conclusion

Using distinct user and workspace settings in VS Code allows us to
balance personal preferences with team-wide coding standards. By
following this approach, we maintain code consistency and readability
across the project while providing the flexibility for individual
customization.

This approach helps maintain code consistency and readability across the
team, ensuring that everyone adheres to the same standards while
allowing for personal customization where it doesn't impact the
project's coding practices.

## References

- [Sharing VS Code Extensions Across
  Teams](https://dev.to/musixmatch/sharing-vs-code-extensions-across-teams-22ij)
- [VS Code Workspace Settings
  Guide](https://spin.atomicobject.com/vscode-workspace-settings/)
- [VS Code Documentation:
  Settings](https://code.visualstudio.com/docs/getstarted/settings)
- [Video: Sharing VS Code
  Settings](https://www.youtube.com/watch?v=D-Ipyy12Qaw)