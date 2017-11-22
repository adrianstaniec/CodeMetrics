[![Build Status](https://travis-ci.org/adrianstaniec/CodeMetrics.png?branch=master)](http://travis-ci.org/adrianstaniec/CodeMetrics?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/adrianstaniec/CodeMetrics/badge.svg?branch=master)](https://coveralls.io/github/adrianstaniec/CodeMetrics?branch=master)

# CodeMetrics
Run it on a folder with (unknown) source code to get to know some summary information about it.

## Usage

### Command Line Interface
```bash
python -m codemetrics -t [-p directory_path]
```

### Graphical User Interface
```bash
python -m codemetrics [-p directory_path]
```

## Roadmap

### Functional

Function                 | Status
-------------------------|--------------------
File count per file type | :white_check_mark:
Line count per file type | :white_check_mark:
Count files omitted      | :white_check_mark:
Support more than UTF-8  | :white_check_mark:
Show textual histobar    | :white_check_mark:
Add GUI dir selector     | :white_check_mark:
Colorize the output      | :white_check_mark:
Allow exec. parameters   | :white_check_mark:
Add GUI output           | :white_check_mark:
Improve plots            | :x:

### Non-Functional

Item                        | Status
----------------------------|--------------------
Split UI from the engine    | :white_check_mark:
Setup pytest                | :white_check_mark:
Fix tests                   | :white_check_mark:
Increase coverage           | :construction:
Setup Travis CI             | :white_check_mark:
Setup Coveralls             | :white_check_mark:
Improve start-up time       | :x:
