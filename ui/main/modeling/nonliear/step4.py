from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy

from ui.main.info_icon import InfoIcon
from ui.main.modeling.matrix_widget import MatrixWidget


class Step4(QWidget):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.input_stack = self.parent()

        header = QLabel("Setting of x0 column", parent=self)
        font = header.font()
        font.setPointSize(15)
        header.setFont(font)

        info = InfoIcon("")

        header_layout = QHBoxLayout()
        header_layout.addWidget(info)
        header_layout.addWidget(header)
        header_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.matrix = MatrixWidget(self)

        layout = QVBoxLayout()
        layout.addLayout(header_layout)
        layout.addWidget(self.matrix)

        self.setLayout(layout)
