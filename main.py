import os
import sys
from os.path import join

from PyQt5 import QtWidgets

from config import database as dbname, resources
from init.init import init
from tools import database, fsys
from ui.Window import Window


def main():
    database.connect(dbname)

    if not fsys.is_locked(join(resources, '.init.lock')):
        init()
        fsys.lock(join(resources, '.init.lock'))

    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    sys.exit(app_exit(app))


def app_exit(app):
    app.exec()
    database.disconnect()
    pass


if __name__ == '__main__':
    main()
