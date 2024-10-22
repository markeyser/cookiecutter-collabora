# Using Black Code Formatter in Your Project

!!! example "Running Black Formatter"

    To format your Python script with Black, run the following command in
    your terminal:

    ```bash
    black sample_script.py
    ```

    This command will reformat your `sample_script.py` file according to
    Black's style guidelines.

Black is an uncompromising code formatter. It ensures that your Python
code adheres to a consistent, readable style. The setup you have thanks
to the Cookiecutter template makes it even more convenient to use Black
in various contexts: Python scripts, Jupyter notebooks, and during git
operations. Below are the key points and examples to help you understand
how to use Black in these scenarios.

## VS Code Integration

When you're writing code in VS Code, Black can manually format your
code. Here's how:

!!! note
    In this Cookiecutter template, we've configured Black to be executed
    manually rather than the default automatic approach upon saving.
    This decision offers users greater precision and control, especially
    in Jupyter notebooks where maintaining context and flow is crucial.

### Formatting Python scripts and Jupyter Notebooks with Black

When working with Python scripts and Jupyter notebooks in VS Code, you
can manually format it by pressing `Shift + Opt + F`
or right-click and select `Format Document`, `Format Cell` or `Format
Notebook`.

!!! example "Black Formatting in Action"
    **Before Formatting**:
    ```python
    def calculate(a,b):result=a+b; return result
    ```

    **After Formatting**: 
    ```python
    def calculate(a, b):
        result = a + b
        return result
    ```

!!! info "VS Code Output Window Log"
    When Black formats a script or a notebook, the VS Code output window for the Black
    Formatter provides a detailed log of the operation.

Here's an example of what you might see:

```bash
2023-09-20 12:38:00.934 [info] Sending request 'textDocument/formatting - (5)'.
2023-09-20 12:38:00.936 [info] Received notification 'window/logMessage'.
2023-09-20 12:38:00.936 [info] Running: /Users/markeyser/Library/Caches/pypoetry/virtualenvs/cookiecutter_rag-zDtOoUN1-py3.11/bin/python -m black --stdin-filename /Users/markeyser/Projects/ccookiecutter-genai-ml-ai/checkformatter.py
2023-09-20 12:38:00.938 [info] CWD formatter: /Users/markeyser/Projects/ccookiecutter-genai-ml-ai
2023-09-20 12:38:00.938 [info] reformatted /Users/markeyser/Projects/ccookiecutter-genai-ml-ai/checkformatter.py
All done! ✨ 🍰 ✨
1 file reformatted.
2023-09-20 12:38:00.940 [info] Sending notification 'textDocument/didChange'.
```

This log provides insights into the formatting process, including the
file being formatted, the Black command being executed, and the result
of the formatting operation.

## Command Line Formatting

For those who prefer using the terminal or need to format multiple files
at once, Black can be run directly from the command line.

!!! info "Formatting Commands"
    - For Python scripts, run:
      ```bash
      black your_script.py
      ```

    - For Jupyter notebooks, run: 
      ```bash
      black your_notebook.ipynb
      ```

!!! example "Formatting with Black from the Terminal"
    Suppose you've written a Python script named `sample_script.py` with the following content:

    ```python
    def calculate(a,b):result=a+b; return result
    ```

To format `sample_script.py` using Black, navigate to the directory
containing the script and run:

```bash
black sample_script.py
```

**Terminal Output**:

```
reformatted sample_script.py
All done! ✨ 🍰 ✨
1 file reformatted.
```

**Formatted Code**:

After running the command, your `sample_script.py` will be updated to:

```python
def calculate(a, b):
    result = a + b
    return result
```

## Pre-commit Hooks in Git

Thanks to the pre-configured hooks, any attempt to commit unformatted
Python code will trigger Black to automatically format the code for you.

!!! example "Git Commit with Black"
    Suppose you've written the following code in `sample_script.py`:

    ```python
    def calculate(a,b):result=a+b; return result
    ```

    You decide to commit your changes:

    ```bash
    git add sample_script.py
    git commit -m "Add example function"
    ```

The pre-commit hook will detect the unformatted code and output a message:

```bash
black....................................................................Failed
- hook id: black
- files were modified by this hook
reformatted sample_script.py

All done! ✨ 🍰 ✨
1 file reformatted.
```

Your commit will be halted, but Black will have automatically formatted
your file. You can simply run the commit command again, and this time it
will succeed with the newly formatted code.

