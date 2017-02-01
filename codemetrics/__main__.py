"""
CodeMetrics - summarizes source codebases
"""

import sys

from codemetrics.engine import gather_info
from codemetrics.cli import print_summary
from codemetrics.gui import ask_for_source_dir


def determine_source_dir(args):
    """Determine source code directory path"""
    origin = ''
    if len(args) == 2:
        origin = args[1]
    else:
        origin = ask_for_source_dir(sys.argv)
    return origin


def main():
    """Main function"""
    origin = determine_source_dir(sys.argv)
    summary, omit_cnt = gather_info(origin)
    print_summary(summary, omit_cnt)


if __name__ == "__main__":
    main()
