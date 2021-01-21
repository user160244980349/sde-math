from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QLineEdit, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy, \
    QPushButton, QApplication, QStyle

from ui.main.error import ErrorWidget
from ui.main.info import InfoIcon
from ui.main.svg import SVG


class Step1(QWidget):
    """
    Application main window
    """
    n_valid = pyqtSignal(int)
    m_valid = pyqtSignal(int)

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        # other variables

        self.n_is_valid = False
        self.m_is_valid = False

        self.input_stack = self.parent()

        # widget creation

        info_n = InfoIcon("Dimension of linear system of Ito SDEs")
        info_m = InfoIcon("Dimension of vector Wiener process")

        label_n = QLabel("n")
        label_m = QLabel("m")

        self.lineedit_n = QLineEdit()
        self.lineedit_m = QLineEdit()

        self.msg_n = ErrorWidget("Wrong value!")
        self.msg_n.hide()

        self.msg_m = ErrorWidget("Wrong value!")
        self.msg_m.hide()

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.msg_n, 0, 2)
        grid_layout.addWidget(self.msg_m, 2, 2)
        grid_layout.addWidget(info_n, 1, 0)
        grid_layout.addWidget(info_m, 3, 0)
        grid_layout.addWidget(label_n, 1, 1)
        grid_layout.addWidget(label_m, 3, 1)
        grid_layout.addWidget(self.lineedit_n, 1, 2)
        grid_layout.addWidget(self.lineedit_m, 3, 2)

        header = QLabel("Dimensions settings", parent=self)
        font = header.font()
        font.setPointSize(15)
        header.setFont(font)

        self.next_btn = QPushButton("Next", self)
        self.next_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_ArrowForward))
        self.next_btn.setEnabled(False)

        # layout  configuration

        header_layout = QHBoxLayout()
        header_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        header_layout.addWidget(header)
        header_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        bottom_bar = QHBoxLayout()
        bottom_bar.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        bottom_bar.addWidget(self.next_btn)

        eq1 = QHBoxLayout()
        eq1.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        eq1.addWidget(SVG("equation1.svg", scale_factor=1.))
        eq1.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        eq2 = QHBoxLayout()
        eq2.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        eq2.addWidget(SVG("equation2.svg", scale_factor=0.8))
        eq2.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        equalities_layout = QVBoxLayout()
        equalities_layout.addLayout(eq1)
        equalities_layout.addItem(QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Minimum))
        equalities_layout.addLayout(eq2)

        equalities_wrap = QHBoxLayout()
        equalities_wrap.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        equalities_wrap.addLayout(equalities_layout)
        equalities_wrap.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        grid_wrap = QHBoxLayout()
        grid_wrap.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        grid_wrap.addLayout(grid_layout)
        grid_wrap.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        layout = QVBoxLayout()
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addLayout(equalities_wrap)
        layout.addItem(QSpacerItem(0, 25, QSizePolicy.Minimum, QSizePolicy.Minimum))
        layout.addLayout(header_layout)
        layout.addItem(QSpacerItem(0, 5, QSizePolicy.Minimum, QSizePolicy.Minimum))
        layout.addLayout(grid_wrap)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addItem(QSpacerItem(0, 25, QSizePolicy.Minimum, QSizePolicy.Minimum))
        layout.addLayout(bottom_bar)

        self.setLayout(layout)

        # signals binding

        self.lineedit_n.textChanged.connect(self.validate_n)
        self.lineedit_m.textChanged.connect(self.validate_m)

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
