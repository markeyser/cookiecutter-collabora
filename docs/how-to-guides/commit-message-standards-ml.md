# Git Commit Message Standards for ML Projects

!!! example "ChatGPT Prompt for Git Commit Message"

    To create a standardized git commit message using ChatGPT, provide the
    following details: the output of `git diff` (1) command (including one or more
    modified files), the JIRA story number, and optionally, any additional
    context. ChatGPT will generate the appropriate commit message based on
    these inputs.
    { .annotate }

    1.  :man_raising_hand: To ensure you get enough information from `git diff` 
    to create a rich git commit message with ChatGPT, use the following 
    command: `git diff -U10 my-script.py`.


    ### Example Prompt

    Copy and paste the example prompt in ChatGPT or similar chat:

    ```plaintext
    Generate git commands for staging and committing the following changes. Follow
    the structure:

    <type>(<scope>): <subject> [#issue_number | #jira_key]

    Include all modified files in the `git diff` command. Provide the
    complete `git add` and `git commit` commands, including the body and 
    footer. Select the right git commit types with emojis. Limit 
    comments to 72 characters per line and code lines to 79 characters. 

    Output of `git diff` command:

    [Please insert the output of the git diff here]

    JIRA story number:

    [Please enter the JIRA story number here]

    Additional Context (Optional):
    -----------------------------

    [Please insert additional context]

    Commit types:
    -------------
    Here’s the list of git commit types with emojis included:

    ### Commit Types:

    - 🎨 Improve structure/format of the code
    - ⚡️ Improve performance
    - 🔥 Remove code or files
    - 🐛 Fix a bug
    - 🚑️ Critical hotfix
    - ✨ Introduce new features
    - 📝 Add or update documentation
    - 🚀 Deploy stuff
    - 💄 Add or update the UI and style files
    - 🎉 Begin a project
    - ✅ Add, update, or pass tests
    - 🔒 Fix security or privacy issues
    - 🔐 Add or update secrets
    - 🔖 Release/Version tags
    - 🚨 Fix compiler/linter warnings
    - 🚧 Work in progress
    - 💚 Fix CI build
    - ⬇️ Downgrade dependencies
    - ⬆️ Upgrade dependencies
    - 📌 Pin dependencies to specific versions
    - 👷 Add or update CI build system
    - 📈 Add or update analytics or track code
    - ♻️ Refactor code
    - ➕ Add a dependency
    - 🔧 Add or update configuration files
    - 🔨 Add or update development scripts
    - 🌍 Internationalization and localization
    - ✏️ Fix typos
    - 💩 Write bad code that needs to be improved
    - ⏪️ Revert changes
    - 🔀 Merge branches
    - 📦️ Add or update compiled files or packages
    - 👽 Update code due to external API changes
    - 🚚 Move or rename resources (e.g., files, paths, routes)
    - 📄 Add or update license
    - 💥 Introduce breaking changes
    - 🍱 Add or update assets
    - ♿️ Improve accessibility
    - 💬 Add or update comments in source code
    - 🗯️ Write code drunkenly
    - 🧪 Add or update text and literals
    - 🗃️ Perform database-related changes
    - 📝 Add or update logs
    - 🔇 Remove logs
    - 👤 Add or update contributor(s)
    - 🛠️ Improve user experience/usability
    - 🏗️ Make architectural changes
    - 📱 Work on responsive design
    - 🔍 Mock things
    - 🥚 Add or update an easter egg
    - ➕ Add or update a .gitignore file
    - 🧪 Add or update snapshots
    - 🔬 Perform experiments
    - 🌐 Improve SEO
    - 🛑 Add or update types
    - 🌱 Add or update seed files
    - 🚩 Add, update, or remove feature flags
    - ❗ Catch errors
    - 📲 Add or update animations and transitions
    - 🗑️ Deprecate code that needs to be cleaned up
    - 🔑 Work on code related to authorization, roles, and permissions
    - 👕 Simple fix for a non-critical issue
    - 🔍 Data exploration/inspection
    - 🧹 Remove dead code
    - 🚨 Add a failing test
    - 🧠 Add or update business logic
    - 🩺 Add or update health checks
    - 🏗️ Infrastructure-related changes
    - 🤝 Improve developer experience
    - 💵 Add sponsorships or money-related infrastructure
    - ⚖️ Add or update code related to multithreading or concurrency
    - 🛡️ Add or update code related to validation

    Example of Expected Output:
    ---------------------------

    git add mkdocs.yml poetry.lock pyproject.toml
    git commit -m "feat(deps): add mkdocs versioning and testing dependencies [#JIRA-123]

    Added dependencies for MkDocs versioning and testing to enhance
    documentation and development workflows. Updated pyproject.toml
    with the following:
    - mkdocs-glightbox: to support image lightboxes in documentation
    - mike: to manage multiple versions of documentation

    Updated poetry.lock with new packages:
    - importlib-resources: for resource management in tests
    - mike: for documentation version management
    - mkdocs-glightbox: for enhanced documentation visuals
    - verspec: for flexible version handling

    These changes improve documentation flexibility and testing coverage.

    Footer notes:
    - Consult package documentation for more details.
    "
    ```

    ### Generated Commit Message

    ChatGPT might respond with:

    ```plaintext
    git add utils/helpers.py
    git commit -m "🎨 refactor(helpers): update pi precision and greeting format [#JIRA-123]

    Updated the `calculate_area` function to use a more precise value
    of pi (3.14159) for improved accuracy in area calculations. Also,
    refined the `greeting` function to include a comma for better
    readability in the output.

    These changes enhance both the mathematical accuracy of area
    calculations and the user experience with improved greeting
    formatting.

    Footer notes:
    - Consider further enhancements to include localization
      for the greeting function.
    "
    ```

    ### Running the Git Command

    To commit your changes with the generated message, run the following command in your terminal:

    ```bash
    git add utils/helpers.py
    git commit -m "🎨 refactor(helpers): update pi precision and greeting format [#JIRA-123]

    Updated the `calculate_area` function to use a more precise value
    of pi (3.14159) for improved accuracy in area calculations. Also,
    refined the `greeting` function to include a comma for better
    readability in the output.

    These changes enhance both the mathematical accuracy of area
    calculations and the user experience with improved greeting
    formatting.

    Footer notes:
    - Consider further enhancements to include localization
      for the greeting function.
    "
    ```

Include this admonition in your `docs/how-to-guides/git-commit-message-standards.md` file. This example explains how to request a standardized git commit message from ChatGPT, providing a detailed prompt and the expected output.

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