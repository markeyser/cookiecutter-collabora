# Cookiecutter Collabora

Welcome to Cookiecutter Collabora, a
[Cookiecutter](https://www.cookiecutter.io/) template engineered for
artificial intelligence, machine learning, and generative AI projects.
This template isn't just a starting point; it's a comprehensive
framework designed to guide you through the intricacies of AI project
development.  It combines best practices, industry standards, and a
suite of tools that aligns with the dynamic needs of modern AI
development.

## 🌟 Features

- **VS Code Dev Container Extension**: Fully integrated with Visual
  Studio Code Development Containers, providing a consistent and
  isolated development environment irrespective of your local setup.
- **Poetry and pyenv Integration**: Streamlined Python dependency
  management and version control with Poetry and pyenv, ensuring
  consistent and isolated environments for your projects.
- **Weight & Bias Ready**: The template is pre-configured to work
  seamlessly with Weight & Bias, a leading tool for machine learning
  experiment tracking, allowing you to monitor and compare your ML
  models effectively.
- **Black & Ruff**: Elegant code formatting with Black, augmented by the
  comprehensive linting capabilities of Ruff.
- **Automated Workflows**: Pre-configured pre-commit hooks and GitHub
  Actions automate code quality checks and standards enforcement.
- **VS Code Optimized**: A carefully selected collection of VS Code
  extensions and settings, optimized for AI development, ensures you can
  start coding right away.
- **Intelligent Spell Checking**: Tailored code spell checker with a
  custom dictionary generated from your project's Python dependencies.
- **Hydra Configuration Management**: Simplify and manage your
  configuration files efficiently with Hydra.
- **Professional Documentation**: MkDocs combined with the Material
  theme, ready to create a responsive documentation site with a curated
  initial setup.
- **Git-Ready**: A meticulously crafted `.gitignore` file tailored for
  AI projects ensures a clean and organized repository.

## 🛠 Requirements to Use the Cookiecutter Template

- **Editor**: Visual Studio Code, a modern, versatile, and extensible
  editor, ideal for Python and AI development.
- **Version Control**: GitHub, the cornerstone of collaborative
  open-source and private development projects.
- **Language**: Python 3, the go-to language for data science, machine
  learning, and AI applications.
- **Docker Desktop**: Required for managing and running your Docker
  containers, providing a consistent development environment across
  various platforms.
- **Weight & Bias**: Ready for integration with Weight & Bias for
  advanced machine learning experiment tracking and model management.

## 📖 Usage

### Installing Cookiecutter

Before starting, ensure Cookiecutter is installed on your system:

```shell
pip install cookiecutter
```

### Generate a New Project

Create a new project by running:

```shell
cookiecutter gh:markeyser/cookiecutter-collabora.git
```

<!-- NOTE: Needs discussion or investigation -@marcos_aguilerakeyser at 12/22/2023, 11:12:51 AM -->
Other appraoches such as for example:

`cookiecutter git@github.com-personal:markeyser/cookiecutter-collabora.git`
<!--  -->


You will be prompted to enter details for your project, such as project
name, OS type, author name, and more. For example:

```bash
  [1/9] project_name (Project Name): My AI Project
  [2/9] project_slug (my-ai-project):
  [3/9] package_name (myaiproject):
  [4/9] environment_name (my-ai-project-env):
  [5/9] author_name (Your name or your organization/company/team): Jane Doe
  [6/9] author_email (youremail@example.com): jane.doe@example.com
  [7/9] description (A short description of the project.): AI project development
  [8/9] independent_reviewer (github_username_of_independent_reviewer):
  [9/9] site_name (My AI Project Docs):
INFO:root:Current working directory: /Users/username/Projects/my-ai-project
```

This process will generate a new project with your specific
configurations.

This will create a new project based on the `cookiecutter-collabora` template
with your specified details.

```bash
cd my-ai-project
```

Once you're in your project's directory, you can open the entire
directory in Visual Studio Code:

```bash
code .
```

### Generate a Project from a Downloaded Template

If you have already downloaded the Cookiecutter template:

#### Listing Installed Cookiecutter Templates

To see installed Cookiecutter templates, use:

```bash
cookiecutter --list-installed
1 installed templates:
 * cookiecutter-collabora
```

#### Locating the `.cookiecutters` Directory on a Mac

Your cloned cookiecutters are usually stored in `~/.cookiecutters/`.

1. **Open Terminal**: Find Terminal in Applications > Utilities, or use
   Spotlight.

2. **Navigate to Home Directory**: Type `cd ~` and press Enter.

3. **List Hidden Directories**: Use `ls -a` to view all files and
   directories, including hidden ones like `.cookiecutters`.

4. **Access the `.cookiecutters` Directory**: Enter `cd .cookiecutters`.

5. **View Template Contents (Optional)**: Use `ls` to view the templates
   in the `.cookiecutters` directory.

   ```bash
   pwd
   /Users/username/.cookiecutters/cookiecutter-collabora
   ```

#### Creating a New Project with a Template

To create a project using the `cookiecutter-collabora` template:

```bash
cookiecutter /Users/username/.cookiecutters/cookiecutter-collabora
```

Enter the details for your project when prompted. For instance:

```bash
  [1/9] project_name (Project Name): My AI Project
  [2/9] project_slug (my-ai-project):
  [3/9] package_name (myaiproject):
  [4/9] environment_name (my-ai-project-env):
  [5/9] author_name (Your name or your organization/company/team): Jane Doe
  [6/9] author_email (youremail@example.com): jane.doe@example.com
  [7/9] description (A short description of the project.): AI project development
  [8/9] independent_reviewer (github_username_of_independent_reviewer):
  [9/9] site_name (My AI Project Docs):
INFO:root:Current working directory: /Users/username/Projects/my-ai-project
```

This will create a new project based on the `cookiecutter-collabora` template
with your specified details.

```bash
cd my-ai-project
```

Once you're in your project's directory, you can open the entire
directory in Visual Studio Code:

```bash
code .
```

## 📁 Resulting Directory Structure

The directory structure of your new project looks like this:

```text
├── README.md                      <- The top-level README for developers using this project.
├── Makefile                       <- Makefile with commands like `make data` or `make train`.
├── config                         <- Configuration files for the project.
├── docs                           <- Documentation for the project.
│   ├── api-reference.md           <- API reference documentation.
│   ├── explanation.md             <- Detailed explanations and conceptual documentation.
│   ├── how-to-guides.md           <- Step-by-step guides on performing common tasks.
│   ├── index.md                   <- The main documentation index page.
│   └── tutorials.md               <- Tutorials related to the project.
├── mkdocs.yml                     <- Configuration file for MkDocs, a static site generator for project documentation.
├── notebooks                      <- Jupyter notebooks for experiments, examples, or data analysis.
├── pyproject.toml                 <- Configuration file for Python projects which includes dependencies and package information.
├── src                            <- Source code for the project.
│   ├── common                     <- Common utilities and functions used across the project.
│   │   └── utils.py               <- Utility functions.
│   └── {{cookiecutter.package_name}}  <- Main project module.
│       ├── __init__.py            <- Initializes the Python package.
│       ├── app.py                 <- Main application script.
│       ├── data                   <- Data module for handling data operations.
│       │   ├── external           <- Data from third-party sources.
│       │   ├── features           <- Processed datasets used for feature engineering.
│       │   ├── interim            <- Intermediate data that has been transformed but not finalized.
│       │   ├── processed          <- The final, canonical datasets used for modeling.
│       │   └── raw                <- The original, immutable data dump.
│       └── models                 <- Machine learning models, scripts, and other related artifacts.
└── tests                          <- Automated tests for the project, typically using a framework like pytest.
```

