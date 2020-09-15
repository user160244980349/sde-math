from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDesktopWidget


class Window(QtWidgets.QMainWindow):
    """
    Application main window
    """

    def __init__(self):
        super(Window, self).__init__()

        self.title = "Plots"
        self.left = 0
        self.top = 0
        self.right = 800
        self.bot = 600

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.right, self.bot)
        self.center()

    def center(self):
        """
        Centers the window
        """
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
