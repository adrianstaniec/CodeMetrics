import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog

app = QApplication(sys.argv)
qpath = QFileDialog.getExistingDirectory(None,
"KodeMetrics: Select the project source code directory")
print(os.path.abspath(qpath))