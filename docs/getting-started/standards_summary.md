# Standards Summary

| **Category**                    | **Standard**                                       | **Resources**                                                                                                                                                                |
|---------------------------------|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **File Naming**                 | snake_case                                         | [File Naming Conventions](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/file-naming-conventions/)                                                         |
| **Field/Column Naming**         | snake_case                                         | [Column Naming Conventions](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/column-naming-conventions/)                                                     |
| **Python Docstring Style**      | Google Style                                       | [Python Docstring Conventions](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/python-docstrings-conventions/)                                              |
| **Length Standards**            | Comments: 72 chars, Code: 79 chars                 | [Python Line Length Standards](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/python-line-lenght-standards/)                                               |
| **Formatter**                   | Black using GitHub Actions                         | [Black Formatter](https://markeyser.github.io/cookiecutter-collabora/tutorials/black-formatter/)                                                                             |
| **Linter**                      | Ruff using GitHub Actions - all `.py` and `.ipynb` | [Ruff Linter](https://markeyser.github.io/cookiecutter-collabora/tutorials/ruff-linter/)                                                                                     |
| **Branching Strategy**          | GitHub Flow                                        | [Branching Strategy](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/branching-strategy/)                                                                   |
| **Commit Message**              | Conventional Commits                               | [Commit Message Standards in ML Projects](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/commit-message-standards-ml/)                                     |
| **Code Review**                 | Peer Review                                        | [Code Review Best Practices](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/code-review-best-practices/)                                                   |
| **Branch Names**                | `<category>/<description>-<JIRA_number>`           | [Git Branch Naming Standards](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/git-branch-naming-standards/)                                                 |
| **Technical Docs**              | MkDocs with Material Theme                         | [MkDocs Documentation](https://markeyser.github.io/cookiecutter-collabora/tutorials/mkdocs-docs/)                                                                            |
| **Testing**                     | Doctest and/or PyTest                              | [Introduction to Doctest](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/introduction-to-doctest/)                                                         |
| **Data Folder Structure**       | Organized by data processing stage                 | [ML Data Folder Naming Guide](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/ml-data-folder-naming/)                                                       |
| **Project Structure**           | Standardized Scaffolding                           | [Project Scaffolding Standards](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/project-scaffolding-standards/)                                             |
| **Exploratory Analysis**        | Jupyter Notebooks                                  | [Steps to Move a Prototype from Jupyter Notebook to Production-Ready Python Class](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/notebook-to-production/) |
| **Object-Oriented Programming** | Design classes and methods properly                | [Python OOP for ML Projects](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/python-oop-for-ml/)                                                            |
| **JIRA Stories**                | Track work effectively                             | [Best Practices for Creating JIRA Stories for ML/AI Projects](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/jira-story-best-practices/)                   |
| **Experiment Tracking**         | W&B Experiment Tracking for RAG                    | [W&B Experiment Tracking for RAG](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/wandb-experiment-tracking-rag/)                                           |
| **Lifecycle Management**        | Comprehensive Git and GitHub usage                 | [Lifecycle Using Git and GitHub](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/lifecycle-git-github/)                                                     |
| **Pushing to GitHub**           | Follow best practices                              | [Pushing to GitHub Best Practices](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/pushing-to-githug-best-practices/)                                       |

!!! warning "Branch Protection with Ruff and Black"

    To ensure code quality, the `dev` branch is protected with branch
    protection rules. This setup requires that all code must pass Ruff
    linting checks before being merged into the `dev` branch. While you can
    push code to your feature branches even if it fails linting and/or
    formatting, merging into `dev` is blocked until all linting and
    formatting errors are resolved. This approach mimics pre-commit hooks,
    maintaining a clean and compliant `dev` branch. Developers should run
    Ruff and Black locally and fix issues before pushing code for review.
