# Introduction to Testing with Doctest for Data Scientists

This guide introduces you to `doctest`, a simple and effective tool for
testing and documenting your Python code. As a team of data scientists,
you might not have extensive coding experience, but `doctest` provides a
straightforward way to ensure your code works as expected while also
serving as a form of documentation.

## What is Doctest?

`doctest` is a module included in the Python standard library that
allows you to test your code by running examples embedded in the
documentation and verifying that they produce the expected results. This
approach helps to ensure that your code works as documented.

## Why Use Doctest?

- **Ease of Use**: `doctest` is simple to set up and use, making it an
  excellent starting point for those new to testing.
- **Documentation**: Tests written with `doctest` serve as both test
  cases and examples of how to use your functions, improving code
  readability and usability.
- **Immediate Feedback**: Running `doctest` provides immediate feedback
  on whether your code is working as expected.

## Why Unit Testing is Important

Even though libraries like pandas, scikit-learn, and TensorFlow are
well-tested and reliable, it’s crucial to unit test your custom code. In
machine learning projects, custom code often includes data
preprocessing, feature engineering, model evaluation, and utility
functions. Ensuring the correctness of this code is vital for the
accuracy and reliability of your models. Unit testing helps catch errors
early, facilitates code maintenance, and promotes confidence in your
code’s functionality.

As a data scientist, testing your code before opening a pull request
(PR) and merging it into the production branch is critical. This
practice is especially important in projects like Retrieval-Augmented
Generation (RAG) systems, where data scientists are expected to
contribute to production code from the very beginning. Unlike
traditional machine learning projects, RAG systems require seamless
integration of custom code into the production environment, making
thorough testing essential to prevent potential issues and ensure smooth
operation.

By incorporating unit testing into your workflow, you ensure that your
contributions are reliable and maintain the integrity of the overall
project. This not only enhances the quality of your code but also
promotes collaborative development, where team members can confidently
build upon each other's work.

## Doctest for Simple Unit Tests

Here's an example of how to use doctest with Google-style docstrings:

```python
def add(a, b):
    """
    Adds two numbers together.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.

    Example:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(0, 0)
        0
    """
    return a + b
```

## Running Doctests

To run the doctests in your module, use the following command:

```bash
python -m doctest -v your_module.py
```

## Additional Resources

For further learning on testing in Python, including more advanced
techniques, consider the following resources:

- [Introduction to Testing in Python -
  DataCamp](https://www.datacamp.com/courses/introduction-to-testing-in-python)
- [Python Testing - Real Python](https://realpython.com/python-testing/)
- [Python Unit Testing - Real
  Python](https://realpython.com/python-unittest/)
- [Unit Testing in Python -
  DataCamp](https://www.datacamp.com/tutorial/unit-testing-python)

By following this guide and incorporating doctest into your development
workflow, you can ensure that your code is well-documented, tested, and
reliable. This foundational practice will help you and your team produce
high-quality, maintainable machine learning projects.