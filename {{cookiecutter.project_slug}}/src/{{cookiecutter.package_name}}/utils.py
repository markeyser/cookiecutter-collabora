"""Utils module.

This module provides utility functions for the acroexpandpackage
project, focusing on metadata generation for various file types and
extracting terms from Python libraries.

Functions:
----------
- extract_terms_from_dependencies():
    Extracts terms from the Python libraries specified in the
    pyproject.toml file. Reads the dependencies and dev-dependencies
    from the pyproject.toml file, imports each library, and extracts
    terms (e.g., function names, class names) from them. The extracted
    terms are then saved to a file in the .vscode/dictionaries
    directory.

- generate_metadata(csv_file_path):
    Generates metadata for a given CSV file, detailing its structure and
    contents such as number of rows, columns, and types. The metadata is
    saved as a JSON file with a similar name as the input CSV file.

- generate_metadata_for_json(json_file_path):
    Similar to generate_metadata, but for JSON files. It processes a
    JSON file containing an array of objects and produces a
    corresponding metadata file outlining the structure and contents of
    the JSON data.

Notes
-----
- The module suppresses warnings and silently skips libraries that fail
  to import.
- Ensure the pyproject.toml file is correctly formatted and located in
  the expected directory.
- The functions for metadata generation assume that the files (CSV and
  JSON) are properly formatted and contain the expected data structures.

Author:
-------
Marcos Aguilera Keyser <marcosak@gmail.com>

"""

import importlib
import json
import os
import warnings
from datetime import datetime

import pandas as pd
import toml


def extract_terms_from_dependencies():
    """Extract dependencies.

    Extract terms from the Python libraries specified in the
    pyproject.toml file to produce a custom dictionary for the VS Code
    extension Code Spell Checker.

    This function reads the dependencies and dev-dependencies from the
    pyproject.toml file, imports each library, and extracts terms (e.g.,
    function names, class names) from them.  The extracted terms are
    then saved to a file in the .vscode/dictionaries directory.

    Notes
    -----
    The function suppresses warnings and silently skips libraries that
    fail to import.

    Returns
    -------
    None
    """
    # Suppress any warnings that might arise during execution
    warnings.filterwarnings("ignore")

    # Determine the path to the pyproject.toml file in the current
    # working directory
    pyproject_path = os.path.join(  # noqa: PTH118
        os.getcwd(),  # noqa: PTH109
        "pyproject.toml",
    )

    # Open and read the pyproject.toml file
    with open(pyproject_path, "r") as f:  # noqa: PTH123, UP015
        # Parse the TOML file and store its content as a dictionary
        pyproject_data = toml.load(f)

    # Extract the names of the regular dependencies from the parsed TOML data
    dependencies = list(
        pyproject_data["tool"]["poetry"]["dependencies"].keys(),
    )

    # Extract the names of the development dependencies from the parsed
    # TOML data
    dev_dependencies = list(
        pyproject_data["tool"]["poetry"]["dev-dependencies"].keys(),
    )

    # Remove the 'python' entry from the list of dependencies, if it exists
    if "python" in dependencies:
        dependencies.remove("python")

    # Combine the lists of regular and development dependencies
    libraries_names = dependencies + dev_dependencies

    # Initialize an empty list to store imported libraries
    libraries = []

    # Iterate over each library name to import it
    for name in libraries_names:
        try:
            # Attempt to import the library using its name
            lib = importlib.import_module(name)
            # If successful, add the library to the list
            libraries.append(lib)
        except:  # noqa: PERF203, E722, S110
            # If the import fails, skip to the next library without
            # raising an error
            pass

    # Determine the path to the output file where terms will be saved
    output_path = os.path.join(  # noqa: PTH118
        os.getcwd(),  # noqa: PTH109
        ".vscode",
        "dictionaries",
        "data-science-en.txt",
    )

    # Open the output file in write mode
    with open(output_path, "w") as f:  # noqa: PTH123
        # Iterate over each imported library to extract its terms
        for library in libraries:
            # Get a list of all attributes and methods of the library
            all_library_contents = dir(library)
            # Initialize an empty list to store new contents
            new_contents = []

            # Iterate over each item in the library's contents
            for item in all_library_contents:
                try:
                    # Check if the item is a class or type
                    if isinstance(getattr(library, item), type):
                        # Extract methods and attributes of the
                        # class/type that don't start with an underscore
                        methods = [
                            method
                            for method in dir(getattr(library, item))
                            if not method.startswith("_")
                        ]
                        # Add the extracted methods to the new contents list
                        new_contents.extend(methods)
                except AttributeError:  # noqa: PERF203
                    # If an AttributeError occurs, skip to the next item
                    continue

            # Combine the original library contents with the new contents
            all_library_contents.extend(new_contents)
            # Remove duplicates by converting the list to a set and back
            # to a list
            all_library_contents = list(set(all_library_contents))
            # Filter out terms that start with an underscore
            all_library_contents = [
                term
                for term in all_library_contents
                if not term.startswith("_")
            ]

            # Write each term to the output file on a new line
            for term in all_library_contents:
                f.write(term + "\n")

    # Print a message indicating where the terms were saved
    print(f"Terms extracted and saved to {output_path}")  # noqa: T201


