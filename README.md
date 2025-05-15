# Thoughtful Package Sorter

This Python project implements a reliable and maintainable function to dispatch packages into the correct stacks (`STANDARD`, `SPECIAL`, `REJECTED`) based on their dimensions and mass, as required by Thoughtful’s robotic automation system.

## Features

- Classifies packages as bulky, heavy, or both based on volume and mass.
- Modular architecture for easy maintanance and extensibility.
- Robust error handling for invalid inputs (negative, zero, and non-numeric).
- Comprehensive unit test coverage for edge cases.
- Logging for debugging and monitoring.

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/dastoc/thoughtful-sorter.git
cd thoughtful-sorter
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running Tests

To run the test suite:

```bash
pytest
```

## Execute
Run this command:
```bash
python main.py
```

the result, should be:
```bash
INFO:sorter:Sorting package: width=100, height=100, length=100, mass=10, bulky=True, heavy=False
Package 1: SPECIAL
INFO:sorter:Sorting package: width=200, height=50, length=50, mass=25, bulky=True, heavy=True
Package 2: REJECTED
INFO:sorter:Sorting package: width=150, height=10, length=10, mass=10, bulky=True, heavy=False
Package 3: SPECIAL
```