#!/usr/bin/env python
import logging
import os
import sys

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWinExtras import QWinTaskbarButton

from config import database, images
from mathematics.sde.nonlinear.symbolic.coefficients.c import C
from tools.database import connect, disconnect
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

    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(images, "function.png")))
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))

    main_window = MainWindow()

    main_window.taskbar_button = QWinTaskbarButton()
    main_window.taskbar_button.setOverlayIcon(QtGui.QIcon("resources/function.svg"))

    exit(app.exec())


if __name__ == "__main__":
    main()
