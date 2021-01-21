from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout, QPushButton, \
    QApplication, QStyle

from ui.main.info import InfoIcon
from ui.main.modeling.matrix_widget import MatrixWidget


class Step3(QWidget):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        # widgets creation

        header = QLabel("Setting of matrix B", parent=self)
        font = header.font()
        font.setPointSize(15)
        header.setFont(font)

        info = InfoIcon("Elements of matrix B are\n"
                        "expected to be real values\n"
                        "Size: n x k")

        self.matrix = MatrixWidget(self)

        self.next_btn = QPushButton("Next", self)
        self.next_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_ArrowForward))

        self.prev_btn = QPushButton("Back", self)
        self.prev_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_ArrowBack))

        # layout configuration

        header_layout = QHBoxLayout()
        header_layout.addWidget(info)
        header_layout.addWidget(header)
        header_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        bottom_bar = QHBoxLayout()
        bottom_bar.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        bottom_bar.addWidget(self.prev_btn)
        bottom_bar.addWidget(self.next_btn)

        layout = QVBoxLayout()
        layout.addLayout(header_layout)
        layout.addWidget(self.matrix)
        layout.addLayout(bottom_bar)

        self.setLayout(layout)
