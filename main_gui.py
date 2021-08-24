#!/usr/bin/env python
import logging
import os
import sys

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

from config import images
from config import recursion_limit
from ui.main.main_window import MainWindow


def main():
    """
    Runs gui application
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S"
    )

    sys.setrecursionlimit(recursion_limit)

    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(images, "function.png")))
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))

    MainWindow()

    exit(app.exec())


if __name__ == "__main__":
    main()
