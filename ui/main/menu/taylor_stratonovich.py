from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QSizePolicy, QSpacerItem, QGroupBox


class StratonovichGroupWidget(QGroupBox):
    """
    Application main window
    """
    show_nonlinear_dialog = pyqtSignal(str)

    def __init__(self, parent=None):
        super(QGroupBox, self).__init__(parent)

        btn1 = QPushButton("Convergence order 1.0")
        btn2 = QPushButton("Convergence order 1.5")
        btn3 = QPushButton("Convergence order 2.0")
        btn4 = QPushButton("Convergence order 2.5")
        btn5 = QPushButton("Convergence order 3.0")

        btn1.setStyleSheet("padding-left: 10px; padding-right: 10px;"
                           "padding-top: 4px; padding-bottom: 4px;")
        btn2.setStyleSheet("padding-left: 10px; padding-right: 10px;"
                           "padding-top: 4px; padding-bottom: 4px;")
        btn3.setStyleSheet("padding-left: 10px; padding-right: 10px;"
                           "padding-top: 4px; padding-bottom: 4px;")
        btn4.setStyleSheet("padding-left: 10px; padding-right: 10px;"
                           "padding-top: 4px; padding-bottom: 4px;")
        btn5.setStyleSheet("padding-left: 10px; padding-right: 10px;"
                           "padding-top: 4px; padding-bottom: 4px;")

        # layout configuration

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.setLayout(layout)

        self.setTitle("Taylor-Stratonovich schemes")
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        #  events

        btn1.clicked.connect(lambda: self.show_nonlinear_dialog.emit("T.-Strat. 1.0"))
        btn2.clicked.connect(lambda: self.show_nonlinear_dialog.emit("T.-Strat. 1.5"))
        btn3.clicked.connect(lambda: self.show_nonlinear_dialog.emit("T.-Strat. 2.0"))
        btn4.clicked.connect(lambda: self.show_nonlinear_dialog.emit("T.-Strat. 2.5"))
        btn5.clicked.connect(lambda: self.show_nonlinear_dialog.emit("T.-Strat. 3.0"))