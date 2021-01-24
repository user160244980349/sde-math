from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, \
    QApplication, QStyle

from ui.main.error import ErrorWidget
from ui.main.info import InfoIcon
from ui.main.modeling.matrix_widget import MatrixWidget


class Step7(QWidget):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.errors = 0

        # widgets creation

        header = QLabel("Setting of column x0", parent=self)
        font = header.font()
        font.setPointSize(15)
        header.setFont(font)

        info = InfoIcon("Elements of column x0 are\n"
                        "expected to be real values\n"
                        "Size: n x 1")

        self.msg = ErrorWidget("Wrong values in matrix!")
        self.msg.hide()

        self.matrix = MatrixWidget(self)

        self.next_btn = QPushButton("Next", self)
        self.next_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_ArrowForward))

        self.prev_btn = QPushButton("Back", self)
        self.prev_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_ArrowBack))

        # layout configuration

        header_layout = QHBoxLayout()
        header_layout.addWidget(info)
        header_layout.addWidget(header)
        header_layout.addWidget(self.msg)
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

        self.matrix.itemChanged.connect(self.validate_item)

    def validate_item(self, item):

        value = item.text()
        try:
            float(value)
            if not item.valid:
                item.valid = True
                self.errors -= 1

        except ValueError:
            if item.valid:
                item.valid = False
                self.errors += 1

        finally:
            self.validate_form()

    def validate_form(self):

        if self.errors == 0:
            self.msg.hide()
            self.next_btn.setEnabled(True)
        else:
            self.msg.show()
            self.next_btn.setEnabled(False)
