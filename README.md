[![Python application](https://github.com/matan1008/parameter-decorators/workflows/Python%20application/badge.svg)](https://github.com/doronz88/pymobiledevice3/actions/workflows/python-app.yml "Python application action")
[![Pypi version](https://img.shields.io/pypi/v/parameter-decorators.svg)](https://pypi.org/project/parameter-decorators/ "PyPi package")
[![Downloads](https://static.pepy.tech/personalized-badge/parameter-decorators?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/parameter-decorators)
[![codecov](https://codecov.io/gh/matan1008/parameter-decorators/branch/master/graph/badge.svg?token=GL0FZD9SVG)](https://codecov.io/gh/matan1008/parameter-decorators)

# parameter-decorators

Handy decorators for converting parameters

# Installation

Install the last released version using `pip`:

```shell
python3 -m pip install -U parameter-decorators
```

Or install the latest version from sources:

```shell
git clone git@github.com:matan1008/parameter-decorators.git
cd parameter-decorators
python3 -m pip install -U -e .
```

# Usage

The package contains several handy decorators, lets give an example with `str_to_path`:

```python
from parameter_decorators import str_to_path


@str_to_path('input_file')
def get_parent(input_file):
    return input_file.parent


# Will print "/usr/bin"
print(get_parent('/usr/bin/python'))
```