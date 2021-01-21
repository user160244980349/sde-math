from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QLineEdit, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy, \
    QPushButton, QApplication, QStyle

from ui.main.error import ErrorWidget
from ui.main.info import InfoIcon


class Step1(QWidget):
    """
    Application main window
    """
    n_valid = pyqtSignal(int)
    m_valid = pyqtSignal(int)
    k_valid = pyqtSignal(int)

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        # other variables

        self.n_is_valid = False
        self.m_is_valid = False
        self.k_is_valid = False

        self.input_stack = self.parent()

        # widget creation

        info_n = InfoIcon("Dimension of linear system of Ito SDEs")
        info_m = InfoIcon("Dimension of vector Wiener process")
        info_k = InfoIcon("Dimension of vector function u(t)")

        label_n = QLabel("n")
        label_m = QLabel("m")
        label_k = QLabel("k")

        self.lineedit_n = QLineEdit()
        self.lineedit_m = QLineEdit()
        self.lineedit_k = QLineEdit()

        self.msg_n = ErrorWidget("Wrong value!")
        self.msg_n.hide()

        self.msg_m = ErrorWidget("Wrong value!")
        self.msg_m.hide()

        self.msg_k = ErrorWidget("Wrong value!")
        self.msg_k.hide()

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.msg_n, 0, 2)
        grid_layout.addWidget(self.msg_m, 2, 2)
        grid_layout.addWidget(self.msg_k, 4, 2)
        grid_layout.addWidget(info_n, 1, 0)
        grid_layout.addWidget(info_m, 3, 0)
        grid_layout.addWidget(info_k, 5, 0)
        grid_layout.addWidget(label_n, 1, 1)
        grid_layout.addWidget(label_m, 3, 1)
        grid_layout.addWidget(label_k, 5, 1)
        grid_layout.addWidget(self.lineedit_n, 1, 2)
        grid_layout.addWidget(self.lineedit_m, 3, 2)
        grid_layout.addWidget(self.lineedit_k, 5, 2)

        header = QLabel("Dimensions settings", parent=self)
        font = header.font()
        font.setPointSize(15)
        header.setFont(font)

        self.next_btn = QPushButton("Next", self)
        self.next_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_ArrowForward))
        self.next_btn.setEnabled(False)

        # layout  configuration

        header_layout = QHBoxLayout()
        header_layout.addWidget(header)
        header_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        bottom_bar = QHBoxLayout()
        bottom_bar.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        bottom_bar.addWidget(self.next_btn)

        column_layout = QVBoxLayout()
        column_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        column_layout.addLayout(header_layout)
        column_layout.addItem(QSpacerItem(0, 25, QSizePolicy.Minimum, QSizePolicy.Minimum))
        column_layout.addLayout(grid_layout)
        column_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        control_layout = QHBoxLayout()
        control_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        control_layout.addLayout(column_layout)
        control_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        layout = QVBoxLayout()
        layout.addLayout(control_layout)
        layout.addLayout(bottom_bar)

        self.setLayout(layout)

        # signals binding

        self.lineedit_n.textChanged.connect(self.validate_n)
        self.lineedit_m.textChanged.connect(self.validate_m)
        self.lineedit_k.textChanged.connect(self.validate_k)

    def validate_form(self):
        if self.n_is_valid and self.m_is_valid:
            self.next_btn.setEnabled(True)
        else:
            self.next_btn.setEnabled(False)

    def validate_n(self, value):
        try:
            typed_value = int(value)
            if typed_value <= 0:
                raise ValueError()

            self.n_is_valid = True
            self.n_valid.emit(typed_value)
            self.msg_n.hide()

        except ValueError:
            self.n_is_valid = False
            self.msg_n.show()

        finally:
            self.validate_form()

    def validate_m(self, value):
        try:
            typed_value = int(value)
            if typed_value <= 0:
                raise ValueError()

            self.m_is_valid = True
            self.m_valid.emit(typed_value)
            self.msg_m.hide()

        except ValueError:
            self.m_is_valid = False
            self.msg_m.show()

        finally:
            self.validate_form()

    def validate_k(self, value):
        try:
            typed_value = int(value)
            if typed_value <= 0:
                raise ValueError()

            self.k_is_valid = True
            self.k_valid.emit(typed_value)
            self.msg_k.hide()

        except ValueError:
            self.k_is_valid = False
            self.msg_k.show()

        finally:
            self.validate_form()
