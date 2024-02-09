# Data Conversion Workflow for NLP Projects

## Overview

This document outlines the process and provides the necessary Python
functions for converting data files between XLSX and CSV formats within
a Natural Language Processing (NLP) project. The workflow is designed to
facilitate seamless data sharing and manipulation among non-technical
stakeholders and machine learning (ML) experts, ensuring uniform
encoding and formatting across different operating systems.

## Procedure

### Context

Non-technical stakeholders often manually create and share data in XLSX
format using Windows OS, without employing programming tools like
Python. ML experts, on the other hand, utilize containers running Linux
to manipulate this data with Python and incorporate it into the
project's codebase. To ensure compatibility and uniformity in data
handling, two Python functions have been developed for converting data
files between XLSX and CSV formats.

!!! note
    This Guide works even if the developer uses Mac or Windows
    without Docker.

### Conversion from XLSX to CSV

When ML experts receive an XLSX file from business stakeholders, the
following Python function should be executed in a Linux-based container
to convert the file into a CSV format. This conversion ensures the data
is encoded in UTF-8 and retains consistent formatting for use in the
project's NLP codebase.

#### Function: `convert_xlsx_to_csv`

```python
def convert_xlsx_to_csv(xlsx_path, csv_path, sheet_name=0):
    """
    Converts an XLSX file to a CSV file with UTF-8 encoding.

    This function takes the path to an XLSX file and a destination path
    for the CSV file as arguments. It optionally accepts the name or
    index of the sheet to convert. It uses `pandas` to read the
    specified sheet, ensuring all data is treated as strings
    (`dtype=str`) to preserve formatting. It then fills any missing
    values with empty strings to avoid the string 'nan' appearing in
    your CSV. Finally, it writes the data to a CSV file, specifying
    UTF-8 encoding and using `\n` as the line terminator to ensure
    compatibility across different operating systems.

    Parameters: - xlsx_path: Path to the source XLSX file.  - csv_path:
    Path where the output CSV file should be saved.  - sheet_name: Name
    or index of the sheet in the XLSX file to convert.
                  Defaults to the first sheet.
    """
    try:
        # Load the specified sheet from the XLSX file
        data = pd.read_excel(xlsx_path, sheet_name=sheet_name, dtype=str)

        # Convert any NaN values to empty strings to avoid 'nan' in the CSV
        data.fillna("", inplace=True)

        # Save the DataFrame to a CSV file with UTF-8 encoding
        data.to_csv(
            csv_path, encoding="utf-8", index=False, lineterminator="\n"
        )

        print(
            f"Successfully converted {xlsx_path} to {csv_path} in UTF-8 encoding."
        )
    except Exception as e:
        print(f"Error converting {xlsx_path} to CSV: {e}")
```

**Parameters:**

- `xlsx_path`: The file path to the source XLSX file.
- `csv_path`: The file path where the output CSV file will be saved.
- `sheet_name`: (Optional) The name or index of the sheet in the XLSX
  file to be converted.

**Usage:**

```python
convert_xlsx_to_csv('path/to/input.xlsx', 'path/to/output.csv')
```

### Conversion from CSV to XLSX

For sharing processed data back with non-technical stakeholders, ML
experts can convert the CSV files (previously created or manipulated
within the Linux containers) back into XLSX format. This conversion
facilitates easy access and interpretation of the results by business
users.

#### Function: `convert_csv_to_xlsx`

```python
import pandas as pd


def convert_csv_to_xlsx(csv_path, xlsx_path):
    """
    Converts a CSV file to an XLSX file.

    This function takes the path to a CSV file and the desired output
    path for the XLSX file. It uses `pandas` to read the CSV file,
    assuming it is encoded in UTF-8 (as ensured by the CSV creation
    function). Then, it writes the data to an XLSX file using the
    `openpyxl` engine, which is required for writing to XLSX format and
    needs to be installed alongside `pandas` if it's not already present
    in your environment.

    Parameters:
    - csv_path: Path to the source CSV file.
    - xlsx_path: Path where the output XLSX file should be saved.
    """
    try:
        # Load the CSV file, assuming UTF-8 encoding
        data = pd.read_csv(csv_path, encoding="utf-8")

        # Save the DataFrame to an XLSX file
        with pd.ExcelWriter(xlsx_path, engine="openpyxl") as writer:
            data.to_excel(writer, index=False)

        print(f"Successfully converted {csv_path} to {xlsx_path}.")
    except Exception as e:
        print(f"Error converting {csv_path} to XLSX: {e}")
```

**Parameters:**

- `csv_path`: The file path to the source CSV file.
- `xlsx_path`: The file path where the output XLSX file will be saved.

**Usage:**

```python
convert_csv_to_xlsx('path/to/input.csv', 'path/to/output.xlsx')
```

## Requirements

- Python 3.x
- Pandas library
- Openpyxl library (for XLSX file writing)

## Installation

Ensure the required libraries are installed in your Linux container:

```bash
pip install pandas openpyxl
```

## Conclusion

This procedure guide facilitates a smooth data exchange and processing
workflow for NLP projects, bridging the gap between non-technical
stakeholders and ML experts. By following the documented steps and
utilizing the provided Python functions, teams can ensure data
consistency, compatibility, and efficiency throughout the project
lifecycle.