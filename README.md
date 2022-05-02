# project euler and runner script
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Python 3.11](https://img.shields.io/badge/python-3.11-green.svg)](https://www.python.org/)

My project euler solutions with a simple script to automate some simple tasks.

### project structure
    .
    ├── inputs              # input files
    ├── problems            # solutions
    ├── utils               # some framework stuff and utils functions
    ├── README.md
    ├── requirements.txt    # pip install from here
    └── runner              # runner executable script

### runner script
```shell
usage: runner [-h] [-s SOLVE] [-e EXPLICIT] [-i INPUT] [-v] [-p PREPARE]
project euler runner

options:
  -h, --help            show this help message and exit
  -s SOLVE, --solve SOLVE
                        problem number
  -e EXPLICIT, --explicit EXPLICIT
                        explicit file to solve
  -i INPUT, --input INPUT
                        input file
  -v, --verbose         print verbose result
  -p PREPARE, --prepare PREPARE
                        problem number
```