## Automated Formatting with GitHub Actions

Upon utilizing the pre-commit hooks for Black, our repository takes an
extra step to ensure code consistency. We've integrated a GitHub Action,
defined in `.github/workflows/black.yml`, that automatically checks and
formats the code whenever new changes are introduced, be it through a
push or a pull request.

This GitHub Action serves a dual purpose:

1. **Automated Code Review**: Before any code merges into the main
   branch, the action ensures it adheres to our predefined formatting
   standards. This guarantees a consistent code style across the
   repository, irrespective of the number of contributors or their
   individual coding environments.

2. **Auto-Fixing Formatting Issues**: If the action detects any code
   that doesn't align with our formatting standards, it doesn't just
   stop at notifying the discrepancy. Instead, it takes a proactive step
   by automatically formatting the code using Black. Once formatted, it
   commits these changes back to the repository. This automation
   minimizes manual interventions, offering a smoother development
   experience. However, a side effect to be aware of is the potential
   addition of extra commits to the git history. While this might make
   the commit log appear denser, we believe the trade-off is worth the
   convenience and consistency it brings to the development process.

When the GitHub Action runs, you might see an output similar to the
following in the action's log:

```bash
reformatted sample_script.py
All done! ✨ 🍰 ✨
1 file reformatted.
```

This output confirms that the action has successfully reformatted the
code to adhere to our standards.

## Skipping Formatting Using Black

If for some reason you need a section of your code to remain unformatted
by Black (for example, due to alignment preferences or specific
readability concerns), you can tell Black to skip that section.

!!! warning "Black Directives for Skipping Formatting"
    To skip formatting for a particular section, you can wrap that
    section of code between `# fmt: off` and `# fmt: on` comments.

    **Example**:

    ```python
    def transformation_matrix():
        # fmt: off
        matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        # fmt: on
        return matrix
    ```

When you run Black on this snippet, the matrix remains untouched, while
the rest of your code (if there were any other parts) would still get
formatted.

If you were to format the above with Black without using the comments,
it might put the entire matrix on a single line if it's short enough, or
it might space things out differently.

```python
def transformation_matrix():
    matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    return matrix
```

## Formatting Multiple Python Files

Formatting multiple Python files with Black can be efficiently handled
in a few ways, depending on your project's structure and your personal
workflow. Here are some approaches:

**Format Entire Directory:** If all your Python files are in a specific
   directory (or directories), you can format them all at once by
   running Black on the directory. For example:

   ```bash
   black path/to/directory/
   ```

**Format Specific File Types:** If you have a mix of file types and only
   want to format the Python files, you can use a command like:

   ```bash
   find . -type f -name "*.py" -exec black {} +
   ```

   This command uses `find` to locate all `.py` files and `black` to
   format each one.

**Integrate with Version Control:** If you're using a version control
   system like Git, you can format only the Python files that have
   changed. This can be particularly useful in a collaborative
   environment. For example, to format all Python files that have been
   modified but not yet committed:

   ```bash
   git diff --name-only --staged | grep '\.py$' | xargs black
   ```

Choose the approach that best fits your workflow and project structure.
Automation and integration with your development tools can significantly
streamline the formatting process.

!!! warning "Branch Protection with Black"

    To ensure code quality, we need to protect the main branch with branch
    protection rules. This setup requires that all code must pass Black
    formatting checks before being merged into the main branch. While you can
    push code to your feature branches even if it fails formatting, merging
    into main is blocked until all formatting errors are resolved. This
    approach mimics pre-commit hooks, maintaining a clean and compliant main
    branch. Developers should run Black locally and fix issues before pushing
    code for review.

## Conclusion

Black ensures consistency and readability across your codebase. With the
integrations provided by the Cookiecutter template, it's easier than
ever to maintain a clean code style, whether you're working in Python
scripts, Jupyter notebooks, or committing changes via git. Remember, a
consistent code style not only makes your codebase look professional but
also reduces cognitive load, making it easier for you and others to
understand and collaborate on the project.

## Further Reading and Resources

For a deeper dive into the functionalities and best practices of using
Black, the following resource is highly recommended:

- [Official Black Documentation](https://black.readthedocs.io/en/stable/)

The official documentation provides a comprehensive guide to Black's
features, configuration options, and integration methods. It's an
excellent resource for understanding the philosophy behind Black and how
to make the most out of this powerful code formatter. Whether you're new
to Black or looking to explore its more advanced features, the official
documentation is a valuable resource.
