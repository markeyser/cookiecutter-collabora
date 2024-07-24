# Writing Google-Style Docstrings and Inline Commentaries

!!! example "ChatGPT Prompt for adding docstrings and commentaries"

    ```plaintext
    You are a world-class Python developer with an eagle eye for detail and
    a deep understanding of best practices in code documentation. Please
    complete the following tasks for the provided Python class:
    
    1. Create Google-style docstrings for the class. This includes:
        - A public module docstring at the very top of the module before the
          imports.
        - A docstring for the class.
        - A docstring for the `__init__` method.
        - Docstrings for all other methods.
    
    2. Add inline commentaries to the Python code. These commentaries
       should:
        - Be one-liner commentaries.
        - Have a length of each text line inside the commentary of 79
          characters or fewer.
        - Provide useful information to the user and not be redundant.
    
    The docstrings must adhere to the following guidelines:
    - Use Google style docstrings.
    - The length of each text line inside the docstring must be 72
      characters or fewer.
    
    Examples of Desired Style:
    
    Module-Level Docstring:
    
    """ This module provides text processing utilities for NLP projects.
    
    The utilities include functions for text cleaning, tokenization, and
    sentiment analysis.  """
    
    Class-Level Docstring:
    
    class TextProcessor: """ A class used to perform text processing for NLP
        tasks.
    
        This class includes methods for cleaning text, tokenizing sentences,
        and calculating sentiment scores.
    
        Attributes:
            language (str): The language of the text to be processed.
        """
    
    Method-Level Docstrings:
    
        def __init__(self, language):
            """
            Initializes the TextProcessor with a specified language.
    
            Args:
                language (str): The language of the text to be processed.
    
            Raises:
                ValueError: If the provided language is not supported.
            """
            if language not in ['en', 'es', 'fr']:
                raise ValueError(f"Unsupported language: {language}")
            self.language = language
    
        def clean_text(self, text):
            """
            Cleans the input text by removing special characters and
            extra spaces.
    
            Args:
                text (str): The text to be cleaned.
    
            Returns:
                str: The cleaned text.
    
            Raises:
                TypeError: If the input text is not a string.
            """
            if not isinstance(text, str):
                raise TypeError("Input text must be a string")
            pass
    
    Placeholder for User's Python Class:
    
    # Please replace the code below with the actual Python class
    
    class SampleClass: def __init__(self, param1, param2): self.param1 =
        param1 self.param2 = param2
    
        def method_one(self, arg1):
            pass
    
        def method_two(self, arg1, arg2):
            pass
    
    Request:
    
    Here is the Python class for which I need Google-style docstrings and
    inline commentaries. Please provide the necessary docstrings and
    commentaries as specified above.
    
    [Replace this comment with the actual Python class code]
    ```

### Example

#### Original Python Class

```python
class SampleClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method_one(self, arg1):
        pass

    def method_two(self, arg1, arg2):
        pass
```

#### Refactored Python Class with Docstrings and Commentaries

```python
"""
This module provides a sample class for demonstration purposes.

The SampleClass includes methods that demonstrate the use of Google-style
docstrings and inline commentaries.
"""

class SampleClass:
    """
    A sample class used to demonstrate Google-style docstrings.

    This class includes methods for demonstration purposes.

    Attributes:
        param1 (Any): The first parameter.
        param2 (Any): The second parameter.
    """

    def __init__(self, param1: Any, param2: Any):
        """
        Initializes the SampleClass with specified parameters.

        Args:
            param1 (Any): The first parameter.
            param2 (Any): The second parameter.
        """
        self.param1 = param1  # Initialize param1
        self.param2 = param2  # Initialize param2

    def method_one(self, arg1: Any) -> None:
        """
        A method that demonstrates a simple operation.

        Args:
            arg1 (Any): An argument for the method.
        """
        pass  # Placeholder for method_one implementation

    def method_two(self, arg1: Any, arg2: Any) -> None:
        """
        Another method that demonstrates a different operation.

        Args:
            arg1 (Any): The first argument for the method.
            arg2 (Any): The second argument for the method.
        """
        pass  # Placeholder for method_two implementation
```

## Overview

This document provides guidelines on how to add Google-style docstrings
and inline commentaries to your Python code. It serves as an
introduction to best practices for documenting your code to improve
readability, maintainability, and collaboration.

!!! note This guide explains the importance of code documentation,
    provides a prompt for adding docstrings and commentaries, and
    demonstrates how to document a Python class.

## Importance of Code Documentation

- **Readability**: Well-documented code is easier to read and
  understand.
- **Maintainability**: Documentation helps maintain and update code
  efficiently.
- **Collaboration**: Clear documentation facilitates collaboration among
  team members.
- **Error Reduction**: Comprehensive documentation reduces the
  likelihood of errors and misunderstandings.

## Benefits of Google-Style Docstrings and Inline Commentaries

- **Consistency**: Adopting a consistent style of documentation across
  your codebase.
- **Clarity**: Providing clear explanations of the purpose and usage of
  classes and methods.
- **Ease of Use**: Making it easier for others to use and extend your
  code.

## Adding Google-Style Docstrings and Inline Commentaries

