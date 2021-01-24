from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QSizePolicy, QSpacerItem, QHBoxLayout, QLabel, QCheckBox, \
    QApplication, QStyle

from tools.fsys import lock, unlock
from ui.main.svg import SVG


class GreetingsWidget(QWidget):
    """
    Application main window
    """
    show_main_menu = pyqtSignal()

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        header = QLabel("Welcome to SDE-MATH Software Package for the Numerical Solution of Systems of Ito SDEs")
        font = header.font()
        font.setPointSize(15)
        header.setAlignment(Qt.AlignJustify)
        header.setWordWrap(True)
        header.setFont(font)

        welcome = QLabel(
            "Exact solutions of Ito SDEs "
            "are known in rare cases. "
            "For this reason, it becomes necessary to construct numerical "
            "methods for Ito SDEs. "
            "Moreover, the problem of numerical solution of Ito SDEs "
            "often occurs even in cases when the exact solution of Ito SDE is known. "
            "This means that in some cases, knowing the exact solution to the Ito "
            "SDE does not allow us to simulate it numerically in a simple way.", self
        )

        font = welcome.font()
        welcome.setFont(font)

        welcome.setAlignment(Qt.AlignJustify)
        welcome.setWordWrap(True)
        welcome.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum))

        check_again = QCheckBox("Do not show again", self)
        next_btn = QPushButton("Ok", self)
        next_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogApplyButton))

        check_again.clicked.connect(self.check_lock)
        next_btn.clicked.connect(lambda: self.show_main_menu.emit())

        controls = QHBoxLayout()
        controls.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        controls.addWidget(check_again)
        controls.addWidget(next_btn)
        controls.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        eq1 = QHBoxLayout()
        eq1.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        eq1.addWidget(SVG("equation1.svg", scale_factor=1.))
        eq1.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        eq2 = QHBoxLayout()
        eq2.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        eq2.addWidget(SVG("equation2.svg", scale_factor=1.))
        eq2.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        column = QVBoxLayout()
        column.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        column.addWidget(header)
        column.addItem(QSpacerItem(0, 15, QSizePolicy.Expanding, QSizePolicy.Minimum))
        column.addLayout(eq1)
        column.addItem(QSpacerItem(0, 15, QSizePolicy.Expanding, QSizePolicy.Minimum))
        column.addLayout(eq2)
        column.addItem(QSpacerItem(0, 15, QSizePolicy.Expanding, QSizePolicy.Minimum))
        column.addWidget(welcome)
        column.addItem(QSpacerItem(0, 30, QSizePolicy.Expanding, QSizePolicy.Minimum))
        column.addLayout(controls)
        column.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        layout = QHBoxLayout()
        layout.addItem(QSpacerItem(50, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(column)
        layout.addItem(QSpacerItem(50, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.setLayout(layout)

    def check_lock(self):
        if self.sender().isChecked():
            lock(".welcome.lock")
        else:
            unlock(".welcome.lock")
