# Reqstool Python Decorators

## Description

This provides decorators and collecting of decorated code, formatting it and writing to yaml file.

## Installation

The package name is `reqstool-decorators`.

* Using pip install:

```
$pip install reqstool-decorators 
```

## Using

### pyproject.toml

* Hatch

```
dependencies = [
    "reqstool-decorators == <version>"
]
```

* Poetry

```
[tool.poetry.dependencies]
reqstool-decorators = "<version>"
```

### Decorators

Import decorators:

```
from reqstool-decorators.decorators.decorators import Requirements, SVCs
```

Example usage of the decorators:

```
@Requirements(REQ_111, REQ_222)
def somefunction():
```

```
@SVCs(SVC_111, SVC_222)
def test_somefunction():
```

### Processor

Import processor:

```
from reqstool.processors.decorator_processor import ProcessDecorator
```

Main function to collect decorators data and generate yaml file:

```
process_decorated_data(path_to_python_files)
```

Here `path_to_python_files` is the directories to search through to find decorated code.

*Note:*

Yaml file is saved into the `/dist` folder, make sure the folder exists before running the `process_decorated_data` function.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
