# Git Commit Message Standards for ML Projects

!!! tip "Introduction"
    Clear, informative commit messages are vital for effective team collaboration in machine learning projects. This guide provides standards and tools for creating standardized commit messages, including how to reference GitHub issue numbers or Jira keys. We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

!!! example "Commit Message Structure"
    Commit messages should follow this structure:

    ```text
    <type>(<scope>): <subject> [#issue_number | #jira_key]

    <body>

    <footer>
    ```

    #### Components
    - **Type**: Category of your commit.
    - **Scope**: Area of the codebase affected.
    - **Subject**: Brief description of changes, including issue tracker reference.
    - **Body**: Detailed explanation of changes and reasoning.
    - **Footer**: Additional notes or references.

!!! summary "Commit Types"
    Maintain consistency and organization with these commit types:

    | Type         | Description                                                   |
    |--------------|---------------------------------------------------------------|
    | `feat`       | New features or enhancements                                  |
    | `fix`        | Bug fixes                                                     |
    | `data`       | Data processing or management changes                         |
    | `experiment` | Experimental or exploratory code changes                      |
    | `model`      | Model development, testing, or deployment changes             |
    | `docs`       | Documentation additions or updates                            |
    | `refactor`   | Performance enhancements without functionality changes        |
    | `test`       | Test writing or fixing                                        |
    | `chore`      | Routine tasks or non-production code updates                  |
    | `build`      | Changes that affect the build system or external dependencies |
    | `ci`         | Changes to CI configuration files and scripts                 |
    | `revert`     | Reverts a previous commit                                     |
    | `style`      | Code style changes (formatting, missing semicolons, etc.)     |

!!! check "Best Practices"
    1. **Concise Subject**: Keep it short and descriptive.
    2. **Imperative Mood**: Phrase as an instruction, e.g., “fix” not “fixed”.
    3. **Capitalized Subject Line**: Start with a capital letter.
    4. **No Period in Subject Line**: Treat it as a title.
    5. **Separate Body with a Blank Line**: For tool compatibility.
    6. **Explain What and Why**: Not just how, in the body.
    7. **Reference Issues and Pull Requests**: Include relevant links for context.

## Examples

Here are some examples of commit messages that meet our standards:

```text
feat(auth): add user authentication feature [#DATA123]

Added a new user authentication feature to enhance security.
This includes login, registration, and password recovery.

Footer: Reviewed by Jane Doe
```

```text
fix(data): resolve data loading error [#GH45]

Fixed an issue where data loading was failing due to incorrect file paths.
Updated the file paths and added error handling.

Footer: Closes #GH45
```

```text
docs: update API documentation

Improved the API documentation to include new endpoints and usage examples.
Fixed typos and clarified descriptions.

Footer: Documentation reviewed by the tech writing team
```

!!! info "VS Code Extensions"
    Enhance commit message standardization with these VS Code extensions:
    - **Gitmoji for VS Code**: Add emoji to commit messages. [Gitmoji](https://marketplace.visualstudio.com/items?itemName=seatonjiang.gitmoji-vscode).
    - **[Commit Message Editor](https://marketplace.visualstudio.com/items?itemName=adam-bender.commit-message-editor)**: Enforce structured commit messages.

!!! bookmark "Reference for Best Practices"
    For an in-depth understanding, refer to [Git Commit Message Best Practices](https://www.gitkraken.com/learn/git/best-practices/git-commit-message).

!!! success "Conclusion"
    By following these guidelines, our team can ensure a uniform and informative history in our repository, turning commit messages into a rich log that enhances clarity and streamlines collaboration.