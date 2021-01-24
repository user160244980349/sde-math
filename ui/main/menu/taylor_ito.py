from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QSizePolicy, QSpacerItem, QGroupBox


class ItoGroupWidget(QGroupBox):
    """
    Application main window
    """
    show_nonlinear_dialog = pyqtSignal(int)

    def __init__(self, parent=None):
        super(QGroupBox, self).__init__(parent)

        btn1 = QPushButton("Euler")
        btn2 = QPushButton("Milstein")
        btn3 = QPushButton("Convergence Order 1.5")
        btn4 = QPushButton("Convergence Order 2.0")
        btn5 = QPushButton("Convergence Order 2.5")
        btn6 = QPushButton("Convergence Order 3.0")

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

        self.setTitle("Taylor-Ito Schemes")
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        #  events

        btn1.clicked.connect(lambda: self.show_nonlinear_dialog.emit(0))
        btn2.clicked.connect(lambda: self.show_nonlinear_dialog.emit(1))
        btn3.clicked.connect(lambda: self.show_nonlinear_dialog.emit(2))
        btn4.clicked.connect(lambda: self.show_nonlinear_dialog.emit(3))
        btn5.clicked.connect(lambda: self.show_nonlinear_dialog.emit(4))
        btn6.clicked.connect(lambda: self.show_nonlinear_dialog.emit(5))
