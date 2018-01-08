import sys

import matplotlib

# Make sure that we are using QT5
matplotlib.use('Qt5Agg')

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication

from main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()

    main_window.show()

    sys.exit(app.exec_())
