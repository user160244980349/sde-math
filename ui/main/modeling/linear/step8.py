import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QGridLayout, QVBoxLayout, QSizePolicy, QSpacerItem, \
    QPushButton, QApplication, QStyle

from ui.main.info import InfoIcon


class Step8(QWidget):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        # other variables

        self.t0 = sys.float_info.min
        self.dt = 0
        self.t1 = sys.float_info.max
        self.s = 0

        self.t0_is_valid = False
        self.dt_is_valid = False
        self.t1_is_valid = False
        self.s_is_valid = True

        self.input_stack = self.parent()

        # widgets creation

        info_t0 = InfoIcon("TOOLTIP")
        info_dt = InfoIcon("TOOLTIP")
        info_t1 = InfoIcon("TOOLTIP")
        info_s = InfoIcon("TOOLTIP")
        self.info_c = InfoIcon("TOOLTIP")

        label_t0 = QLabel("t0")
        label_dt = QLabel("dt")
        label_t1 = QLabel("t1")
        label_s = QLabel("seed")

        self.lineedit_t0 = QLineEdit()
        self.lineedit_dt = QLineEdit()
        self.lineedit_t1 = QLineEdit()
        self.lineedit_s = QLineEdit()

        self.msg_t0 = QLabel()
        self.msg_t0.setStyleSheet("color: rgb(255, 0, 0);")
        self.msg_t0.hide()

        self.msg_dt = QLabel()
        self.msg_dt.setStyleSheet("color: rgb(255, 0, 0);")
        self.msg_dt.hide()

        self.msg_t1 = QLabel()
        self.msg_t1.setStyleSheet("color: rgb(255, 0, 0);")
        self.msg_t1.hide()

        self.msg_s = QLabel()
        self.msg_s.setStyleSheet("color: rgb(255, 0, 0);")
        self.msg_s.hide()

        header = QLabel("Accuracy settings", parent=self)
        font = header.font()
        font.setPointSize(15)
        header.setFont(font)

        self.prev_btn = QPushButton("Back", self)
        self.prev_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_ArrowBack))

        self.run_btn = QPushButton("Perform modeling", self)
        self.run_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_ArrowForward))
        self.run_btn.setEnabled(False)

        # layout configuration

        header_layout = QHBoxLayout()
        header_layout.addWidget(header)
        header_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        bottom_bar = QHBoxLayout()
        bottom_bar.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        bottom_bar.addWidget(self.prev_btn)
        bottom_bar.addWidget(self.run_btn)

        grid_layout = QGridLayout()

        grid_layout.addWidget(self.msg_t0, 0, 2)

        grid_layout.addWidget(info_t0, 1, 0)
        grid_layout.addWidget(label_t0, 1, 1)
        grid_layout.addWidget(self.lineedit_t0, 1, 2)

        grid_layout.addWidget(self.msg_dt, 0, 5)

        grid_layout.addWidget(info_dt, 1, 3)
        grid_layout.addWidget(label_dt, 1, 4)
        grid_layout.addWidget(self.lineedit_dt, 1, 5)

        grid_layout.addWidget(self.msg_t1, 0, 8)

        grid_layout.addWidget(info_t1, 1, 6)
        grid_layout.addWidget(label_t1, 1, 7)
        grid_layout.addWidget(self.lineedit_t1, 1, 8)

        grid_layout.addWidget(self.msg_s, 2, 2)

        grid_layout.addWidget(info_s, 3, 0)
        grid_layout.addWidget(label_s, 3, 1)
        grid_layout.addWidget(self.lineedit_s, 3, 2)

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

        # signals

        self.lineedit_t0.textChanged.connect(self.validate_t0)
        self.lineedit_t0.textChanged.connect(self.validate_t1)
        self.lineedit_t0.textChanged.connect(self.validate_dt)
        self.lineedit_dt.textChanged.connect(self.validate_dt)
        self.lineedit_t1.textChanged.connect(self.validate_t0)
        self.lineedit_t1.textChanged.connect(self.validate_t1)
        self.lineedit_t1.textChanged.connect(self.validate_dt)
        self.lineedit_s.textChanged.connect(self.validate_s)

    def count_c(self, flag: bool):
        if flag:
            self.info_c.show()
            self.label_c.show()
        else:
            self.info_c.hide()
            self.label_c.hide()

        self.msg_c.hide()

    def validate_form(self):
        if self.t0_is_valid \
                and self.dt_is_valid \
                and self.t1_is_valid \
                and self.s_is_valid:
            self.run_btn.setEnabled(True)
        else:
            self.run_btn.setEnabled(False)

    def validate_t0(self):
        try:
            typed_value = float(self.lineedit_t0.text())
            if typed_value >= self.t1:
                raise ValueError()

            self.t0_is_valid = True
            self.t0 = typed_value
            self.msg_t0.hide()

        except ValueError:
            self.t0_is_valid = False
            self.msg_t0.setText("Wrong value!")
            self.msg_t0.show()

    def validate_dt(self):
        try:
            typed_value = float(self.lineedit_dt.text())
            if typed_value <= 0 or (self.t1 - self.t0) / typed_value < 1 or typed_value >= 1:
                raise ValueError("input error")

            self.dt_is_valid = True
            self.dt = typed_value
            self.msg_dt.hide()
            self.validate_form()

        except ValueError:
            self.dt_is_valid = False
            self.msg_dt.setText("Wrong value!")
            self.msg_dt.show()

    def validate_t1(self):
        try:
            typed_value = float(self.lineedit_t1.text())
            if typed_value <= self.t0:
                raise ValueError()

            self.t1_is_valid = True
            self.t1 = typed_value
            self.msg_t1.hide()

        except ValueError:
            self.t1_is_valid = False
            self.msg_t1.setText("Wrong value!")
            self.msg_t1.show()

    def validate_s(self):
        try:
            if self.lineedit_s.text() == "":
                self.s_is_valid = True
                self.s = 0
            else:
                typed_value = int(self.lineedit_s.text())
                if typed_value <= 0:
                    raise ValueError("input error")
                self.s = typed_value

            self.s_is_valid = True
            self.msg_s.hide()

        except ValueError:
            self.s_is_valid = False
            self.msg_s.setText("Wrong value!")
            self.msg_s.show()

        finally:
            self.validate_form()
