from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QGridLayout, QVBoxLayout, QSizePolicy, QSpacerItem

from ui.main.info_icon import InfoIcon


class Step5(QWidget):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.input_stack = self.parent()

        info_t0 = InfoIcon("TOOLTIP")
        info_dt = InfoIcon("TOOLTIP")
        info_t1 = InfoIcon("TOOLTIP")
        info_s = InfoIcon("TOOLTIP")
        self.info_c = InfoIcon("TOOLTIP")

        label_t0 = QLabel("t0")
        label_dt = QLabel("dt")
        label_t1 = QLabel("t1")
        label_s = QLabel("seed")
        self.label_c = QLabel("C")

        self.lineedit_t0 = QLineEdit()
        self.lineedit_dt = QLineEdit()
        self.lineedit_t1 = QLineEdit()
        self.lineedit_s = QLineEdit()
        self.lineedit_c = QLineEdit()

        grid_layout = QGridLayout()
        grid_layout.addWidget(info_t0, 0, 0)
        grid_layout.addWidget(label_t0, 0, 1)
        grid_layout.addWidget(self.lineedit_t0, 0, 2)

        grid_layout.addWidget(info_dt, 0, 3)
        grid_layout.addWidget(label_dt, 0, 4)
        grid_layout.addWidget(self.lineedit_dt, 0, 5)

        grid_layout.addWidget(info_t1, 0, 6)
        grid_layout.addWidget(label_t1, 0, 7)
        grid_layout.addWidget(self.lineedit_t1, 0, 8)

        grid_layout.addWidget(info_s, 1, 0)
        grid_layout.addWidget(label_s, 1, 1)
        grid_layout.addWidget(self.lineedit_s, 1, 2)

        grid_layout.addWidget(self.info_c, 1, 3)
        grid_layout.addWidget(self.label_c, 1, 4)
        grid_layout.addWidget(self.lineedit_c, 1, 5)

        header = QLabel("Accuracy settings", parent=self)
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
