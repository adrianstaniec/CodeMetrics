import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog


def ask_for_source_dir(argv):
    app = QApplication(argv)
    window_title = "CodeMetrics: Select the project source code directory"
    qpath = QFileDialog.getExistingDirectory(None, window_title)
    return os.path.abspath(qpath)


