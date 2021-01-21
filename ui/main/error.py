from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QApplication, QStyle, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy


class ErrorWidget(QWidget):

    def __init__(self, text: str, parent=None):
        super(QWidget, self).__init__(parent)

        msg_m = QLabel(text)
        msg_m.setStyleSheet("QLabel { color: rgb(230, 0, 0); }")

        msg_i = QLabel()
        msg_i.setStyleSheet("QToolTip { background: white; }")
        msg_i.setPixmap(QApplication.style().standardIcon(
            QStyle.SP_MessageBoxCritical).pixmap(QSize(16, 16)))

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(msg_i)
        layout.addWidget(msg_m)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.setLayout(layout)
