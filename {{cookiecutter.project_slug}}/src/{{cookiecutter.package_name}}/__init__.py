"""
Package for {{ cookiecutter.project_name }}

This package contains the core functionality for '{{
cookiecutter.project_name }}', which is intended to demonstrate how to
structure a Python project using Cookiecutter templates. This includes a
modular design with an Application class that can be expanded to suit
various needs.

Modules:
    app.py - Contains the Application class that drives the main
    functionality of the project.

How to use the package:
    - Import the Application class from the app module.
    - Create an instance of Application with the required configuration.
    - Call the run method to execute the application.

Example:
    from {{ cookiecutter.package_name }} import Application

    config = {
        'name': '{{ cookiecutter.project_name }}', 'version': '1.0',
        'environment': '{{ cookiecutter.environment_name }}'
    }

    app = Application(config) app.run()

This simple example sets up a basic application instance and runs it,
demonstrating the package's potential structure and usage.

"""

# Import necessary classes or functions from modules
from .app import Application

# Defines what is exported when `from package import *` is used.
__all__ = ['Application']  
