"""
Graphical User Interface module for Code Metrics
"""

import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog


def ask_for_source_dir(argv):
    """Ask user to select code source path with a dialog"""
    app = QApplication(argv)
    window_title = "CodeMetrics: Select the project source code directory"
    qpath = QFileDialog.getExistingDirectory(None, window_title)
    return os.path.abspath(qpath)
