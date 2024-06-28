# Software Development Best Practices Guide

## GitHub Repository Management

!!! tip "One Project, One GitHub Repo"
    It is best practice to create one GitHub repository per project. This helps to maintain clarity, organization, and manageability. Each project should have a dedicated repository to keep all relevant code, documentation, and resources in one place.

    **Standard Repo Naming Convention:** Use `kebab-case` for naming your repositories.
    
    **Example:** `my-github-repo`

    [REad more](https://markeyser.github.io/cookiecutter-collabora/explanation/github-naming-conventions/?h=nam)

!!! tip "Repository Scaffolding"
    Standardizing the project structure ensures consistency, ease of navigation, and efficient collaboration across projects. When code is always in the `src` folder, team members can quickly locate files. This also facilitates onboarding of new team members, improves maintainability, and enhances the overall productivity by reducing the time spent searching for files and understanding project layout.

    [Read more about repository scaffolding best practices](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/project-scaffolding-standards/?h=sca)

!!! tip "Standardize the README.md File"
    The `README.md` file is crucial for providing an overview of the project, instructions for setup, usage, and contribution guidelines. Standardizing this file ensures that every project has a clear and informative introduction, making it easier for new developers and users to understand and contribute to the project. A well-maintained `README.md` can significantly enhance the accessibility and usability of the project.

    [Read more about README.md best practices](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/templates/?h=readme)

!!! tip "One Branch per JIRA Story/Bug"
    Creating a separate branch for each JIRA story or bug ensures that changes are isolated and can be reviewed and tested independently. This practice improves code quality and makes it easier to track changes related to specific issues.

    [Read more about branching best practices](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/git-branch-naming-standards/)


!!! tip "Multiple Commits per Branch"
    Making multiple, small commits helps to save progress and reduces the risk of losing work. It also makes it easier to review changes and identify issues. Each commit should represent a logical unit of work and include a meaningful commit message.


!!! tip "Commit Best Practices"
    Committing frequently helps ensure progress is saved and reduces the risk of losing work. Each commit should represent a logical unit of work and include a meaningful commit message. This practice improves code quality and makes it easier to track changes.

    [Read more about commit best practices](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/git-commit-message-standards/)

## Environment Management

!!! tip "Python Virtual Environments"
    Using a dedicated Python virtual environment for each project helps
    avoid conflicts between dependencies and ensures that the project’s
    dependencies are isolated. This practice prevents the base
    environment from being inadvertently modified and makes it easier to
    manage and replicate the project environment.
    
    [Read more about Python virtual environments](https://markeyser.github.io/cookiecutter-collabora/tutorials/poetry/?h=envi#debugging-environment-issues)

## Coding Standards

!!! tip "Code and Text Length Standards"
    Adhering to code and text length standards ensures that your code is
    readable and maintainable. Limiting line lengths helps prevent
    horizontal scrolling and makes it easier for team members to review
    code and understand comments.

    - Comments: 72 characters
    - Code: 79 characters

    [Read more about Python Line Length Standards](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/python-line-lenght-standards/?h=leng)

!!! tip "Python Docstring Style"
    Using a consistent docstring style, such as the Google style, ensures that your documentation is clear and easy to follow. Well-written docstrings help team members understand the purpose and usage of your code, which is crucial for collaboration and maintenance.

    [Read more about Python Docstring Conventions](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/python-docstrings-conventions/?h=google)

## Data Management

!!! tip "Data Folder Structure"
    Organizing your data folder by data processing stage helps maintain
    clarity and order in your projects. This approach makes it easier to
    locate and manage data files relevant to different stages of data
    processing.

    [Read more about ML Data Folder Naming Guide](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/ml-data-folder-naming/?h=data)

!!! tip "Field/Column Naming"
    Using snake_case for field and column names ensures consistency and
    readability across your datasets. This practice facilitates easier
    data manipulation and querying.
    
    [Read more about Column Naming Conventions](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/column-naming-conventions/)

!!! tip "File Naming Convention"
    Adhering to a consistent file naming convention like snake_case
    helps maintain organization and makes it easier to find and manage
    files. This practice is crucial for collaborative work and long-term
    project maintenance.
    
    [Read more about File Naming Conventions](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/file-naming-conventions/)

## Experiment Tracking

!!! tip "Experiment Tracking Practices"
    Using a consistent experiment tracking practice is crucial for
    reproducibility and effective collaboration in machine learning
    projects. Tools like Weights & Biases (W&B) help you keep track of
    your experiments, visualize results, and share findings with your
    team.
    
    [Read more about W&B Experiment Tracking for RAG](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/wandb-experiment-tracking-rag/)

## Object-Oriented Programming (OOP)

!!! tip "OOP Best Practices"
    Designing classes and methods properly is essential for creating
    maintainable and scalable code in machine learning projects.
    Following OOP principles ensures that your code is organized,
    reusable, and easy to understand.
    
    [Read more about Python OOP for ML Projects](https://markeyser.github.io/cookiecutter-collabora/how-to-guides/python-oop-for-ml/?h=oop#example-of-oop-in-python)