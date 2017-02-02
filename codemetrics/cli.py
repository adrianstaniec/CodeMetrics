"""
Command Line Interface module for Code Metrics
"""

import math
import os
import logging
import colorama

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


def determine_screen_width():
    try:
        terminal_columns = os.get_terminal_size().columns
        terminal_columns = min(terminal_columns, DEFAULT_TERMINAL_WIDTH)
    except OSError:
        terminal_columns = DEFAULT_TERMINAL_WIDTH
        logging.info("Terminal width couldn't be detected, "
                     "{0} chars assumed." .format(DEFAULT_TERMINAL_WIDTH))
    return terminal_columns


def assign_colors(keys):
    color_map = {}
    avail_colors = [colorama.Fore.CYAN, colorama.Fore.YELLOW,
                    colorama.Fore.RED, colorama.Fore.GREEN,
                    colorama.Fore.WHITE, colorama.Fore.MAGENTA,
                    colorama.Fore.BLUE]
    for counter, key in enumerate(keys):
        color_map[key] = avail_colors[(counter) % len(avail_colors)]
    return color_map


def print_title(project, width):
    title = ' project "{0}" - code metrics '.format(project)
    title = '\n' + title.center(width) + '\n'
    parts = title.split(project)
    print(parts[0], end='')
    print(colorama.Style.BRIGHT + project, end='' + colorama.Style.RESET_ALL)
    print(parts[1], end='')


def calc_scaling_factor(ser, width):
    """Calculate the factor for scaling count to bargraph"""
    avail_cols = width  - 1 - EXTENSION_STR_LEN - 1 - COUNT_STR_LEN
    avail_cols -= RIGHT_MARGIN
    max_val = ser.max()
    factor = 1
    if ser.max() > avail_cols:
        factor = avail_cols / max_val
    return factor


def print_column(ser, width, char, color_map=None):
    """Print a single column"""
    factor = calc_scaling_factor(ser, width)
    ser = ser.sort_values(ascending=False)
    cnt = 0
    for extension, count in ser.iteritems():
        line = str(extension).ljust(EXTENSION_STR_LEN)
        line += ' ' + str(count).rjust(COUNT_STR_LEN)
        line += ' ' + char * math.floor(count * factor)
        if color_map != None:
            line = color_map[extension] + line + colorama.Fore.RESET
        print(line)
        cnt += 1
        if cnt >= NUM_EXTENSION_TO_REPORT:
            print('...\n')
            break


def print_summary(project, data, omit_cnt, colorful=True):
    """Print summary text to output"""
    width = determine_screen_width()
    colorama.init()

    print_title(project, width)

    if colorful:
        data = data.sort_index().sort_values('Files',ascending=False)
        color_map = assign_colors(data.index)
    else:
        color_map = None

    print(colorama.Style.BRIGHT)
    print("File types:")
    print_column(data['Files'], width, '*', color_map)
    print("Code lines:")
    print_column(data['Lines'], width, '=', color_map)
    print(colorama.Style.RESET_ALL)

    if omit_cnt > 0:
        print("Lines in {0} files were not counted,".format(omit_cnt),
              "because they could not be decoded.")