def generate_metadata(csv_file_path):
    """
    Generate metadata for a CSV file and save it as a JSON file.

    This function reads a CSV file from the given path, extracts the
    necessary information such as file name, creation date, number of
    rows, number of columns, and column details.  It then generates a
    metadata dictionary and saves this as a JSON file with the same base
    name as the CSV file. The metadata includes the CSV file's structure
    and details, which aids in providing context, ensuring
    reproducibility, and offering insights into data quality.

    Parameters
    ----------
    csv_file_path : str
        The file path to the CSV file for which metadata is to be
        generated.

    Returns
    -------
    None

    See Also
    --------
    pandas.read_csv : Read a comma-separated values (csv) file into
    DataFrame.

    Notes
    -----
    The `preprocessing` key in the metadata dictionary is initialized as
    an empty list.  It should be manually populated with preprocessing
    steps, or you can modify the function to record preprocessing steps
    programmatically if they are consistently applied in the data
    pipeline.

    The function assumes the pandas library is installed in the Python
    environment.  The source of data and additional notes are specified
    as placeholders and should be provided explicitly.

    The generated metadata JSON file will have the same name as the CSV
    file, suffixed with '_metadata.json'.

    Example
    -------
    >>> generate_metadata('path/to/your/sales_data.csv')
    This will create a JSON file named 'sales_data_metadata.json' with 
    the metadata information in the same directory as 'sales_data.csv'.
    
    """
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Extracting information
    file_name = csv_file_path.split("/")[-1]
    creation_date = datetime.now().strftime("%Y-%m-%d")
    number_of_rows = df.shape[0]
    number_of_columns = df.shape[1]
    columns = [{"name": col, "type": str(df[col].dtype)} for col in df.columns]

    # Metadata dictionary
    metadata = {
        "file_name": file_name,
        "creation_date": creation_date,
        "source": "Specify the data source",
        "number_of_rows": number_of_rows,
        "number_of_columns": number_of_columns,
        "columns": columns,
        # Add any preprocessing steps manually or through code
        "preprocessing": [],  
        "notes": "Add any additional notes here",
    }

    # Saving metadata to a JSON file
    with open(file_name.replace(".csv", "_metadata.json"), "w") as json_file:
        json.dump(metadata, json_file, indent=4)




def generate_metadata_for_json(json_file_path):
    """
    Generate metadata for a JSON file and save it as a separate JSON
    file.

    This function reads a JSON file from the given path, extracts the
    necessary information such as file name, creation date, number of
    records, and details of the data fields.  It then generates a
    metadata dictionary and saves this as a JSON file with a similar
    name as the original JSON file but with '_metadata.json' as a
    suffix. The metadata includes details of the JSON file's structure
    and content, providing context and aiding in reproducibility and
    data quality assessment.

    Parameters
    ----------
    json_file_path : str
        The file path to the JSON file for which metadata is to be
        generated.

    Returns
    -------
    None

    Notes
    -----
    The source of the data and additional notes are provided as
    placeholders in the generated metadata and should be filled in with
    actual details relevant to the JSON file being processed.

    This function assumes that the JSON file contains an array of
    objects, with each object representing a record akin to a row in a
    CSV.

    Example
    -------
    >>> generate_metadata_for_json('path/to/your/data.json')
    This will create a JSON file named 'data_metadata.json' with the metadata
    information in the same directory as 'data.json'.

    """
    # Read the JSON file
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    # Assuming the JSON file is an array of dictionaries
    if not isinstance(data, list) or not all(
        isinstance(item, dict) for item in data
    ):
        raise ValueError(
            "JSON file format is not supported. Expected an array of objects."
        )

    # Extracting information
    file_name = json_file_path.split("/")[-1]
    creation_date = datetime.now().strftime("%Y-%m-%d")
    number_of_records = len(data)
    columns_info = (
        [
            {
                "name": key,
                "type": type(value).__name__,
                "description": "Description of {}".format(key),
            }
            for key, value in data[0].items()
        ]
        if data
        else []
    )

    # Metadata dictionary
    metadata = {
        "file_name": file_name,
        "creation_date": creation_date,
        "source": "Specify the data source",
        "number_of_records": number_of_records,
        "columns": columns_info,
        # Add any preprocessing steps manually or through code
        "preprocessing": [], 
        "notes": "Add any additional notes here",
    }

    # Saving metadata to a JSON file
    metadata_file_path = json_file_path.replace(".json", "_metadata.json")
    with open(metadata_file_path, "w") as json_file:
        json.dump(metadata, json_file, indent=4)


if __name__ == "__main__":
    extract_terms_from_dependencies()
