# Project Scaffolding Standards for AI/ML Projects

## Overview

Establishing a standardized project structure is essential for
maintaining organization, enhancing collaboration, and ensuring
consistency across all AI/ML projects. This guide outlines the
recommended folder and file structure to follow for all projects within
the AI team.

## Folder and File Structure

Here is the standardized folder and file structure for AI/ML projects:

## Project Structure

```text
├── .github
│   ├── CONTRIBUTING.md             <- Guidelines for contributing to the project.
│   ├── PULL_REQUEST_TEMPLATE
│   │   └── pull_request_template.md
│   └── workflows
│       ├── black.yaml              <- GitHub Actions workflow for Black formatter.
│       └── ruff.yaml               <- GitHub Actions workflow for Ruff linter.
├── .gitignore                      <- Specifies intentionally untracked files to ignore.
├── .vscode
│   ├── cspell.json                 <- Spell checker configuration.
│   ├── dictionaries
│   │   └── data-science-en.txt     <- Custom dictionary for spell checker.
│   ├── extensions.json             <- List of recommended VS Code extensions.
│   └── settings.json               <- VS Code workspace settings.
├── .env                            <- Environment variables configuration file.
├── README.md                       <- The top-level README for developers using this project.
├── Makefile                        <- Makefile with commands like `make data` or `make train`.
├── config                          <- Configuration files for the project.
│   ├── base_config.cfg
│   ├── config.cfg
│   └── settings.yaml
├── data                            <- Data files for the project.
│   ├── raw                         <- Raw data files.
│   └── processed                   <- Processed data files.
├── docs                            <- Documentation files for the project.
│   ├── api-reference.md
│   ├── explanation.md
│   ├── how-to-guides.md
│   ├── index.md
│   ├── tutorials.md
│   └── assets                      <- Assets for documentation (images, CSS, etc.).
│       └── ...
├── logs                            <- Logs generated by the project.
│   └── application.log
├── mkdocs.yml                      <- Configuration for mkdocs documentation generation.
├── notebooks                       <- Jupyter notebooks for exploration and analysis.
│   └── ...                         <- Individual notebook files.
├── pyproject.toml                  <- Project configuration file for dependencies and tools.
├── poetry.lock                     <- Lock file for poetry to ensure reproducibility.
├── scripts                         <- Utility scripts for various tasks.
│   ├── preprocess_data.py          <- Script for data preprocessing
│   ├── train_model.py              <- Script for model training
│   ├── deploy_model.py             <- Script for model deployment
│   ├── evaluate_model.py           <- Script for evaluating model performance
│   └── data_operations.py          <- Script for S3 data operations
├── sagemaker                       <- SageMaker-specific scripts and configurations.
│   ├── train_script.py             <- Training script for SageMaker.
│   ├── deploy_script.py            <- Deployment script for SageMaker.
│   ├── preprocessing_script.py     <- Preprocessing script for SageMaker.
│   ├── hyperparameters.json        <- Hyperparameters for SageMaker training jobs.
│   └── sagemaker_config.json       <- Configuration for SageMaker jobs.
├── src                             <- Source code for the project.
│   └── package_name                <- Main package directory.
│       ├── __init__.py             <- Module docstring
│       ├── data_preprocessing
│       │   ├── __init__.py         <- Module docstring
│       │   ├── data_reader.py      <- Module for reading original documents
│       │   ├── data_cleaning.py    <- Module for cleaning and preprocessing documents
│       │   └── data_chunking.py    <- Module for chunking documents
│       ├── embeddings
│       │   ├── __init__.py         <- Module docstring
│       │   ├── embedding_generator.py <- Module for generating embeddings
│       │   └── embedding_utils.py  <- Utility functions for embeddings
│       ├── retrievers
│       │   ├── __init__.py         <- Module docstring
│       │   ├── retriever.py        <- Module for retrieving relevant chunks
│       │   ├── retriever_utils.py  <- Utility functions for retrievers
│       │   └── retriever_preprocessing.py <- Module for pre-processing queries before retrieval
│       ├── generators
│       │   ├── __init__.py         <- Module docstring
│       │   ├── generator.py        <- Module for generating answers from retrieved chunks
│       │   ├── generator_utils.py  <- Utility functions for generators
│       │   └── generation_postprocessing.py <- Module for post-processing generated answers
│       ├── evaluation
│       │   ├── __init__.py         <- Module docstring
│       │   ├── evaluation_metrics.py <- Module for evaluating model performance
│       │   └── evaluation_utils.py <- Utility functions for evaluation
│       ├── utils
│       │   ├── __init__.py         <- Module docstring
│       │   ├── logger.py           <- Module for logging
│       │   ├── config.py           <- Module for configuration management
│       │   ├── constants.py        <- Module for constants used across the project
│       │   └── utils.py            <- General utility functions used across the project
│       ├── main.py                 <- Main entry point for the application
│       └── app.py                  <- Application setup and configuration
├── Dockerfile                      <- Dockerfile for containerizing the application.
└── tests                           <- Unit and integration tests.
    ├── __init__.py                 <- Module docstring
    ├── test_data_preprocessing.py  <- Tests for data preprocessing
    ├── test_embeddings.py          <- Tests for embedding generation
    ├── test_retrievers.py          <- Tests for retrievers
    │   └── test_retriever_preprocessing.py <- Tests for query pre-processing
    ├── test_generators.py          <- Tests for generators
    │   └── test_generation_postprocessing.py <- Tests for post-processing generated answers
    └── test_evaluation.py          <- Tests for evaluation
```

