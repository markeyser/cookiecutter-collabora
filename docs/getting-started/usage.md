# Usage

## Installing Cookiecutter

Before starting, ensure Cookiecutter is installed on your system:

```shell
pip install cookiecutter
```

## Generate a New Project

Create a new project by running:

```shell
cookiecutter gh:markeyser/cookiecutter-collabora.git
```

You will be prompted to enter details for your project, such as project
name, OS type, author name, and more. For example:

```bash
[1/17] project_name (Project Name): My AI Project
[2/17] project_slug (Project Slug): my-ai-project
[3/17] package_name (Package Name): myaiproject
[4/17] env_name (Environment Name): my-ai-project-env
[5/17] author (Author Name): Jane Doe
[6/17] email (Author Email): jane.doe@example.com
[7/17] description (Project Description): AI project development
[8/17] reviewer (Independent Reviewer GitHub): 
[9/17] site_name (Documentation Site Name): My AI Project Docs
[10/17] os (Operating System) [Linux, Windows, Mac]: Linux
[11/17] cloud (Cloud Provider) [Google Cloud, AWS, Azure]: AWS
[12/17] ml_type (ML Project Type) [Package, Supervised, Unsupervised, Generative AI]: Generative AI
[13/17] data_type (Data Type) [Structured, Unstructured, Semi-structured]: Unstructured
[14/17] packaging (Packaging Tool) [Poetry, Conda]: Poetry
[15/17] venv (Create Virtual Environment) [Yes, No]: Yes
[16/17] formatter (Code Formatter) [Black, Ruff]: Black
[17/17] docker (Use Docker with VS Code Dev Containers) [Yes, No]: Yes
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

## Generate a Project from a Downloaded Template

If you have already downloaded the Cookiecutter template:

### Listing Installed Cookiecutter Templates

To see installed Cookiecutter templates, use:

```bash
cookiecutter --list-installed
1 installed templates:
 * cookiecutter-collabora
```

### Locating the `.cookiecutters` Directory on a Mac

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
   /Users/username/.cookiecutters/cookiecutter-collabora
   ```

### Creating a New Project with a Template

To create a project using the `cookiecutter-collabora` template:

```bash
cookiecutter /Users/username/.cookiecutters/cookiecutter-collabora
```

Enter the details for your project when prompted. For instance:

```bash
[1/17] project_name (Project Name): My AI Project
[2/17] project_slug (Project Slug): my-ai-project
[3/17] package_name (Package Name): myaiproject
[4/17] env_name (Environment Name): my-ai-project-env
[5/17] author (Author Name): Jane Doe
[6/17] email (Author Email): jane.doe@example.com
[7/17] description (Project Description): AI project development
[8/17] reviewer (Independent Reviewer GitHub): 
[9/17] site_name (Documentation Site Name): My AI Project Docs
[10/17] os (Operating System) [Linux, Windows, Mac]: Linux
[11/17] cloud (Cloud Provider) [Google Cloud, AWS, Azure]: AWS
[12/17] ml_type (ML Project Type) [Package, Supervised, Unsupervised, Generative AI]: Generative AI
[13/17] data_type (Data Type) [Structured, Unstructured, Semi-structured]: Unstructured
[14/17] packaging (Packaging Tool) [Poetry, Conda]: Poetry
[15/17] venv (Create Virtual Environment) [Yes, No]: Yes
[16/17] formatter (Code Formatter) [Black, Ruff]: Black
[17/17] docker (Use Docker with VS Code Dev Containers) [Yes, No]: Yes
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

## Resulting Directory Structure

Below is an example directory structure for a Generative AI project that
fine-tunes a Named Entity Recognition (NER) model using SpaCy
Transformers to create a Python package:

```text
.
├── .benchmarks                     # Benchmark files for performance testing.
├── .devcontainer                   # Configuration files for development containers.
├── .github                         # GitHub-specific files.
│   ├── CONTRIBUTING.md             # Guidelines for contributing to the project.
│   ├── PULL_REQUEST_TEMPLATE       # Template for pull request descriptions.
│   └── workflows                   # GitHub Actions workflows.
│       ├── black.yaml              # Workflow for Black formatter.
│       └── ruff.yaml               # Workflow for Ruff linter.
├── .vscode                         # VS Code configuration.
│   ├── cspell.json                 # Spell checker configuration.
│   ├── dictionaries                # Custom dictionaries for spell checker.
│   │   └── data-science-en.txt
│   ├── extensions.json             # Recommended VS Code extensions.
│   └── settings.json               # VS Code workspace settings.
├── .env                            # Environment variables configuration file.
├── .gitignore                      # Specifies intentionally untracked files to ignore.
├── .coverage                       # Code coverage report.
├── CHANGELOG.md                    # Changelog for the project.
├── Makefile                        # Makefile with commands like `make data` or `make train`.
├── README.md                       # The top-level README for developers using this project.
├── config                          # Configuration files for the project.
│   ├── base_config.yaml
├── dist                            # Distribution files
├── docs                            # Project documentation.
│   ├── api-reference.md
│   ├── assets
│   │   ├── css
│   │   │   └── custom.css
│   │   └── logo.png
│   ├── explanation.md
│   ├── how-to-guides.md
│   ├── index.md
│   └── tutorials.md
├── mkdocs.yml                      # MkDocs configuration for generating documentation.
├── notebooks                       # Jupyter notebooks for exploration and analysis.
├── poetry.lock                     # Poetry lock file for dependencies.
├── pyproject.toml                  # Project configuration file for dependencies and tools.
├── src                             # Source code for the project.
│   ├── package_name                # Main package directory.
│   │   ├── __init__.py             # Initialization file for the package.
│   │   ├── module1.py              # Generic module 1.
│   │   ├── module2.py              # Generic module 2.
│   │   ├── module3.py              # Generic module 3.
│   │   ├── data                    # Data handling modules.
│   │   │   ├── __init__.py
│   │   │   ├── external
│   │   │   ├── features
│   │   │   ├── interim
│   │   │   ├── processed
│   │   │   └── raw
│   │   ├── logs
│   │   │   └── application.log
│   │   └── models                  # Model files
│   ├── common
│   │   └── utils.py                # Common utility functions.
└── tests                           # Unit and integration tests.
    └── __pycache__
        ├── test_module1.py
        └── test_module2.py
```