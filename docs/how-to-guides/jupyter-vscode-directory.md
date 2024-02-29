# How to Set Up Jupyter Notebooks in VS Code to Use the Correct Start-up Directory

Ensuring that Jupyter notebooks in Visual Studio Code (VS Code) start in
the correct directory is crucial for maintaining a smooth and efficient
workflow, especially when dealing with file paths. This guide will walk
you through configuring VS Code so that Jupyter notebooks always use
your project's root directory as their start-up directory, eliminating
the need to adjust paths frequently.

## Prerequisites

- Ensure you have Visual Studio Code installed.
- Ensure the Jupyter extension for VS Code is installed and enabled.

## Step-by-Step Guide

1. **Open VS Code Settings in JSON Format**

   - Open VS Code.
   - Access the Command Palette by pressing `Ctrl+Shift+P` on
     Windows/Linux or `Cmd+Shift+P` on macOS.
   - Type `Open Settings (JSON)` and select the option that appears to
     open your settings file in JSON format.

2. **Configure the Start-up Directory**

   - In the `settings.json` file, look for the
     `jupyter.notebookFileRoot` setting. If it's not present, you'll
     need to add it.
   - Insert or modify the line as follows:

     ```json
     "jupyter.notebookFileRoot": "${workspaceFolder}",
     ```

   This setting instructs VS Code to use the workspace folder (the
   project root directory) as the default directory for Jupyter
   notebooks. The workspace folder is determined by the location of your
   `.code-workspace` file or the primary folder you have opened in VS
   Code.

3. **Save the Changes**

   - After adding or modifying the line, save the `settings.json` file.
   - Close and reopen any active Jupyter notebooks for the changes to
     take effect.

## Conclusion

By following these steps, you have successfully configured Visual Studio
Code to set the project's root directory as the default start-up
directory for Jupyter notebooks. This configuration streamlines your
workflow by removing the need to frequently adjust paths within your
notebooks. Now, you can focus more on your data analysis or development
tasks without the hassle of directory-related issues.