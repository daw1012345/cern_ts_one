# CERN Technical Student Assignment - Question 1
## Requirements
- Python >= 3.7
    - This is required, as Counter is guaranteed to preserve insertion order in Python >= 3.7 according to the official documentation
- No other dependencies are required (see below for development requirements for linting/testing)

## Installation
- While it is possible to install this package, for a project/assignment this small I recommend running it without installing
- `pip install .`

## Running (No Installation)
`PYTHONPATH=$PWD/src python3 src/tsa_one/cli.py a b c`

## Running (If Installed)
- `tsa_one-cli a b c d a` OR `python3 -m tsa_one a b c d a`


## Contributing and Code Quality
- If you wish to contribute, fork the project and create a PR
- A GitHub workflow will automatically lint and test your code. Requirements:
  - Passes Black lint
  - Passes isort lint
  - Passes flake8 lint
- Tests were not mandated by the exercise description, and therefore their presence is not enforced. They are only provided as a courtesy. 
- **It is recommended that you install the provided pre-commit hooks**

## Manual linting/testing/formatting
First, install all the development dependencies with `pip install '.[dev]'`
- Black: `black .`
- isort: `isort .`
- flake8: `flake8`
- pytest: `pytest --doctest-modules --junitxml=junit/test-results.xml --cov=src --cov-report=xml --cov-report=html`
