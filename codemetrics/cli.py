"""
Command Line Interface module for Code Metrics
"""

import math
import os
import logging


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


def calc_scaling_factor(ser, width):
    """Calculate the factor for scaling count to bargraph"""
    avail_cols = width  - 1 - EXTENSION_STR_LEN - 1 - COUNT_STR_LEN
    avail_cols -= RIGHT_MARGIN
    max_val = ser.max()
    factor = 1
    if ser.max() > avail_cols:
        factor = avail_cols / max_val
    return factor


def print_column(ser, width, char):
    """Print a single column"""
    factor = calc_scaling_factor(ser, width)
    ser = ser.sort_values(ascending=False)
    cnt = 0
    for extention, count in ser.iteritems():
        print(str(extention).ljust(EXTENSION_STR_LEN),
              str(count).rjust(COUNT_STR_LEN),
              char * math.floor(count * factor))
        cnt += 1
        if cnt >= NUM_EXTENSION_TO_REPORT:
            print('...\n')
            break


def determine_screen_width():
    try:
        terminal_columns = os.get_terminal_size().columns
        terminal_columns = min(terminal_columns, DEFAULT_TERMINAL_WIDTH)
    except OSError:
        terminal_columns = DEFAULT_TERMINAL_WIDTH
        logging.info("Terminal width couldn't be detected, "
                     "{0} chars assumed." .format(DEFAULT_TERMINAL_WIDTH))
    return terminal_columns


def print_summary(project, data, omit_cnt):
    """Print summary text to output"""
    width = determine_screen_width()

    title = ' project "{0}" - code metrics '.format(project)
    print('\n' + title.center(width, '_') + '\n')

    print("File types:")
    print_column(data['Files'], width, '*')

    print("Code lines:")
    print_column(data['Lines'], width, '=')

    if omit_cnt > 0:
        print("Lines in {0} files were not counted,".format(omit_cnt),
              "because they could not be decoded.")

    print(width * '_')

