# Contributing

- [Contributing](#contributing)
  - [Contributor's Guide to Tooling and Setup Assumptions](#contributors-guide-to-tooling-and-setup-assumptions)
    - [Essential Tooling](#essential-tooling)
  - [Steps to Set Up Your Python Development Environment on Docker](#steps-to-set-up-your-python-development-environment-on-docker)
    - [1. Open Project in Container](#1-open-project-in-container)
    - [2. Adding Extensions in Your Container](#2-adding-extensions-in-your-container)
    - [3. Setting Up `pyenv` on Debian Linux](#3-setting-up-pyenv-on-debian-linux)
      - [3.1. Installing `pyenv`](#31-installing-pyenv)
      - [3.2. Set Up `pyenv` with Python 3.10.13](#32-set-up-pyenv-with-python-31013)
      - [3.3. Quick Start with `pipx`](#33-quick-start-with-pipx)
    - [4. Install Poetry with `pipx`](#4-install-poetry-with-pipx)
      - [4.1. Setting Up a Virtual Environment with Poetry](#41-setting-up-a-virtual-environment-with-poetry)
      - [4.2. Auto-Activate Poetry Environment in VS Code](#42-auto-activate-poetry-environment-in-vs-code)
    - [5. SSH Setup for GitHub in VS Code Dev Container](#5-ssh-setup-for-github-in-vs-code-dev-container)
    - [6. Getting Started with Git and GitHub](#6-getting-started-with-git-and-github)
      - [6.1. Pushing to GitHub](#61-pushing-to-github)
    - [7. Quick Guide to MkDocs for Documentation](#7-quick-guide-to-mkdocs-for-documentation)
    - [8. Updating CSpell Dictionary with Python Terms](#8-updating-cspell-dictionary-with-python-terms)
    - [9. Exiting VS Code Dev Containers](#9-exiting-vs-code-dev-containers)
    - [10. Running Tests](#10-running-tests)

## Contributor's Guide to Tooling and Setup Assumptions

Ready to make your contribution? Here's a quick overview of the
essential tools you'll need and some assumptions we make to ensure
you're all set for a seamless setup process.

### Essential Tooling

| Tool                                                                         | Notes                                                                                              |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [Python](https://www.python.org/)                                            | The foundational language of our project. Ensure it's installed first.                             |
| [pyenv](https://github.com/pyenv/pyenv)                                      | A lifesaver for managing multiple Python versions effortlessly.                                    |
| [Poetry](https://github.com/python-poetry/poetry)                            | Our go-to for handling dependencies and packaging with minimal fuss.                               |
| [VS Code](https://code.visualstudio.com/)                                    | The recommended code editor for its robust features and wide acceptance.                           |
| [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Optional) | Perfect for those who prefer a containerized development environment for consistency and isolation.|
| [Git](https://git-scm.com/)                                                  | Our version control backbone, essential for collaborative coding and codebase management.          |
| [GitHub](https://github.com/)                                                | The platform where our project resides.                                                            |
| [Doccano](https://github.com/doccano/doccano/)                               | Best installed on Docker Desktop if you're using it. Useful for labeling or annotation tasks.      |

>If fine-tuning language models with GPU access is part of your work,
>Docker containers might not work. It's expected that all required tools
>are installed on your host machine or in the cloud, assuming GPU access
>is available there.

## Steps to Set Up Your Python Development Environment on Docker

### 1. Open Project in Container

After checking your settings, open VS Code's command palette
(`Ctrl+Shift+P` or `Cmd+Shift+P`) and choose "Remote-Containers: Reopen
in Container" to launch your project inside a container. The initial
setup might take a bit, but it'll be quicker next time.

### 2. Adding Extensions in Your Container

Once you're in your containerized environment in VS Code, adding the
necessary extensions is easy:

1. **Find Remote Explorer**: It's on the sidebar, symbolized by two
   screens or a remote window, used for managing remote connections.

2. **Choose Your Container**: Look for "Python 3 @ desktop-linux" in the
   Remote Explorer and click on it.

3. **Install Extensions**: Click the cloud icon with a download arrow at
   the bottom right of the Dev Container tab to see available
   extensions. Select the ones you need for your project.

4. **Confirm Installation**: After choosing, hit "OK" to install them.

### 3. Setting Up `pyenv` on Debian Linux

`pyenv` is a tool that makes managing multiple Python versions simple,
particularly useful in Debian Linux. Follow these steps to install
`pyenv` and ensure you can easily switch between Python versions for
your projects.

#### 3.1. Installing `pyenv`

Start by installing essential packages for `pyenv`. Run this in your
terminal:

```shell
sudo apt install curl git-core gcc make zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libssl-dev
```

Next, clone `pyenv` from its GitHub repo for the latest version:

```shell
git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv
```

Now, define where `pyenv` is installed and make it recognizable to your
system by adding a few lines to your `.bashrc` file:

1. Open `.bashrc` with a text editor, like `nano`:

   ```shell
   nano $HOME/.bashrc
   ```

2. Append these lines for `pyenv` setup:

   ```bash
   export PYENV_ROOT="$HOME/.pyenv"
   export PATH="$PYENV_ROOT/bin:$PATH"
   if command -v pyenv 1>/dev/null 2>&1; then
     eval "$(pyenv init -)"
   fi
   ```

To exit nano after editing, press `Control` + `X`, then `Y` to save
changes, and `Enter` to confirm and exit.

Reload `.bashrc` or restart your shell to apply changes:

```shell
source $HOME/.bashrc
```

#### 3.2. Set Up `pyenv` with Python 3.10.13

Once `pyenv` is installed, setting it to use a specific Python version,
such as 3.10.13, is straightforward:

1. Install Python 3.10.13:

   ```shell
   pyenv install 3.10.13
   ```

2. Set it as the global version:

   ```shell
   pyenv global 3.10.13
   ```

Check the active Python version with `python --version` to confirm the
setup.

#### 3.3. Quick Start with `pipx`

Ensure `pipx` is ready in your environment for isolated Python package
management:

1. **Check Installation**:

   ```bash
   pipx --version
   ```

   Confirm `pipx` is installed with the version displayed.

2. **Update `pipx`** (Optional):

   ```bash
   python3 -m pip install --upgrade pipx
   ```

   Keeps `pipx` up-to-date.

Verify `pipx` is installed or updated by rerunning the version check.

### 4. Install Poetry with `pipx`

Quickly set up Poetry for managing dependencies:

1. **Install Poetry**:

   ```bash
   pipx install poetry
   ```

   This isolates Poetry, avoiding conflicts with other packages.

2. **Update Poetry** (Optional):

   ```bash
   pipx upgrade poetry
   ```

   Ensures you're using the latest version.

#### 4.1. Setting Up a Virtual Environment with Poetry

Create an isolated environment for your project using Poetry:

1. **Verify Python Version**: Confirm Poetry is set to the desired Python version with:

   ```zsh
   poetry env use 3.10.13
   ```

2. **Install Dependencies**: At your project root (where `pyproject.toml` is), run:

   ```shell
   poetry install
   ```

3. **Activate Environment**: Enter the environment with:

   ```shell
   poetry shell
   ```

4. **Check Installation**: Ensure all dependencies are installed:

   ```shell
   poetry show
   ```

5. **Environment Info**: Get detailed environment information:

   ```shell
   poetry env info
   ```

#### 4.2. Auto-Activate Poetry Environment in VS Code

To ensure that VS Code automatically uses your Poetry virtual
environment, especially when working remotely, follow these steps:

1. **Obtain the Virtual Environment Path**:
   - Open the VS Code terminal.
   - Retrieve the path to your Poetry-managed virtual environment by
     executing:

     ```bash
     poetry env info --path
     ```

   This command will provide the path to the virtual environment. Note
   this path as you will need it to configure the remote settings.

2. **Accessing Remote Settings in VS Code**:
   - Click the gear icon located on the bottom left corner of VS Code to
     open the Command Palette.
   - Go to `Settings`, then select `Remote [Environment]`, where
     `[Environment]` corresponds to your remote environment type (e.g.,
     Remote-SSH, Remote-Containers).
   - On the top right corner of the settings UI, click on the `{}` icon
     to open the `settings.json` file for remote settings.

3. **Create and Configure the Remote Settings JSON File**:
   - Based on the path obtained from the `poetry env info --path`
     command, you need to configure the `Remote settings.json` file in
     your VS Code environment. Use a generic placeholder for the path in
     this professional guide:

     ```json
     {
       "python.terminal.activateEnvInCurrentTerminal": true,
       "python.defaultInterpreterPath": "<Your-Virtual-Env-Path>",
       "ruff.args": [
           "--config=pyproject.toml",
           "--preview"
       ],
       "ruff.path": [
           "<Your-Virtual-Env-Path>/bin/ruff"
       ],
       "ruff.interpreter": [
           "<Your-Virtual-Env-Path>/bin/python"
       ]
     }
     ```

     - **`<Your-Virtual-Env-Path>`**: Replace this placeholder with the
       actual path to your virtual environment.
     - **`python.defaultInterpreterPath`**: Sets the Python interpreter
       to the one located in your virtual environment.
     - **`ruff.args`**: Includes all necessary command-line arguments
       for `ruff`.
     - **`ruff.path`** and **`ruff.interpreter`**: Make sure these paths
       point directly to the executables within your Poetry environment.

By implementing these steps, VS Code will automatically activate your
Poetry virtual environment whenever you open a terminal session in your
remote workspace, ensuring all Python executions and tool uses are
correctly configured for your environment.

### 5. SSH Setup for GitHub in VS Code Dev Container

Quickly set up SSH for GitHub within your Dev Container:

1. **Create the `.ssh` Directory:** If `.ssh` does not exist in your
   container, create it in the home directory of the `vscode` user.

    ```bash
    mkdir -p /home/vscode/.ssh
    ```

2. **Set the Correct Permissions:** Apply restricted permissions to the
   `.ssh` directory.

    ```bash
    chmod 700 /home/vscode/.ssh
    ```

3. **Transfer SSH Keys and Config from Host to Container:** Copy your
   SSH key files and configuration from the host to the container. The
   `docker cp` command should be executed on the host's terminal, not
   inside the container. Copy the container ID from the running
   container on Docker Desktop.

    ```bash
    docker cp ~/.ssh/id_ed25519_corporate <container_id>:/home/vscode/.ssh/
    docker cp ~/.ssh/id_ed25519_corporate.pub <container_id>:/home/vscode/.ssh/
    docker cp ~/.ssh/id_ed25519_personal <container_id>:/home/vscode/.ssh/
    docker cp ~/.ssh/id_ed25519_personal.pub <container_id>:/home/vscode/.ssh/
    docker cp ~/.ssh/config <container_id>:/home/vscode/.ssh/
    ```

4. **Set Correct Permissions for SSH Keys and Config:** Adjust
   permissions for the SSH keys and config file inside the container.

    ```bash
    sudo chmod 600 /home/vscode/.ssh/id_ed25519_corporate
    sudo chmod 644 /home/vscode/.ssh/id_ed25519_corporate.pub
    sudo chmod 600 /home/vscode/.ssh/id_ed25519_personal
    sudo chmod 644 /home/vscode/.ssh/id_ed25519_personal.pub
    sudo chmod 600 /home/vscode/.ssh/config
    ```

5. **Change Ownership of the SSH Files:** Change file ownership to the
   `vscode` user.

    ```bash
    sudo chown -R vscode:vscode /home/vscode/.ssh/
    ```

6. **Add SSH Keys to the Agent:** Add your SSH keys to the SSH agent in
   the container.

     ```bash
     ssh-add /home/vscode/.ssh/id_ed25519_corporate
     ssh-add /home/vscode/.ssh/id_ed25519_personal
     ```

7. **Test SSH Connection:** Verify the setup by testing the SSH
   connection.

     ```bash
     ssh -T git@github.com-corporate
     ```

### 6. Getting Started with Git and GitHub

Using Git for version control in your local repository and pushing to
GitHub when you're ready is a great way to manage and share your
project. Here's how to get started:

1. **Configure Git Global Settings:** Set your Git username and email
   globally within the container. This is important for proper
   attribution of your commits.

     ```bash
     git config --global user.email "you@example.com"
     git config --global user.name "Your Name"
     ```

2. **Initialize a New Git Repository:** In the root directory of your
   project, run the following command to initialize a new Git
   repository:

   ```bash
   git init
   ```

   This creates a new `.git` subdirectory, which stores all of your
   project's version history.

3. **Add Files to the Repository:** After initializing the repository,
   add your project files to it. Check the status of your repository
   with:

   ```bash
   git status
   ```

   This shows which files are untracked or modified. To add all your
   files to the repository, use:

   ```bash
   git add .
   ```

4. **Commit Your Changes:** Commit these changes to take a snapshot of
   your current project state. Commit with a message describing your
   changes:

   ```bash
   git commit -m "Initial commit"
   ```

5. **Continue Developing:** Keep making changes to your files. Regularly
   commit your changes with `git add` and `git commit`.

#### 6.1. Pushing to GitHub

Once you're ready to share your work or back it up on GitHub, follow
these steps:

1. **Create a New Repository on GitHub:**
   - Go to [GitHub](https://github.com) and sign in.
   - Click the '+' icon in the upper right corner and select 'New
     repository'.
   - Name your repository and leave it empty (no README, .gitignore, or
     license).

2. **Link Your Local Repository to GitHub:** Back in your local project,
   link it to your GitHub repository with:

   ```bash
   git remote add origin https://github.com/yourusername/{{cookiecutter.project_slug}}.git
   ```

3. **Push Local Repository to GitHub:** Push your local repository to
   GitHub with:

   ```bash
   git push -u origin main
   ```

   This command pushes your commits to GitHub, and the `-u` flag sets
   the remote repository as the upstream for future pushes.

### 7. Quick Guide to MkDocs for Documentation

We use MkDocs with the Material theme for sleek, easy-to-navigate
documentation. Here’s how to work with it:

- **Build Documentation**: Generate static site files with:

  ```bash
  mkdocs build
  ```

- **Live Preview**: For real-time updates as you edit, run:
  
  ```bash
  mkdocs serve
  ```

  This launches a local server. View your docs at
  `http://127.0.0.1:8000/{{cookiecutter.project_slug}}/`. Changes
  auto-refresh.

Stop the server with `Ctrl + C`. Restarting your VS Code session
afterward ensures your edits fully update.

### 8. Updating CSpell Dictionary with Python Terms

Improve spell checking by adding Python library terms to CSpell:

```bash
make cspell_dictionary
```

This enriches CSpell's dictionary with terms from your project's Python
libraries, reducing false positives on technical jargon.

### 9. Exiting VS Code Dev Containers

To exit a Dev Container and go back to local VS Code:

1. Click the green corner (bottom-left) showing the remote connection.
2. Choose "Close Remote Connection."

This returns you to your local environment.

### 10. Running Tests

Check the `Acro Expand Package` functionality by running:

```bash
poetry run pytest
```