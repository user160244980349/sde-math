from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout, QGridLayout, QSpacerItem, QSizePolicy

from ui.main.info_icon import InfoIcon


class Step1(QWidget):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        info_n = InfoIcon("TOOLTIP")
        info_m = InfoIcon("TOOLTIP")
        info_k = InfoIcon("TOOLTIP")

        label_n = QLabel("n")
        label_m = QLabel("m")
        label_k = QLabel("k")

        lineedit_n = QLineEdit()
        lineedit_m = QLineEdit()
        lineedit_k = QLineEdit()

        grid_layout = QGridLayout()
        grid_layout.addWidget(info_n, 0, 0)
        grid_layout.addWidget(info_m, 1, 0)
        grid_layout.addWidget(info_k, 2, 0)
        grid_layout.addWidget(label_n, 0, 1)
        grid_layout.addWidget(label_m, 1, 1)
        grid_layout.addWidget(label_k, 2, 1)
        grid_layout.addWidget(lineedit_n, 0, 2)
        grid_layout.addWidget(lineedit_m, 1, 2)
        grid_layout.addWidget(lineedit_k, 2, 2)

        header = QLabel("Dimensions settings", parent=self)
        font = header.font()
        font.setPointSize(15)
        header.setFont(font)

        header_layout = QHBoxLayout()
        header_layout.addWidget(header)
        header_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        column_layout = QVBoxLayout()
        column_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        column_layout.addLayout(header_layout)
        column_layout.addItem(QSpacerItem(0, 25, QSizePolicy.Minimum, QSizePolicy.Minimum))
        column_layout.addLayout(grid_layout)
        column_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        layout = QHBoxLayout()
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        layout.addLayout(column_layout)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.setLayout(layout)
