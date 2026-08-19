# pybind-tutorial

A minimal example of wrapping C++ functions for Python using
[pybind11](https://pybind11.readthedocs.io/), and benchmarking the result
against pure Python.

## What's here

- `mymath.cpp` — a small C++ extension module (`mymath`) exposing:
  - `add(a, b)` — adds two integers
  - `sum_squares(n)` — sums i² for i in 0..n-1 (matches the pure-Python
    version in `main.py` exactly)
- `main.py` — times a pure-Python `sum_squares` loop against the C++
  `mymath.sum_squares` and prints the speedup.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)
- A C++ compiler (e.g. `g++` or `clang++`) with C++17 support

## Setup

```bash
uv sync
```

## Build the extension module

```bash
c++ -O3 -Wall -shared -std=c++17 -fPIC \
  $(uv run python -m pybind11 --includes) \
  mymath.cpp -o mymath$(uv run python -c "import sysconfig; print(sysconfig.get_config_var('EXT_SUFFIX'))")
```

This produces a `mymath*.so` file in the project root, importable directly
from Python (it's gitignored — rebuild it after cloning).

## Usage

```bash
uv run python -c "import mymath; print(mymath.add(2, 3))"
```

## Run the benchmark

```bash
uv run main.py
```

This compares a pure-Python `sum_squares` loop against the C++
implementation for n = 10,000,000 and prints the timing and speedup.

## Project structure

```
.
├── main.py        # benchmark: pure Python vs. mymath.sum_squares
├── mymath.cpp      # pybind11 extension module source
├── pyproject.toml  # project metadata / dependencies (managed by uv)
└── uv.lock
```
