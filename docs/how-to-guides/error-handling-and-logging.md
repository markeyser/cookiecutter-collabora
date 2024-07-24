# Adding Error Handling and Logging to Your Python Code

!!! example "ChatGPT Prompt for adding error handling and logging"

    ```plaintext
    You are a world-class Python developer with an eagle eye for detail and
    a deep understanding of best practices in error handling and logging in
    Python code. I have a Python script, and I want to add error handling and
    logging based on these recommendations:
    
    1. Error Handling: Identify potential points of failure in the code and
       add appropriate try-except blocks to handle exceptions. Ensure that
       the error messages provide clear and actionable information.
    2. Logging Configuration: Set up a logging configuration that outputs
       logs to a `.log` file located in a `log` folder at the root of the project
       directory. The logging should include error level and above messages
       with timestamps and detailed error descriptions.
    3. Exception Logging: Ensure that exceptions are logged with detailed
       information about the error, including the stack trace.
    4. Custom Error Messages: Provide custom error messages that give a
       clear explanation of the error and suggest possible fixes.
    5. File and Directory Setup: Create a `log` directory in the root of the
       project if it does not exist, and configure the logging output to a file
       within this directory.
    
    Please produce a refactored version of the Python code with the necessary 
    error handling and logging.
    
    Here is the script:
    
    ```python
    [Insert your Python script here]
    ```

### Example

#### Original Python Script (Without Error Handling and Logging)

```python
def process_data(file_path='/data/input.txt', chunk_size=1024):
    with open(file_path, 'r') as file:
        while chunk := file.read(chunk_size):
            process_chunk(chunk)

def process_chunk(chunk):
    print(f'Processing chunk of size {len(chunk)}')
    # Processing logic here

if __name__ == "__main__":
    process_data()
```

#### Refactored Python Script with Error Handling and Logging

```python
import logging
import os

# Ensure the log directory exists
os.makedirs('log', exist_ok=True)

# Configure logging
logging.basicConfig(filename='log/myfile.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def process_data(file_path: str = '/data/input.txt', chunk_size: int = 1024) -> None:
    try:
        with open(file_path, 'r') as file:
            while chunk := file.read(chunk_size):
                process_chunk(chunk)
    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}. Exception: {e}")
    except Exception as e:
        logging.error(f"An error occurred while processing the file: {e}")

def process_chunk(chunk: str) -> None:
    try:
        logging.info(f'Processing chunk of size {len(chunk)}')
        # Processing logic here
    except Exception as e:
        logging.error(f"An error occurred while processing the chunk: {e}")

if __name__ == "__main__":
    process_data()
```

#### Using the Prompt

To use the prompt, copy the original Python script into the `[Insert
your Python script here]` section and provide it to ChatGPT. The output
will include the refactored Python script with error handling and
logging.

## Overview

This document provides guidelines on how to add error handling and
logging to your Python code. It serves as an introduction to best
practices for improving the robustness and maintainability of your code
through proper error handling and logging mechanisms.

!!! note This guide explains the importance of error handling and
    logging, provides a prompt for refactoring code, and demonstrates
    how to add error handling and logging to a Python script.

## Importance of Error Handling and Logging

- **Error Handling**: Proper error handling ensures that your code can
  gracefully handle unexpected situations without crashing. It provides
  clear and actionable error messages to help diagnose and fix issues.
- **Logging**: Logging is essential for tracking the execution of your
  code, identifying issues, and understanding the sequence of events
  leading to errors. It is crucial for debugging, monitoring, and
  maintaining your applications.

## Benefits of Adding Error Handling and Logging

- **Improved Reliability**: Code with proper error handling is more
  reliable and less likely to fail unexpectedly.
- **Easier Debugging**: Detailed error logs make it easier to understand
  what went wrong and how to fix it.
- **Better Monitoring**: Logging provides insights into the
  application's behavior and performance, helping with monitoring and
  maintenance.
- **Enhanced User Experience**: Graceful error handling ensures that
  users receive clear and helpful error messages, improving their
  experience.

## Directory Structure for Logging

!!! info Ensure that you create a `log` directory in the root of your
    project to store log files.

### Example Directory Structure

```plaintext
src/
├── __pycache__/
├── module1/
├── module2/
├── module3/
├── main.py
log/
└── myfile.log
```

## Adding Error Handling and Logging

To add error handling and logging to your Python code, follow these
steps:

1. **Identify Points of Failure**: Review your code to identify where
   errors might occur, such as file operations, network requests, or
   data processing.
2. **Add Try-Except Blocks**: Wrap potentially error-prone code in
   try-except blocks to handle exceptions gracefully.
3. **Set Up Logging**: Configure logging to output to a `.log` file in
   the `log` directory. Use appropriate logging levels (e.g., ERROR,
   INFO) and include timestamps and detailed error descriptions.
4. **Log Exceptions**: Ensure that exceptions are logged with detailed
   information, including the stack trace.
5. **Provide Custom Error Messages**: Customize error messages to
   provide clear explanations and possible fixes for errors.

## Example Code

### Original Code (Without Error Handling and Logging)

```python
def process_data(file_path='/data/input.txt', chunk_size=1024):
    with open(file_path, 'r') as file:
        while chunk := file.read(chunk_size):
            process_chunk(chunk)

