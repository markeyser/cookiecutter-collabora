# Using Configuration Files to Avoid Hardcoding Values

!!! example "ChatGPT Prompt for creating config files"

    ```plaintext
    You are a world-class Python developer with an eagle eye for detail and
    a deep understanding of best practices in detecting and refactoring
    hardcoded values in Python code. I have a Python script, and I want to
    detect and refactor the following issues based on these recommendations:
    
    1. **Parameters and Defaults**: Identify function parameter defaults
       related to configuration settings such as chunk sizes, timeouts, and
       AWS session durations. These should be externalized to a
       configuration file or environment variables.
    2. **File Extensions and Paths**: Detect hardcoded paths and file
       extensions used frequently or subject to change. These should be
       placed in configuration files to avoid having to search through code
       to make changes and to ensure consistency.
    3. **Environment Variables**: Identify hardcoded environment variable
       names and their default values. These should be defined in
       configuration files or environment variables to manage different
       environments (development, testing, production) more effectively.
    4. **Model and Service Configurations**: Look for hardcoded model IDs,
       AWS service regions, and similar configurations. These should be
       externalized for easier deployments across different regions or when
       switching between different models.
    5. **Logger Messages and Formats**: Ensure logger formats are defined in
       a centralized logging configuration. Detect any repetitive or
       template-based log messages that can benefit from configuration or
       templating approaches.
    
    Please produce two files: a configuration file using YAML language and
    the refactored version of the Python code.
    
    Here is the script:
    
    ```python
    [Insert your Python script here]
    ```
    
    ### Example
    
    #### Original Python Script
    
    ```python
    import logging
    import os
    
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    
    def process_data(file_path='/data/input.txt', chunk_size=1024):
        with open(file_path, 'r') as file:
            while chunk := file.read(chunk_size):
                process_chunk(chunk)
    
    def process_chunk(chunk):
        logging.info(f'Processing chunk of size {len(chunk)}')
        # Processing logic here
    
    if __name__ == "__main__":
        process_data()
    ```
    
    #### Using the Prompt
    
    To use the prompt, copy the original Python script into the `[Insert
    your Python script here]` section and provide it to ChatGPT. The output
    will include two files: a configuration file in YAML format and the
    refactored Python script.
    
    #### Expected Configuration File (config.yaml)
    
    ```yaml
    logging:
      level: INFO
      format: '%(asctime)s - %(message)s'
    
    defaults:
      file_path: '/data/input.txt'
      chunk_size: 1024
    ```
    
    #### Expected Refactored Python Script
    
    ```python
    import logging
    import os
    import yaml
    
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    logging.basicConfig(level=getattr(logging, config['logging']['level']), format=config['logging']['format'])
    
    def process_data(file_path=config['defaults']['file_path'], chunk_size=config['defaults']['chunk_size']):
        with open(file_path, 'r') as file:
            while chunk := file.read(chunk_size):
                process_chunk(chunk)
    
    def process_chunk(chunk):
        logging.info(f'Processing chunk of size {len(chunk)}')
        # Processing logic here
    
    if __name__ == "__main__":
        process_data()
    ```

- [Using Configuration Files to Avoid Hardcoding Values](#using-configuration-files-to-avoid-hardcoding-values)
  - [Overview](#overview)
  - [Benefits of Using Configuration Files](#benefits-of-using-configuration-files)
  - [Directory Structure for Configuration](#directory-structure-for-configuration)
    - [Example Directory Structure](#example-directory-structure)
  - [What Should Be Included in Configuration Files](#what-should-be-included-in-configuration-files)
    - [Example Content of a Configuration File](#example-content-of-a-configuration-file)
      - [module1.yaml](#module1yaml)
  - [What Should Be Included in the .env File](#what-should-be-included-in-the-env-file)
    - [Example Content of the .env File](#example-content-of-the-env-file)
    - [Summary](#summary)
  - [Loading Configuration in Code](#loading-configuration-in-code)
    - [Loading YAML Configuration Files](#loading-yaml-configuration-files)
    - [Loading Environment Variables](#loading-environment-variables)
  - [Conclusion](#conclusion)
- [Best Practices for Configuration Files Using YAML](#best-practices-for-configuration-files-using-yaml)
  - [Overview](#overview-1)
  - [Directory Structure](#directory-structure)
    - [Example Directory Structure](#example-directory-structure-1)
  - [Creating Configuration Files](#creating-configuration-files)
    - [Naming Convention](#naming-convention)
    - [Main Configuration File](#main-configuration-file)
    - [Example Content of a Sub-Package Configuration File](#example-content-of-a-sub-package-configuration-file)
    - [YAML File for Each Sub-Package](#yaml-file-for-each-sub-package)
  - [Loading Configuration Files](#loading-configuration-files)
    - [Helper Function to Load YAML Configuration](#helper-function-to-load-yaml-configuration)
    - [Example Usage](#example-usage)
  - [Conclusion](#conclusion-1)
  - [Best Practices for Refactoring Hardcoded Values in Python Code](#best-practices-for-refactoring-hardcoded-values-in-python-code)
    - [Introduction](#introduction)
    - [Best Practices](#best-practices)
    - [Prompt for Automating Refactoring](#prompt-for-automating-refactoring)
    - [Example](#example)
      - [Original Python Script](#original-python-script)
      - [Using the Prompt](#using-the-prompt)
      - [Expected Configuration File (config.yaml)](#expected-configuration-file-configyaml)
      - [Expected Refactored Python Script](#expected-refactored-python-script)
    - [Conclusion](#conclusion-2)


## Overview

This document provides guidelines on how to use configuration files to
avoid hardcoding values in your codebase. It serves as an introduction
to best practices for creating and managing YAML configuration files in
your project. This introduction explains what should be included in
configuration files and what should be stored in the `.env` file.

## Benefits of Using Configuration Files

- **Maintainability**: Centralizes configuration settings, making it
  easier to manage and update without modifying the code.
- **Separation of Concerns**: Differentiates between configuration
  settings and application logic.
- **Security**: Keeps sensitive information, such as API keys and
  passwords, separate from non-sensitive configuration settings.

## Directory Structure for Configuration

Place all non-sensitive configuration settings in a dedicated `config`
directory and use the `.env` file for storing secrets and sensitive
information.

### Example Directory Structure

```
src/
├── __pycache__/
├── module1/
├── module2/
├── module3/
├── main.py
config/
├── module1.yaml
├── config.yaml
├── module2.yaml
├── module3.yaml
└── logging.yaml
.env
```

## What Should Be Included in Configuration Files

Configuration files should include non-sensitive settings that are
required for the application to function. These can be categorized by
module and stored in individual YAML files.

### Example Content of a Configuration File

#### module1.yaml

```yaml
# Configuration for module1