### Notes from conversation wth Guy

I beleive we need a spearated moducle fo the cunking techniques.

yes, the data folder must be there because we need local data for you
to run evaluation etc. So, update the .gitignore file accordignly.
Let's put in the docs the .gitingore that aligns with the above tree.

The `embedding_generator.py` generets the embeddings and push them into
the vector database. Mention this. Both actions happens in the same
moducle. Generate embeddings and populate them into OpenSearch.
Impliciity this module also ingest the metadata.

For the retrivers we need to add another script there, one for the
pre-processing. We do not need it to populate it in the first
interaction but we keep it as placeholder. For example, the
pre-processing is useful if we get questions that are not well formed
so, if we want to do query expansion we can hadle it in a pre-process
module. So, here we are going to do query pre-processing things like.
For example query expansion or acronym expansion. So, anything we do
with the query before put in into the retrieval.

For generation, we need a post-processing module to include thinghs such
as content moderation. Or  to include the code aobut showoing the
citation.

Include a general util for cross function modules maybe the name can be
helper.py.

Notice that we already have a Docker file there.

Docker compose, for backend
We need also the requiremts.txt file, the dependencies.
The readme.md put links to all data etc....

We need the dependicies for the backend.

In summary, I need to put there:

- README.md
- CONTRIBUTING.md
- pyproject.toml (instead of the requirements.txt)
- .gitignore
- empty files and folders with the right names.

### Summary of Changes

1. **.env File**: Included for managing environment variables locally.
2. **data Folder**: Kept for storing raw and processed data files, useful during local development.
3. **SageMaker Folder**: Added for SageMaker-specific scripts and configurations to manage training and deployment.
4. **Scripts Folder**: Added for utility scripts that support various tasks such as preprocessing, training, deployment, and data operations.
5. **Dockerfile**: Included for containerizing the application, ensuring a consistent development and production environment.
6. **Additional Documentation Files**: Included `LICENSE` and `CODE_OF_CONDUCT.md` for legal and community guidelines.

