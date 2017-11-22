#!/usr/bin/env python
"""
CodeMetrics - summarizes source codebases
"""

import os
import sys
import logging
import argparse

from PyQt5 import QtWidgets

from codemetrics import engine
from codemetrics import cli
from codemetrics import gui


def main_cli(path=None):
    if path is None:
        path = input("Provide path with code base location: ")
    if path[-1] == os.sep:
        path = path[:-1]
    project_name = path.split(os.sep)[-1]
    summary, omit_cnt = engine.gather_info(path)
    cli.print_summary(project_name, summary, omit_cnt)


def main_gui(path=None):
    qApp = QtWidgets.QApplication(sys.argv)
    aw = gui.AppWin(path)
    aw.show()
    sys.exit(qApp.exec_())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-p", "--path", type=str, default=None,
                        help="Path to code base directory")
    parser.add_argument("-t", "--text-mode", action="store_true",
                        help="Use CLI, not the GUI.")
    args = parser.parse_args()

    if args.text_mode:
        main_cli(args.path)
    else:
        main_gui(args.path)