parameter1: value1
parameter2: value2

logging:
  level: INFO
  format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
```

## What Should Be Included in the .env File

The `.env` file should include sensitive information, such as API keys,
secrets, and credentials that should not be exposed in the codebase or
configuration files.

### Example Content of the .env File

```plaintext
# Store of global environment variables. 

API_KEY="your_api_key_here" 
DATABASE_URL="your_database_url_here" 
SECRET_KEY="your_secret_key_here" 
```

### Summary

1. **Configuration Files (YAML)**: Store non-sensitive configuration
   settings related to application logic and modules.
2. **.env File**: Store sensitive information and secrets that should
   not be exposed in the configuration files or codebase.

## Loading Configuration in Code

To load the configuration files and environment variables in your code,
use appropriate libraries and functions.

### Loading YAML Configuration Files

```python
import yaml

def load_config(config_path: str) -> dict:
    """Loads a YAML configuration file.

    Args:
        config_path (str): The path to the YAML configuration file.

    Returns:
        dict: A dictionary containing the configuration data 
              loaded from the YAML file.
    """
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config

# Example usage
module1_config = load_config('config/module1.yaml')
```

### Loading Environment Variables

Use a library such as `python-dotenv` to load environment variables from
the `.env` file:

```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")
```

## Conclusion

By following these guidelines, you can ensure that your project’s
configuration files are well-organized, maintainable, and secure. This
approach enhances the readability and manageability of your codebase,
making it easier to implement and modify configurations as your project
evolves. Keep sensitive information in the `.env` file and other
configuration settings in the respective YAML files within the `config`
directory. For detailed best practices, refer to the main technical
documentation on best practices for configuration files using YAML.

# Best Practices for Configuration Files Using YAML

## Overview

This document provides a comprehensive guide on how to organize and
manage configuration files for your project using YAML. It aims to
ensure consistency, maintainability, and ease of use across different
sub-packages of your codebase.

## Directory Structure

To maintain a well-organized project, place all configuration files in a
dedicated `config` directory. Each sub-package should have its own YAML
configuration file named after the sub-package for clarity and ease of
identification. Additionally, include a main `config.yaml` file for
global configurations.

### Example Directory Structure

```
src/
└── fpservicesagemodel/
    ├── __pycache__/
    ├── chunking/
    ├── conversations/
    ├── data/
    ├── data_preprocessing/
    ├── embeddings/
    ├── evaluation/
    ├── generators/
    ├── llms/
    ├── retrievers/
    ├── utils/
    └── vectorization/
        ├── app.py
        ├── main.py
        └── service_sage.py