To add Google-style docstrings and inline commentaries to your Python
code, follow these steps:

1. **Module-Level Docstring**: Add a public module docstring at the top
   of the module before the imports.
2. **Class-Level Docstring**: Add a docstring for the class, including a
   description and attribute details.
3. **Method-Level Docstrings**: Add docstrings for the `__init__` method
   and all other methods, including arguments, return types, and raised
   exceptions.
4. **Inline Commentaries**: Add useful one-liner commentaries to the
   code, ensuring each line is 79 characters or fewer.

## Example Code

### Original Code (Without Docstrings and Commentaries)

```python
class SampleClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method_one(self, arg1):
        pass

    def method_two(self, arg1, arg2):
        pass
```

### Refactored Code (With Docstrings and Commentaries)

```python
"""
This module provides a sample class for demonstration purposes.

The SampleClass includes methods that demonstrate the use of Google-style
docstrings and inline commentaries.
"""

class SampleClass:
    """
    A sample class used to demonstrate Google-style docstrings.

    This class includes methods for demonstration purposes.

    Attributes:
        param1 (Any): The first parameter.
        param2 (Any): The second parameter.
    """

    def __init__(self, param1: Any, param2: Any):
        """
        Initializes the SampleClass with specified parameters.

        Args:
            param1 (Any): The first parameter.
            param2 (Any): The second parameter.
        """
        self.param1 = param1  # Initialize param1
        self.param2 = param2  # Initialize param2

    def method_one(self, arg1: Any) -> None:
        """
        A method that demonstrates a simple operation.

        Args:
            arg1 (Any): An argument for the method.
        """
        pass  # Placeholder for method_one implementation

    def method_two(self, arg1: Any, arg2: Any) -> None:
        """
        Another method that demonstrates a different operation.

        Args:
            arg1 (Any): The first argument for the method.
            arg2 (Any): The second argument for the method.
        """
        pass  # Placeholder for method_two implementation
```

## Conclusion

By following these guidelines, you can ensure that your Python code is
well-documented with Google-style docstrings and inline commentaries.
This approach enhances the readability, maintainability, and usability
of your code, making it easier to understand and extend.

## Best Practices for Code Documentation

### Introduction

Proper code documentation is a critical component of software
development that improves the maintainability, flexibility, and
scalability of your applications. This section explains the rationale
behind best practices for code documentation, provides a prompt for
automating the documentation process, and demonstrates a basic example
of how to use the prompt with a simple Python class.

### Best Practices

1. **Module-Level Docstring**:
   - **Reason**: Providing a high-level overview of the module helps
     users understand its purpose and functionality.
   - **Example**: Adding a docstring at the top of the module to
     describe the module's purpose and included utilities.

    ```python
    """
    This module provides a sample class for demonstration purposes.

    The SampleClass includes methods that demonstrate the use of Google-style
    docstrings and inline commentaries.
    """
    ```

2. **Class-Level Docstring**:
   - **Reason**: Describing the class, its purpose, and its attributes
     helps users understand its role and how to use it.
   - **Example**: Adding a docstring for the class to describe its
     purpose and attributes.

    ```python
    class SampleClass:
        """
        A sample class used to demonstrate Google-style docstrings.

        This class includes methods for demonstration purposes.

        Attributes:
            param1 (Any): The first parameter.
            param2 (Any): The second parameter.
        """
    ```

3. **Method-Level Docstrings**:
   - **Reason**: Providing detailed information about each method,
     including its arguments, return types, and raised exceptions, helps
     users understand how to use the method and what to expect.
   - **Example**: Adding a docstring for the `__init__` method and other
     methods.

    ```python
    def __init__(self, param1: Any, param2: Any):
        """
        Initializes the SampleClass with specified parameters.

        Args:
            param1 (Any): The first parameter.
            param2 (Any): The second parameter.
        """
        self.param1 = param1  # Initialize param1
        self.param2 = param2  # Initialize param2

    def method_one(self, arg1: Any) -> None:
        """
        A method that demonstrates a simple operation.

        Args:
            arg1 (Any): An argument for the method.
        """
        pass  # Placeholder for method_one implementation

    def method_two(self, arg1: Any, arg2: Any) -> None:
        """
        Another method that demonstrates a different operation.

        Args:
            arg1 (Any): The first argument for the method.
            arg2 (Any): The second argument for the method.
        """
        pass  # Placeholder for method_two implementation
    ```

4. **Inline Commentaries**:
   - **Reason**: Adding useful one-liner commentaries helps explain
     specific parts of the code, making it easier for others to follow
     and understand.
   - **Example**: Adding inline comments to explain variable
     initialization and placeholders.

    ```python
    def __init__(self, param1: Any, param2: Any):
        """
        Initializes the SampleClass with specified parameters.

        Args:
            param1 (Any): The first parameter.
            param2 (Any): The second parameter.
        """
        self.param1 = param1  # Initialize param1
        self.param2 = param2  # Initialize param2
    ```

By following these best practices for code documentation, you can ensure
that your Python code is well-documented, making it more readable,
maintainable, and usable for others. This approach enhances the overall
quality and usability of your codebase.