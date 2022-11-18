# Advent of Code Solutions


## Introduction
This repo has solutions to the [Advent of Code](https://adventofcode.com/) 
online coding problems. It solves all historical problems and will be updated 
to solve new ones as they are released.

The solutions are written for combined development and execution speed (i.e. 
to minimize the total time from when I start reading the problem to when I have 
submitted the correct answer) and are therefore not up to the highest standards 
of excellence stylistically.


## Project Structure
- `assembly.py` utility for assembly problems
- `common.py` utility for standard imports
- `search.py` utility for search problems
- `timer.py` utility for timing a process
- `web.py` utility for interacting with the website
- `prototype` a directory to copy and rename for a new problem
- `[year]` a year
  - `[day]` a day of december
    - `sln.py` the solution file
    - `inp.txt` the input from the specific problem; optional if the input data is in solution file


## Setup
Set the `AOC_SESSION` environment variable by following the following steps in Chrome
0. Login to [AOC online](https://adventofcode.com/)
0. Right click > Inspect > Application > Cookies > https://adventofcode.com/
0. Copy the value of the session cookie to your environment variable


## Execution
Run a given solution with
```bash
cd ./[year]/[day]
./sln.py
```


## Next Steps
0. Update `requirements.txt`
0. Centralize 100% of imports into `common.py` and replace all imports
0. Fix TODOs
0. Migrate all problems to use `web.py`
0. Migrate all search problems to use `search.py`
0. Auto-remove unused imports when importing `common.py` by detecting what will be used 
0. Identify and improve other common patterns
0. Translate text like in 21-13 and elsewhere to a submission
