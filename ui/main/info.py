from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QApplication, QStyle, QLabel


class InfoIcon(QLabel):

    def __init__(self, text: str, parent=None):
        super(QWidget, self).__init__(parent)

        self.setToolTip(text)
        self.setPixmap(QApplication.style().standardIcon(
            QStyle.SP_MessageBoxInformation).pixmap(QSize(16, 16)))
