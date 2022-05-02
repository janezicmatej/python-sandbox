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
    ├── euler               # executable script
    └── requirements.txt    # pip install from here

### Script
```
usage: euler [-h] [-s SOLVE] [-i INPUT] [-v] [-p PREPARE]

project euler runner

options:
  -h, --help            show this help message and exit
  -s SOLVE, --solve SOLVE
                        solve problem with given number
  -i INPUT, --input INPUT
                        input file
  -v, --verbose         print verbose result
  -p PREPARE, --prepare PREPARE
                        prepare file for given problem number
```
### Todo
- [ ] modify prepare script