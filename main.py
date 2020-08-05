from PyQt5.QtWidgets import QApplication

from config import database
from init.init import init
from tools.database import connect, disconnect
from ui.Window import Window


def main():
    init()
    connect(database)

    app = QApplication([])
    window = Window()
    window.show()
    exit(app_exit(app))


def app_exit(app):
    app.exec()
    disconnect()


if __name__ == '__main__':
    main()
