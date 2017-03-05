"""
Graphical User Interface module for Code Metrics
"""

import os
import pandas as pd

import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from codemetrics import engine


class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes0 = fig.add_subplot(211)
        self.axes1 = fig.add_subplot(212)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def update_plot(self, df):
        df = df.sort_index().sort_values('Files', ascending=False)
        files = df['Files'].sort_values().tail(10)
        lines = df['Lines'].sort_values().tail(10)
        self.axes0.clear()
        self.axes1.clear()
        files.plot(ax=self.axes0, kind='barh')
        self.axes0.set_xlabel('No. of files')
        lines.plot(ax=self.axes1, kind='barh')
        self.axes1.set_xlabel('No. of lines')
        self.draw()


class AppWin(QtWidgets.QMainWindow):
    def __init__(self, path=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Open', self.open_dir, QtCore.Qt.Key_O)
        self.file_menu.addAction('&Quit', self.close, QtCore.Qt.Key_Q)

        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.help_menu.addAction('&About', self.about, QtCore.Qt.Key_A)

        self.menuBar().addMenu(self.file_menu)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.main_widget = QtWidgets.QWidget(self)

        l = QtWidgets.QVBoxLayout(self.main_widget)
        self.sc = MyMplCanvas(self.main_widget)
        l.addWidget(self.sc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.open_dir(path)

    def open_dir(self, path=None):
        if path is None:
            window_title = "CodeMetrics: Select the project source code dir"
            qpath = QtWidgets.QFileDialog.getExistingDirectory(None,
                                                               window_title)
            path = os.path.abspath(qpath)
        df, _ = engine.gather_info(os.path.abspath(path))
        self.sc.update_plot(df)
        project_name = path.split(os.sep)[-1]
        self.setWindowTitle(f"CodeMetrics - project \"{project_name}\"")

    def about(self):
        astr = "This is CodeMetrics by adrsta"
        QtWidgets.QMessageBox.about(self, "About", astr)
