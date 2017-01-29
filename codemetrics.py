"""
CodeMetrics - python script summarizing source code base
"""

import math         # for flooring floats
import os           # for file access
import sys          # for command line arguments
import pandas as pd # for data storage and manipulation

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog

def determine_source_dir(args):
    """Determine source code directory path"""
    origin = ''
    if len(args) == 2:
        origin = args[1]
    else:
        app = QApplication(sys.argv)
        window_title = "CodeMetrics: Select the project source code directory"
        qpath = QFileDialog.getExistingDirectory(None, window_title)
        origin = os.path.abspath(qpath)
    return origin


def scan_file(filepath):
    """Analyzes a single file's name and content"""
    dummy, ext = os.path.splitext(filepath)
    lncnt = 0
    omitted = 0

    encodings = ['utf-8', None]
    for enc in encodings:
        try:
            with open(filepath, mode='r', encoding=enc) as filelines:
            # with open(filepath) as filelines:
                for line in filelines:
                    line = line.rstrip()
                    if line != "":
                        lncnt += 1
            break
        except UnicodeDecodeError:
            continue
    else:
        omitted = 1

    return ext, lncnt, omitted


def gather_info(origin):
    """Crawl the directory for stats"""
    # Prepare data structures
    file_types = pd.Series(dtype='int64', name='Files')
    code_lines = pd.Series(dtype='int64', name='Lines')
    summary = pd.concat([file_types, code_lines], axis=1)
    summary.index.name = "File type"
    omit_cnt = 0

    # Gather information
    for root, dummy, files in os.walk(origin):
        for filename in files:
            ext, lncnt, omitted = scan_file(os.path.join(root, filename))
            omit_cnt += omitted
            ext = ext.lower()
            try:
                summary.loc[ext] += 1, lncnt
            except KeyError:
                summary.loc[ext] = 1, lncnt

    return summary, omit_cnt


def calc_scaling_factor(ser):
    """Calculate the facotr for scaling data to charbar"""
    line_width = os.get_terminal_size().columns
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


def main():
    """Main function"""
    origin = determine_source_dir(sys.argv)
    summary, omit_cnt = gather_info(origin)
    print_summary(summary, omit_cnt)


if __name__ == "__main__":
    main()