def process_chunk(chunk):
    print(f'Processing chunk of size {len(chunk)}')
    # Processing logic here

if __name__ == "__main__":
    process_data()
```

### Refactored Code (With Error Handling and Logging)

```python
import logging
import os

# Ensure the log directory exists
os.makedirs('log', exist_ok=True)

# Configure logging
logging.basicConfig(filename='log/myfile.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def process_data(file_path: str = '/data/input.txt', chunk_size: int = 1024) -> None:
    try:
        with open(file_path, 'r') as file:
            while chunk := file.read(chunk_size):
                process_chunk(chunk)
    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}. Exception: {e}")
    except Exception as e:
        logging.error(f"An error occurred while processing the file: {e}")

def process_chunk(chunk: str) -> None:
    try:
        logging.info(f'Processing chunk of size {len(chunk)}')
        # Processing logic here
    except Exception as e:
        logging.error(f"An error occurred while processing the chunk: {e}")

if __name__ == "__main__":
    process_data()
```

## Conclusion

By following these guidelines, you can ensure that your Python code is
more robust and maintainable through proper error handling and logging.
This approach enhances the reliability, debuggability, and monitoring of
your applications, making it easier to identify and fix issues as they
arise.

## Best Practices for Error Handling and Logging

### Introduction

Proper error handling and logging are critical components of software
development that improve the maintainability, flexibility, and
scalability of your applications. This document explains the rationale
behind best practices for error handling and logging in Python code,
provides a prompt for automating the refactoring process, and
demonstrates a basic example of how to use the prompt with a simple
Python script.

### Best Practices

1. **Error Handling**:
   - **Reason**: Adding try-except blocks around potentially error-prone
     code ensures that the application can handle unexpected situations
     gracefully.
   - **Example**: Wrapping file operations in try-except blocks to catch
     and handle `FileNotFoundError` exceptions.

2. **Logging Configuration**:
   - **Reason**: Configuring logging to output to a file with detailed
     information, including timestamps and error descriptions, helps
     with debugging and monitoring.
   - **Example**: Setting up a logging configuration that outputs error
     level and above messages to a `myfile.log` file in the `log`
     directory.

3. **Exception Logging**:
   - **Reason**: Logging exceptions with detailed information, including
     stack traces, provides insights into the root cause of errors.
   - **Example**: Using `logging.error()` to log exceptions with stack
     traces.

4. **Custom Error Messages**:
   - **Reason**: Providing custom error messages helps users understand
     the nature of the error and possible fixes.
   - **Example**: Logging custom error messages that explain the error
     and suggest potential solutions.

5. **File and Directory Setup**:
   - **Reason**: Ensuring that the necessary directories for logging
     exist before configuring logging helps avoid runtime errors.
   - **Example**: Using `os.makedirs()` to create the `log` directory if
     it does not exist.
