Sure! Here is the updated document with the approach of using a helper module for Pydantic validation.

# Using Pydantic for Input Validation at Runtime

!!! example "ChatGPT Prompt for adding Pydantic-based validation with a helper module"

    ```plaintext
    You are a world-class Python developer with an eagle eye for detail and
    a deep understanding of best practices in using Pydantic for runtime
    input validation in Python classes. I have a Python script, and I want
    to add Pydantic-based input validation to the class methods based on
    these recommendations:
    
    1. Helper Module for Pydantic Validation: Create a helper module to
    define Pydantic models and perform input validation separately from the
    original class.
    2. Validation in Methods: Refactor the methods to use these Pydantic
    models for input validation.
    3. Error Handling: Ensure that validation errors are appropriately
    handled and logged.
    4. Documentation: Document the changes and the purpose of the
    validation for each refactored method.
    5. Consistency: Ensure that the validation is consistent across all
    methods, adhering to the principles of clean code and
    maintainability.
    
    Please produce a helper module with the Pydantic models and validation 
    logic, and refactor the original Python class to use this helper module.

    Here is the script:
    
    ```python
    [Insert your Python script here]
    ```

### Example

#### Original Python Script

```python
class SimpleClass:
    def method(self, param1, param2):
        if not isinstance(param1, int):
            raise TypeError("param1 must be an integer")
        if not isinstance(param2, str):
            raise TypeError("param2 must be a string")
        print(f"param1: {param1}, param2: {param2}")

# Example usage
obj = SimpleClass()
obj.method(1, "example")
```

#### Using the Prompt

To use the prompt, copy the original Python script into the `[Insert
your Python script here]` section and provide it to ChatGPT. The output
will include the helper module and the refactored Python script using Pydantic for input
validation.

#### Expected Helper Module

```python
# validation_helper.py
from pydantic import BaseModel, ValidationError

class MethodParams(BaseModel):
    param1: int
    param2: str

def validate_method_params(params):
    try:
        validated_params = MethodParams(**params)
        return validated_params
    except ValidationError as e:
        raise ValueError(f"Validation error: {e}")
```

#### Expected Refactored Python Script

```python
from validation_helper import validate_method_params

class SimpleClass:
    def method(self, param1: int, param2: str):
        params = {'param1': param1, 'param2': param2}
        try:
            validated_params = validate_method_params(params)
        except ValueError as e:
            print(f"Validation error: {e}")
            return
        print(f"param1: {validated_params.param1}, param2: {validated_params.param2}")

# Example usage
obj = SimpleClass()
obj.method(1, "example")
```

### Explanation

#### Before Using Pydantic

- **Manual Validation:** The original method manually checks the types
  of `param1` and `param2` using `isinstance`.
- **Error Handling:** Raises a `TypeError` if the types are incorrect.
- **Readability:** The validation logic is mixed with the method's core
  functionality, making the code less readable and harder to maintain.

#### After Using Pydantic with a Helper Module

- **Helper Module:** The validation logic is moved to a separate helper
  module (`validation_helper.py`).
- **Automatic Validation:** The refactored method uses the helper module
  to validate the inputs using Pydantic.
- **Error Handling:** Catches `ValidationError` exceptions and logs the
  validation errors.
- **Readability:** The core functionality of the method is separated
  from the validation logic, making the code cleaner and easier to
  maintain.

### Overview

This guide provides a detailed approach to using Pydantic for input
validation at runtime in Python classes by leveraging a helper module.
It covers the benefits of using Pydantic, a step-by-step example, and an
explanation of the changes before and after using Pydantic.

## Benefits of Using Pydantic

- **Automatic Data Validation:** Pydantic automatically validates data
  types and values at runtime.
- **Clearer Code:** Reduces boilerplate validation code, making the code
  cleaner and more readable.
- **Error Messages:** Provides detailed error messages, which can be
  more informative than manually raised exceptions.
- **Data Parsing:** Parses and transforms data, ensuring that the inputs
  conform to the expected types and formats.

## Best Practices for Using Pydantic

### 1. Helper Module for Pydantic Validation

- **Define Models:** Create Pydantic models in a helper module to
  represent the expected input data structure for each method.
- **Reuse Models:** Reuse Pydantic models across different methods if
  they share similar input structures.

### 2. Validation in Methods

- **Validate Inputs:** Use the helper module to validate inputs at the
  beginning of each method.
- **Refactor Code:** Refactor existing validation code to utilize
  Pydantic models for cleaner and more maintainable code.

### 3. Error Handling

- **Catch Validation Errors:** Catch `ValidationError` exceptions and
  handle them appropriately.
- **Log Errors:** Log validation errors with detailed information to aid
  in debugging and issue resolution.

### 4. Documentation

- **Document Models:** Document the purpose and structure of each
  Pydantic model in the helper module.
- **Explain Validation:** Explain the validation process in the method
  docstrings to provide context to future maintainers.

### 5. Consistency

- **Consistent Validation:** Ensure that all methods in a class follow a
  consistent approach to input validation by using the helper module.
- **Code Quality:** Adhere to clean code principles and maintain high
  code quality by using Pydantic.

## MyPy vs. Pydantic

### MyPy

- **Purpose:** MyPy is a static type checker for Python.
- **Functionality:** It checks the types in your code without running
  it. It verifies that the types match the annotations you've provided
  and that type usage is consistent.
- **Usage:** It helps catch type-related errors during development
  before runtime, ensuring type safety and reducing bugs.

### Pydantic

- **Purpose:** Pydantic is used for runtime data validation and settings
  management using Python type annotations.
- **Functionality:** It validates data at runtime, ensuring that the
  data conforms to the specified types and constraints.
- **Usage:** It is often used in web frameworks like FastAPI to validate
  request data or in applications that require robust data validation
  and settings management.

### Key Differences

- **MyPy:** Checks types statically during development. It doesn't
  affect the runtime performance or the running of the code.
- **Pydantic:** Validates types and data at runtime, raising errors if
  the data does not conform to the expected types.

### Conclusion

Using Pydantic for input validation at runtime simplifies the validation
process, makes the code cleaner, and provides robust error handling. By
following best practices and leveraging a helper module, you can ensure
that your methods receive correctly typed and valid data, reducing
potential runtime errors and improving code maintainability. This
approach, combined with static type checking using MyPy, can
significantly enhance the robustness and reliability of your Python
applications.