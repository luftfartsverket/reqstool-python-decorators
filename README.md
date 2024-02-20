
[![Commit Activity](https://img.shields.io/github/commit-activity/m/Luftfartsverket/reqstool-python-decorators?label=commits&style=for-the-badge)](https://github.com/Luftfartsverket/reqstool-python-decorators/pulse)
[![GitHub Issues](https://img.shields.io/github/issues/Luftfartsverket/reqstool-python-decorators?style=for-the-badge&logo=github)](https://github.com/Luftfartsverket/reqstool-python-decorators/issues)
[![License](https://img.shields.io/github/license/Luftfartsverket/reqstool-python-decorators?style=for-the-badge&logo=opensourceinitiative)](https://opensource.org/license/mit/)
[![Build](https://img.shields.io/github/actions/workflow/status/Luftfartsverket/reqstool-python-decorators/build.yml?style=for-the-badge&logo=github)](https://github.com/Luftfartsverket/reqstool-python-decorators/actions/workflows/build.yml)
[![Static Badge](https://img.shields.io/badge/Documentation-blue?style=for-the-badge&link=docs)](https://luftfartsverket.github.io/reqstool-python-decorators/reqstool-python-decorators/0.0.1/index.html)

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
