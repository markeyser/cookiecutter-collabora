# API Reference

This API Reference provides detailed documentation for the modules and
classes within the "{{ cookiecutter.package_name }}" package. This
package is structured as per the "{{ cookiecutter.project_name }}"
generated from the Cookiecutter template, aiming to demonstrate a
well-organized Python project.

## Package Overview

Located in `{{ cookiecutter.package_name }}/__init__.py`, this package
initializes and configures the export of the main application
functionality.

### Package Content

The `{{ cookiecutter.package_name }}` package is designed to encapsulate
the core functionality of '{{ cookiecutter.project_name }}'. It includes
the main Application class that provides the basic framework for the
application operations.

```python

from .app import Application

__all__  = ['Application']
```  

**Modules:**

- `app.py`: Contains the `Application` class that drives the main
  functionality of the project.

## `{{ cookiecutter.package_name }}.app` Module
  
Located in `src/{{ cookiecutter.package_name }}/app.py`, this module
contains the `Application` class which is pivotal to the project's
functionality.

### `Application` Class

::: {{ cookiecutter.package_name }}.app.Application