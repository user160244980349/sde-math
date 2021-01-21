from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QSizePolicy, QSpacerItem, QGroupBox


class ItoGroupWidget(QGroupBox):
    """
    Application main window
    """
    show_nonlinear_dialog = pyqtSignal(str)

    def __init__(self, parent=None):
        super(QGroupBox, self).__init__(parent)

        btn1 = QPushButton("Euler")
        btn2 = QPushButton("Milstein")
        btn3 = QPushButton("Convergence order 1.5")
        btn4 = QPushButton("Convergence order 2.0")
        btn5 = QPushButton("Convergence order 2.5")
        btn6 = QPushButton("Convergence order 3.0")

        # layout configuration

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)
        layout.addWidget(btn6)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.setLayout(layout)

        self.setTitle("Taylor-Ito schemes")
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        #  events

        btn1.clicked.connect(lambda: self.show_nonlinear_dialog.emit("Euler"))
        btn2.clicked.connect(lambda: self.show_nonlinear_dialog.emit("Milstein"))
        btn3.clicked.connect(lambda: self.show_nonlinear_dialog.emit("T.-Ito 1.5"))
        btn4.clicked.connect(lambda: self.show_nonlinear_dialog.emit("T.-Ito 2.0"))
        btn5.clicked.connect(lambda: self.show_nonlinear_dialog.emit("T.-Ito 2.5"))
        btn6.clicked.connect(lambda: self.show_nonlinear_dialog.emit("T.-Ito 3.0"))
