"""
CodeMetrics - python script summarizing source code base
"""

import os           # for file access
import sys          # for command line arguments
import pandas as pd # for data storage and manipulation

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog

from codemetrics.engine import gather_info
from codemetrics.cli import print_summary


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


def main():
    """Main function"""
    origin = determine_source_dir(sys.argv)
    summary, omit_cnt = gather_info(origin)
    print_summary(summary, omit_cnt)


if __name__ == "__main__":
    main()