config/
├── chunking.yaml
├── config.yaml
├── conversations.yaml
├── data.yaml
├── data_preprocessing.yaml
├── embeddings.yaml
├── evaluation.yaml
├── generators.yaml
├── llms.yaml
├── retrievers.yaml
├── utils.yaml
└── vectorization.yaml
```

## Creating Configuration Files

### Naming Convention

Use clear and meaningful names for the configuration files that reflect
the sub-package they belong to. Avoid redundant suffixes like `_config`
since the files are already placed within a `config` directory.

### Main Configuration File

The main `config.yaml` file can be used to store global settings or to
reference other configuration files.

```yaml
# Main configuration file

global_settings:
  logging_level: INFO
  default_region: us-east-1

includes:
  - chunking.yaml
  - conversations.yaml
  - data.yaml
  - data_preprocessing.yaml
  - embeddings.yaml
  - evaluation.yaml
  - generators.yaml
  - llms.yaml
  - retrievers.yaml
  - utils.yaml
  - vectorization.yaml
```

### Example Content of a Sub-Package Configuration File

Here’s an example of what the `vectorization.yaml` file might look like:

```yaml
# Configuration for vectorization module

models:
  all-mini-lm:
    dimension: 384
  titan:
    dimension: 1536

indexing:
  knn:
    ef_search: 100
    ef_construction: 256
    m: 48

logging:
  level: INFO
  format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
```

### YAML File for Each Sub-Package

1. **chunking.yaml**

    ```yaml
    # Configuration for chunking module

    chunk_size: 1000
    overlap: 100

    logging:
      level: INFO
      format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ```

2. **conversations.yaml**

    ```yaml
    # Configuration for conversations module

    conversation_timeout: 300
    max_conversations: 5

    logging:
      level: INFO
      format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ```

3. **data.yaml**

    ```yaml
    # Configuration for data module

    data_source: 's3://bucket-name/data'
    batch_size: 100

    logging:
      level: INFO
      format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ```

(Continue similarly for other sub-packages)

## Loading Configuration Files

To load the configuration files in your code, use a helper function.
This ensures that the configuration data is easily accessible and can be
utilized across different parts of your project.

### Helper Function to Load YAML Configuration

```python
import yaml

def load_config(config_path: str) -> dict:
    """Loads a YAML configuration file.

    This function reads a YAML file from the specified path and 
    loads its contents into a dictionary. The configuration file 
    is expected to contain model-specific settings such as 
    embedding dimensions.

    Args:
        config_path (str): The path to the YAML configuration file.

    Returns:
        dict: A dictionary containing the configuration data 
              loaded from the YAML file.
    """
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config
```

### Example Usage

Load the configuration file in your code where necessary. For instance,
in the `main` function of the `vectorization` sub-package:

```python
import os
from typing import List

def main() -> None:
    config_path = "config/vectorization.yaml"
    config = load_config(config_path)

    model_name = "titan"  # This could be dynamically set
    dimension = config["models"].get(model_name, {}).get("dimension")

    handler = OpenSearchIngestor(
        endpoint=os.getenv("ENDPOINT") or "",
        region="us-east-1",
        index_name="servicesage-baseline",
        service="aoss",
        metadata_mappings={},
        dimension=dimension
    )

    # Placeholder for embedded_chunks. Replace with actual data in the future.
    embedded_chunks: List[Chunk] = []  # or define some mock data for testing

    handler.create_index(model_name, handler.dimension)
    handler.ingest_chunks(embedded_chunks)

if __name__ == "__main__":
    main()