This structure is designed to support development workflows for Data
Scientists initially and can be easily extended as Machine Learning
Engineers join the project. It also ensures that both local development
and deployment to AWS SageMaker are well-organized and manageable. o
```

## Directory Descriptions

- **README.md**: A top-level README file that provides an overview of
  the project, how to set up and use it, and any other relevant
  information for developers.

- **Makefile**: Contains commands for setting up and running the
  project, such as `make data` for data preparation or `make train` for
  model training.

- **config/**: Contains configuration files used by the project. These
  files define various settings and parameters needed for the project.

- **dist/**: Stores distribution files for the project, such as wheels
  and tarballs for package distribution.

- **docs/**: Contains all documentation files, including API references,
  explanations, how-to guides, and tutorials. The assets subdirectory
  holds images and CSS used in the documentation.

- **logs/**: Stores log files generated by the project, useful for
  debugging and monitoring.

- **mkdocs.yml**: Configuration file for generating project
  documentation using mkdocs.

- **notebooks/**: Contains Jupyter notebooks for exploratory data
  analysis and experiments.

- **poetry.lock**: Poetry lock file that specifies the exact versions of
  dependencies used in the project.

- **pyproject.toml**: Project configuration file that defines
  dependencies, tools, and other settings for the project.

- **src/**: Contains all source code for the project. This includes data
  management scripts, model definitions, utility scripts, and any other
  code needed for the project.

- **tests/**: Contains all unit and integration tests for the project.
  Each test module typically corresponds to a module in the src
  directory.

- **.devcontainer/**: Configuration for VS Code Dev Containers to ensure
  a consistent development environment.

- **.github/**: Contains GitHub-specific files for repository
  management, including issue templates, pull request templates,
  workflows, and contributing guidelines.

- **.gitignore**: Specifies intentionally untracked files to ignore,
  helping to keep the repository clean.

- **.vscode/**: Contains settings and extensions for Visual Studio Code
  to ensure a consistent development environment.

## Example Structure

### Config Directory

The config directory holds all configuration files required by the
project:

```plaintext
config/
├── base_config.cfg
├── config.cfg
└── settings.yaml
```

### Documentation Directory

The docs directory includes various types of documentation and assets:

```plaintext
docs/
├── api-reference.md
├── explanation.md
├── how-to-guides.md
├── index.md
├── tutorials.md
└── assets/
    ├── images/
    │   └── example.png
    ├── css/
    │   └── custom.css
    └── logo.png
```

### Source Directory

The src directory contains all the source code organized into
subdirectories:

```plaintext
src/
├── project_name/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── external/
│   │   ├── features/
│   │   ├── interim/
│   │   └── processed/
│   ├── models/
│   │   ├── __init__.py
│   │   └── model.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── utils.py
│   └── logs/
│       └── application.log
└── tests/
    ├── __init__.py
    ├── test_data.py
    ├── test_models.py
    └── test_utils.py
```

## Note on Shared Configuration Files for ML/AI Projects

To ensure consistency and maintain high standards across all ML/AI
projects, specific files have been pre-configured and included in the
GitHub repository. These files contain settings and configurations that
enforce standardized practices for all developers involved in the
project. As such, these files should not be modified by individual
developers. The pre-configured files help to ensure that everyone
follows the same standards, enhancing collaboration and project
management.

### Files That Should Not Be Modified by Developers

The following files and sections are crucial for maintaining the
project's standards and should not be altered:

#### .vscode Folder Content
The `.vscode` folder contains settings and extensions for Visual Studio
Code to ensure a consistent development environment for all team
members.

#### .github Folder Content
The `.github` folder includes files for repository management, such as
issue templates, pull request templates, workflows, and contributing
guidelines.

#### .devcontainer Folder Content
The `.devcontainer` folder holds configuration files for VS Code Dev
Containers, providing a consistent development environment setup.

#### pyproject.toml Sections
Specific sections in the `pyproject.toml` file are configured to enforce
coding standards and dependencies. These sections should not be
modified:

- **[tool.poetry.dev-dependencies]**
- **[tool.poetry.group.dev.dependencies]**
- **[tool.black]**
- **[tool.ruff]**
- **[tool.pymarkdown]**
- **[tool.coverage.report]**

By keeping these files and sections untouched, we ensure that all
developers are adhering to the same standards, which is critical for
maintaining code quality and project consistency. The person who set up
the GitHub repository has included these configurations to streamline
the development process and enforce best practices.

### Summary

- **.vscode Folder**: Contains settings and extensions for a consistent
  VS Code environment.
- **.github Folder**: Includes repository management files and
  templates.
- **.devcontainer Folder**: Provides configuration for VS Code Dev
  Containers.
- **pyproject.toml Sections**: Enforces coding standards and
  dependencies.

These pre-configured files and settings help to maintain uniformity and
high standards across the project, ensuring that all team members follow
the same practices. Therefore, developers should not modify these files.

## Conclusion

Following this standardized folder and file structure will help maintain
consistency and readability across all AI/ML projects, making it easier
for team members to collaborate and manage the project effectively. This
structure ensures that all necessary components are well-organized and
easily accessible.