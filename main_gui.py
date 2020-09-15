#!/usr/bin/env python
from PyQt5.QtWidgets import QApplication

import tools.database as db
from config import database
from init.init import init
from ui.main_window import MainWindow


def main():
    """
    Runs initialization of components if it is necessary and
    runs gui application
    """
    init()
    db.connect(database)

    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    exit(app_exit(app))


def app_exit(app):
    """
    Provides correct database disconnect
    while application is closing
    """
    app.exec()
    db.disconnect()


if __name__ == "__main__":
    main()