```

## Conclusion

By following these best practices, you can ensure that your project’s
configuration files are well-organized, maintainable, and easily
accessible. This approach enhances the readability and manageability of
your codebase, making it easier to implement and modify configurations
as your project evolves.

## Best Practices for Refactoring Hardcoded Values in Python Code

### Introduction

Refactoring code to externalize hardcoded values is a crucial step in
improving the maintainability, flexibility, and scalability of software.
This document explains the rationale behind five best practices for
refactoring hardcoded values in Python code, provides a prompt for
automating the detection and refactoring process, and demonstrates a
basic example of how to use the prompt with a simple Python script.

### Best Practices

1. **Parameters and Defaults**:
   - **Reason**: Hardcoding function parameter defaults, especially
     those related to configuration settings such as chunk sizes,
     timeouts, and AWS session durations, limits flexibility.
     Externalizing these parameters to configuration files or
     environment variables allows for easier modifications and better
     adaptability to different environments.
   - **Example**: Instead of setting a timeout of 30 seconds directly in
     the function definition, it should be read from a configuration
     file or environment variable.

2. **File Extensions and Paths**:
   - **Reason**: Hardcoded paths and file extensions make the code less
     flexible and more difficult to maintain. Placing these values in
     configuration files ensures consistency and makes updates easier
     without searching through the codebase.
   - **Example**: Hardcoded paths like `/data/files` should be stored in
     a configuration file to facilitate changes across environments
     (development, testing, production).

3. **Environment Variables**:
   - **Reason**: Hardcoding environment variable names and their default
     values makes it challenging to manage different environments
     effectively. Defining these values in configuration files or
     environment variables enhances flexibility and maintainability.
   - **Example**: Instead of using `os.getenv('DB_HOST', 'localhost')`
     directly in the code, the default value `localhost` should be
     defined in a configuration file.

4. **Model and Service Configurations**:
   - **Reason**: Hardcoding model IDs, AWS service regions, and similar
     configurations hampers the ability to deploy across different
     regions or switch between models. Externalizing these
     configurations simplifies deployments and model management.
   - **Example**: Instead of specifying `region='us-west-2'` directly in
     the code, the region should be read from a configuration file.

5. **Logger Messages and Formats**:
   - **Reason**: Centralizing logger formats and repetitive log messages
     in a configuration or templating approach improves consistency and
     maintainability. It also allows for easy updates to logging formats
     across the application.
   - **Example**: Logger formats like `%(asctime)s - %(name)s -
     %(levelname)s - %(message)s` should be defined in a centralized
     logging configuration file.

### Prompt for Automating Refactoring

```plaintext
You are a world-class Python developer with an eagle eye for detail and
a deep understanding of best practices in detecting and refactoring
hardcoded values in Python code. I have a Python script, and I want to
detect and refactor the following issues based on these recommendations:

1. **Parameters and Defaults**: Identify function parameter defaults
   related to configuration settings such as chunk sizes, timeouts, and
   AWS session durations. These should be externalized to a
   configuration file or environment variables.
2. **File Extensions and Paths**: Detect hardcoded paths and file
   extensions used frequently or subject to change. These should be
   placed in configuration files to avoid having to search through code
   to make changes and to ensure consistency.
3. **Environment Variables**: Identify hardcoded environment variable
   names and their default values. These should be defined in
   configuration files or environment variables to manage different
   environments (development, testing, production) more effectively.
4. **Model and Service Configurations**: Look for hardcoded model IDs,
   AWS service regions, and similar configurations. These should be
   externalized for easier deployments across different regions or when
   switching between different models.
5. **Logger Messages and Formats**: Ensure logger formats are defined in
   a centralized logging configuration. Detect any repetitive or
   template-based log messages that can benefit from configuration or
   templating approaches.

Please produce two files: a configuration file using YAML language and
the refactored version of the Python code.

Here is the script:

```python
[Insert your Python script here]
```

### Example

#### Original Python Script

```python
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def process_data(file_path='/data/input.txt', chunk_size=1024):
    with open(file_path, 'r') as file:
        while chunk := file.read(chunk_size):
            process_chunk(chunk)

def process_chunk(chunk):
    logging.info(f'Processing chunk of size {len(chunk)}')
    # Processing logic here

if __name__ == "__main__":
    process_data()
```

#### Using the Prompt

To use the prompt, copy the original Python script into the `[Insert
your Python script here]` section and provide it to ChatGPT. The output
will include two files: a configuration file in YAML format and the
refactored Python script.

#### Expected Configuration File (config.yaml)

```yaml
logging:
  level: INFO
  format: '%(asctime)s - %(message)s'

defaults:
  file_path: '/data/input.txt'
  chunk_size: 1024
```

#### Expected Refactored Python Script

```python
import logging
import os
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

logging.basicConfig(level=getattr(logging, config['logging']['level']), format=config['logging']['format'])

def process_data(file_path=config['defaults']['file_path'], chunk_size=config['defaults']['chunk_size']):
    with open(file_path, 'r') as file:
        while chunk := file.read(chunk_size):
            process_chunk(chunk)

def process_chunk(chunk):
    logging.info(f'Processing chunk of size {len(chunk)}')
    # Processing logic here

if __name__ == "__main__":
    process_data()
```

### Conclusion

By following these best practices and using the provided prompt, you can
significantly enhance the maintainability, flexibility, and scalability
of your Python code. The example demonstrates how to refactor a simple
script to externalize hardcoded values into a configuration file, making
the code easier to manage and adapt to different environments.