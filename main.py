from PyQt5.QtWidgets import QApplication

import init as i
import tools.database as db
from config import database
from ui.Window import Window


def main():
    i.init()
    db.connect(database)

    app = QApplication([])
    window = Window()
    window.show()
    exit(app_exit(app))


def app_exit(app):
    app.exec()
    db.disconnect()


if __name__ == '__main__':
    main()
