# Project euler and runner script
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Python 3.11](https://img.shields.io/badge/python-3.11-green.svg)](https://www.python.org/)
---
My project euler solutions with a simple script to automate some tasks.

### Project structure
    .
    ├── fwk                 # framework
    ├── inputs              # input files
    ├── problems            # solutions
    ├── utils               # utils functions
    ├── README.md
    ├── euler.py            # executable script
    └── requirements.txt    # pip install from here

### Command Line Interface
```
usage: euler.py [-h] [--debug] {solve,prepare,open} ...

project euler cli

positional arguments:
  {solve,prepare,open}
    solve               solve problem
    prepare             prepare solution file
    open                open problem page

options:
  -h, --help            show this help message and exit
  --debug               print debug info

command 'solve'
usage: euler.py solve [-h] [-v] [-o] [-c] n

positional arguments:
  n              solve problem with given problem

options:
  -h, --help     show this help message and exit
  -v, --verbose  print verbose result
  -o, --open     open problem page
  -c, --copy     copy solution to clipboard

command 'prepare'
usage: euler.py prepare [-h] [-f] n

positional arguments:
  n            prepare file with given problem

options:
  -h, --help   show this help message and exit
  -f, --force  override solution file

command 'open'
usage: euler.py open [-h] n

positional arguments:
  n           open page with given problem

options:
  -h, --help  show this help message and exit


```