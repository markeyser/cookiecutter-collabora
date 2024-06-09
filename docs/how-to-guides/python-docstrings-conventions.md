# Docstring Guide Using Google Style

## Overview

Docstrings are a crucial part of writing clear and maintainable code.
This guide explains how to write docstrings following the Google style,
providing examples for module-level, class-level, and method-level
docstrings. Additionally, we will cover how to automate the creation of
these docstrings using the VS Code extension
[autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring).

## Module-Level Docstring

The module-level docstring is placed at the very top of the Python
script. It provides an overview of the module's purpose and
functionality.

```python
"""
This module provides text processing utilities for NLP projects.

The utilities include functions for text cleaning, tokenization, and sentiment analysis.
"""
```

## Class-Level Docstring

The class-level docstring describes the class's purpose and provides an
overview of its functionality.

```python
class TextProcessor:
    """
    A class used to perform text processing for NLP tasks.

    This class includes methods for cleaning text, tokenizing sentences,
    and calculating sentiment scores.
    
    Attributes:
        language (str): The language of the text to be processed.
    """
```

## Method-Level Docstrings

Each method should have a docstring explaining what the method does, its
parameters, return values, any exceptions it raises, and providing an
example if necessary.

```python
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
        Cleans the input text by removing special characters and extra spaces.

        Args:
            text (str): The text to be cleaned.

        Returns:
            str: The cleaned text.

        Raises:
            TypeError: If the input text is not a string.
        """
        if not isinstance(text, str):
            raise TypeError("Input text must be a string")
        # Implementation goes here
        pass

    def tokenize(self, text):
        """
        Tokenizes the input text into a list of words.

        Args:
            text (str): The text to be tokenized.

        Returns:
            list: A list of words (tokens).

        Raises:
            TypeError: If the input text is not a string.
        """
        if not isinstance(text, str):
            raise TypeError("Input text must be a string")
        # Implementation goes here
        pass

    def analyze_sentiment(self, text):
        """
        Analyzes the sentiment of the input text.

        Args:
            text (str): The text to be analyzed.

        Returns:
            float: The sentiment score of the text.

        Raises:
            TypeError: If the input text is not a string.
        """
        if not isinstance(text, str):
            raise TypeError("Input text must be a string")
        # Implementation goes here
        pass
```

## Automating Docstring Creation with autoDocstring

### Configuration Setup

The following settings in `.vscode/settings.json` configure
autoDocstring to use the Google style format for docstrings:

```json
// #############################
// ### Docstring ####
// #############################
// Use Google format for docstrings
"autoDocstring.docstringFormat": "google",
// Include Extended Summary section
"autoDocstring.includeExtendedSummary": true,
// Do not include function name at the start of docstrings
"autoDocstring.includeName": false,
```

### Using autoDocstring

1. Place your cursor inside the function or method where you want to add
   a docstring.
2. Trigger the autoDocstring generation by opening the Command Palette
   (`Ctrl+Shift+P` or `Cmd+Shift+P`), typing `Generate Docstring`, and
   selecting it.
3. The extension will automatically generate a Google-style docstring
   template for you.

### Example

Before using autoDocstring:

```python
def clean_text(text):
    # Implementation goes here
    pass
```

After using autoDocstring:

```python
def clean_text(text):
    """
    Cleans the input text by removing special characters and extra spaces.

    Args:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.

    Raises:
        TypeError: If the input text is not a string.
    """
    # Implementation goes here
    pass
```

## Full Example

Here is the complete example with all docstrings included:

```python
"""
This module provides text processing utilities for NLP projects.

The utilities include functions for text cleaning, tokenization, and sentiment analysis.
"""

class TextProcessor:
    """
    A class used to perform text processing for NLP tasks.

    This class includes methods for cleaning text, tokenizing sentences,
    and calculating sentiment scores.
    
    Attributes:
        language (str): The language of the text to be processed.
    """

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
        Cleans the input text by removing special characters and extra spaces.

        Args:
            text (str): The text to be cleaned.

        Returns:
            str: The cleaned text.

        Raises:
            TypeError: If the input text is not a string.
        """
        if not isinstance(text, str):
            raise TypeError("Input text must be a string")
        # Implementation goes here
        pass

    def tokenize(self, text):
        """
        Tokenizes the input text into a list of words.

        Args:
            text (str): The text to be tokenized.

        Returns:
            list: A list of words (tokens).

        Raises:
            TypeError: If the input text is not a string.
        """
        if not isinstance(text, str):
            raise TypeError("Input text must be a string")
        # Implementation goes here
        pass

    def analyze_sentiment(self, text):
        """
        Analyzes the sentiment of the input text.

        Args:
            text (str): The text to be analyzed.

        Returns:
            float: The sentiment score of the text.

        Raises:
            TypeError: If the input text is not a string.
        """
        if not isinstance(text, str):
            raise TypeError("Input text must be a string")
        # Implementation goes here
        pass
```

For more details, refer to the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).

## Requesting Google-Style Docstrings from ChatGPT

A fast and easy way to create Google-style docstrings is by using
ChatGPT. You can provide a simple prompt to request the creation of the
docstring for any Python function.

### Example Prompt

Here’s an example prompt you could use with ChatGPT to request a
Google-style docstring following the settings in your
`.vscode/settings.json` file:

**Prompt:**

```plaintext
Create a Google-style docstring for the following Python function:

def add_numbers(a, b):
    result = a + b
    return result
```

### Generated Docstring

Using the prompt above, ChatGPT will generate a docstring similar to
this:

```python
def add_numbers(a, b):
    """
    Adds two numbers together.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.

    Raises:
        TypeError: If either 'a' or 'b' is not an integer.
    """
    result = a + b
    return result
```

By following these guidelines and using the autoDocstring extension or a
ChatGPT-like app, you can ensure that your Python code is
well-documented and easy to understand for other developers.