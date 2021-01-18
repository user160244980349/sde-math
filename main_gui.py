#!/usr/bin/env python
import logging

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWinExtras import QWinTaskbarButton

from ui.main.main_window import MainWindow


def main():
    """
    Runs initialization of components if it is necessary and
    runs gui application
    """

    logging.basicConfig(level=logging.INFO)

    app = QApplication([])
    app.setWindowIcon(QtGui.QIcon("resources/function.svg"))
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))

    main_window = MainWindow()

    main_window.taskbar_button = QWinTaskbarButton()
    main_window.taskbar_button.setOverlayIcon(QtGui.QIcon("resources/function.svg"))

    # Это до кучи пример если в таскбаре надо показывать прогресс работы
    # main_window.taskbar_progress = window.taskbar_button.progress()
    # main_window.taskbar_progress.setRange(0, 100)
    # main_window.taskbar_progress.setValue(50);
    # main_window.taskbar_progress.show()
    # main_window.taskbar_button.setWindow(main_window.windowHandle())

    main_window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
