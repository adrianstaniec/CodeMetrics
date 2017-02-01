"""
CodeMetrics - summarizes source codebases
"""

import os
import sys

from codemetrics.engine import gather_info
from codemetrics.cli import print_summary
from codemetrics.gui import ask_for_source_dir


def determine_source(args):
    """Determine source code directory path"""
    path = ''
    if len(args) == 2:
        path = args[1]
    else:
        path = ask_for_source_dir(sys.argv)
    project_name = path.split(os.sep)[-1]
    return path, project_name


def main():
    """Main function"""
    path, project_name = determine_source(sys.argv)
    summary, omit_cnt = gather_info(path)
    print_summary(project_name, summary, omit_cnt)


if __name__ == "__main__":
    main()
