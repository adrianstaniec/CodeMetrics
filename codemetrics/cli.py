"""
Command Line Interface module for Code Metrics
"""

import math         # for flooring floats
import os           # for file access


DEFAULT_TERMINAL_WIDTH = 80
EXTENSION_STR_LEN = 7
COUNT_STR_LEN = 7
RIGHT_MARGIN = 1
NUM_EXTENSION_TO_REPORT = 10


def determine_source_dir(args):
    """Determine source code directory path"""
    origin = ''
    if len(args) == 2:
        origin = args[1]
    else:
        origin = os.path.abspath('.')
    return origin


def calc_scaling_factor(ser):
    """Calculate the factor for scaling count to bargraph"""
    try:
        line_width = os.get_terminal_size().columns
    except OSError:
        line_width = DEFAULT_TERMINAL_WIDTH
    avail_cols = line_width - EXTENSION_STR_LEN - COUNT_STR_LEN - 2 - RIGHT_MARGIN
    max_val = ser.max()
    factor = 1
    if ser.max() > avail_cols:
        factor = avail_cols / max_val
    return factor


def print_column(ser, factor):
    """Print a single column"""
    ser = ser.sort_values(ascending=False)
    cnt = 0
    for extention, count in ser.iteritems():
        print(str(extention).ljust(EXTENSION_STR_LEN),
              str(count).rjust(COUNT_STR_LEN),
              '*' * math.floor(count * factor))
        cnt += 1
        if cnt >= NUM_EXTENSION_TO_REPORT:
            print('...')
            break


def print_summary(project, data, omit_cnt):
    """Print summary text to output"""
    print("\n=== Code Metrics for project {0} ===".format(project))
    print("\nFile types:")
    factor = calc_scaling_factor(data['Files'])
    print_column(data['Files'], factor)

    print("\nCode lines:")
    factor = calc_scaling_factor(data['Lines'])
    print_column(data['Lines'], factor)

    if omit_cnt > 0:
        print("")
        print("Lines in {0} files were not counted, due to decoding problems.".format(omit_cnt))
