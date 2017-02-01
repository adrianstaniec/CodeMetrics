# CodeMetrics
Run it on a folder with (unknown) source code to get to know some summary information about it.

## Usage

### Command Line Interface
```bash
python -m codemetrics directory_path
```

### Graphical User Interface
```bash
python -m codemetrics
```
*at the moment the output is still printed to the terminal

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
Add GUI output           | :x:

### Non-Functional

Item                     | Status
-------------------------|--------------------
Split UI from the engine | :white_check_mark:
Add engine tests         | :x:
