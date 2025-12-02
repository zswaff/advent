# Advent of Code Solutions

## Introduction

This repo has solutions to the [Advent of Code](https://adventofcode.com/)
online coding problems. It solves all historical problems and will be updated
to solve new ones as they are released.

The solutions are written for combined development and execution speed (i.e.
to minimize the total time from when I start reading the problem to when I have
submitted the correct answer) and are therefore not up to the highest standards
of excellence stylistically.

## Utilities

### Data

| Variable | Purpose   |
| -------- | --------- |
| `dt`     |  raw data |
| `ls`     |  lines    |
| `l`      |  line     |
| `ss`     |  sections |
| `sm(…)`  |  submit   |

### Processing

| Variable        | Purpose                                                                      |
| --------------- | ---------------------------------------------------------------------------- |
| `pa(l, pt+)`    | pattern match, e.g. `pa(l, "valve {} has flow rate={i}")`                    |
| `gr(ls, fn?)`   | gridify lines, optionally postprocessing each character                      |
| `cngr(es, tgs)` | condense graph from (edge_map: {T, {T, int}}, targets: [T]) -> {T, {T, int}} |

### Other

- Assembly
- Search
- Timer

## Project Structure

- `aoc.py` utility for standard imports
- `assembly.py` utility for assembly problems
- `search.py` utility for search problems
- `timer.py` utility for timing a process
- `web.py` utility for interacting with the website
- `prototype` a directory to copy and rename for a new problem
- `[year]` a year
  - `[day]` a day of december
    - `sln.py` the solution file
    - `inp.txt` the input from the specific problem; optional if the input data is in solution file

## Yearly Setup

Set the `AOC_SESSION` environment variable by following the following steps in Chrome

1. Open [AOC online](https://adventofcode.com/) and Log in
2. Right click > Inspect > Application > Cookies > https://adventofcode.com/
3. Copy the value of the session cookie to the `AOC_SESSION` environment variable

## Execution

Run a given solution with

```bash
cd ./[year]/[day]
./sln.py
```

## Next Steps

- [ ] Simplify imports so root doesn't have to be in PYTHONPATH
- [ ] Centralize 100% of imports into `aoc.py` and replace all imports
- [ ] Fix TODOs
- [ ] Migrate all problems to use `web.py`
- [ ] Migrate all search problems to use `search.py`
- [ ] Identify and improve other common patterns
- [ ] Translate text like in 2021-13 and elsewhere to a submission
- [ ] Improve types and naming of common stuff
