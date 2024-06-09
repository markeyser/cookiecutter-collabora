# Guide to Using Code Tags in ML/AI Projects

## Overview

Code tags are an essential tool for maintaining readability and
manageability in your codebase. They provide clear markers for important
comments, issues, and reminders, enhancing collaboration and ensuring
critical information is not overlooked. This guide explains why and how
to use code tags in your ML/AI projects, leveraging the VS Code
extensions **CodeTags** and **Todo Highlight**.

## Why Use Code Tags?

1. **Improve Readability**: Highlight important comments, making them
   stand out in the code.
2. **Facilitate Collaboration**: Help team members quickly identify
   issues, requests, and important notes.
3. **Enhance Documentation**: Provide clear and consistent documentation
   within the code.
4. **Ensure Accountability**: Track who is responsible for various parts
   of the code.
5. **Increase Efficiency**: Quickly locate and address critical areas in
   the codebase.

## Setting Up VS Code

To get started, ensure you have the following extensions installed:

- [CodeTags](https://marketplace.visualstudio.com/items?itemName=cg-cnu.vscode-codetags)
- [Todo
  Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight)

The configuration for these extensions is located in your
`.vscode/settings.json` file. This configuration includes specific
keywords for code tags, their styling, and which file types to include
or exclude. Here is a brief overview:

- **Keywords**: Defines various tags like `BUG`, `TODO`, `RFE`, etc.,
  with specific colors and background settings.
- **Include/Exclude**: Specifies which file types and directories should
  be included or excluded from highlighting.

Example settings:

```json
// #############################
// ### CODETAGS ###
// #############################
"todohighlight.keywords": [
    // Keywords and styling configurations...
],
"codetags.custom": [
    // Custom tags and their descriptions...
],
"todohighlight.include": [
    "**/*.js",
    "**/*.jsx",
    "**/*.ts",
    "**/*.tsx",
    "**/*.html",
    "**/*.php",
    "**/*.css",
    "**/*.scss",
    "**/*.py"
],
"todohighlight.exclude": [
    "**/node_modules/**",
    "**/bower_components/**",
    "**/dist/**",
    "**/build/**",
    "**/.vscode/**",
    "**/.github/**",
    "**/_output/**",
    "**/*.min.*",
    "**/*.map",
    "**/.next/**"
]
```

## Using Code Tags in Your Project

Here are some common code tags and their intended use in ML/AI projects:

- **BUG**: To mark sections of code that have known bugs.
- **NOBUG**: To indicate well-known issues that will not be addressed.
- **RFE**: To mark requests for enhancements or features to be added.
- **IDEA**: To highlight ideas or potential improvements.
- **???**: To mark areas of the code that need further investigation.
- **!!!**: To indicate urgent issues that need immediate attention.
- **PORT**: To note portability issues or workarounds.
- **CAVEAT**: To point out non-intuitive implementation details.
- **FAQ**: To highlight frequently asked questions or important notes.
- **GLOSS**: To add glossaries or explanations of terms.
- **SEE**: To provide pointers to other parts of the code or external
  resources.
- **TODOC**: To indicate areas that need documentation.
- **CRED**: To give credit for external help or contributions.
- **STAT**: To indicate the status or maturity of a file.
- **RVD**: To mark files or sections that have been reviewed.
- **NOTE**: To add general notes or important reminders.
- **HACK**: To mark quick and dirty fixes or hacks.
- **TODO**: To indicate tasks that need to be done.

### Example Usage

Here are some examples of how to use these code tags in your Python
code:

```python
# TODO: Implement the function to process the data
def process_data(data):
    """
    Processes the input data.

    Args:
        data (list): The data to be processed.

    Returns:
        list: The processed data.
    """
    pass

# BUG: This function does not handle empty lists properly
def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers.

    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list.")
    return sum(numbers) / len(numbers)

# !!!: This section needs immediate attention to fix performance issues
def perform_heavy_computation(data):
    """
    Performs a heavy computation on the input data.

    Args:
        data (list): The data to be processed.

    Returns:
        list: The result of the computation.
    """
    # Placeholder for the heavy computation logic
    result = [x * x for x in data]  # Optimize this line for better performance
    return result

# SEE: For more details on the algorithm, refer to the research paper (link).
```

### Automation with CodeTags and Todo Highlight

By configuring the `todohighlight.keywords`, `todohighlight.include`,
and `todohighlight.exclude` settings in your `.vscode/settings.json`
file, you can automate the highlighting of important code tags, making
it easier to manage and navigate your codebase.

## Conclusion

Using code tags effectively helps maintain a clean, readable, and
manageable codebase. By following this guide and using the provided VS
Code extensions, you can enhance collaboration, improve documentation,
and ensure critical areas of your code are highlighted and addressed
promptly.