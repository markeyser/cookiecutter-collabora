#!/bin/bash

# Redirect output to a file
exec > >(tee -a script_output.log) 2>&1

# Assign values from Cookiecutter variables
os_type="{{ cookiecutter.os_type }}"
project_slug="{{ cookiecutter.project_slug }}"
target_directory="{{ cookiecutter._output_dir }}"
# Get the username from the environment
username=$(echo "$USERPROFILE" | awk -F'\\' '{print $NF}')

# Construct the template directory path
template_dir="C:/Users/$username/.cookiecutters/cookiecutter-rag"

# Construct the source filename
source_filename="$template_dir/READMEs/README_${os_type,,}.md"

# Construct the target filename
target_filename="$target_directory/$project_slug/README.md"

# Print the directories and filenames for debugging
echo "Target Directory: $target_directory"
echo "Source Filename: $source_filename"
echo "Target Filename: $target_filename"

# Ensure the target directory exists
mkdir -p "$target_directory"

# Check if the source file exists and is readable
if [[ -r "$source_filename" ]]; then
    # Copy the file content
    dd if="$source_filename" of="$target_filename"
else
    echo "Source file $source_filename not found or not readable"
    exit 1
fi




