"""
Command Line Interface module for Code Metrics
"""

import math         # for flooring floats
import os           # for file access


def determine_source_dir(args):
    """Determine source code directory path"""
    origin = ''
    if len(args) == 2:
        origin = args[1]
    else:
        origin = os.path.abspath('.')
    return origin


def calc_scaling_factor(ser):
    """Calculate the factor for scaling data to charbar"""
    try:
        line_width = os.get_terminal_size().columns
    except OSError:
        line_width = 80
    avail_cols = line_width - 20
    max_val = ser.max()
    factor = 1
    if ser.max() > avail_cols:
        factor = avail_cols / max_val
    return factor


def print_column(ser, factor):
    """Print a single column"""
    ser = ser.sort_values(ascending=False)
    cnt = 0
    for ind, val in ser.iteritems():
        print(str(ind).ljust(6), str(val).rjust(7), end='')
        print(' ', '*' * math.floor(val * factor))
        cnt += 1
        if cnt >= 10:
            print('...')
            break


def print_summary(data, omit_cnt):
    """Print summary text to output"""
    print("\nFile types:")
    factor = calc_scaling_factor(data['Files'])
    print_column(data['Files'], factor)

    print("\nCode lines:")
    factor = calc_scaling_factor(data['Lines'])
    print_column(data['Lines'], factor)

    if omit_cnt > 0:
        print("")
        print("Lines in {0} files were not counted, due to decoding problems.".format(omit_cnt))
