from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QSizePolicy, QSpacerItem, QGroupBox


class StratonovichGroupSignals(QObject):

    show_nonlinear_dialog = pyqtSignal(str)


class StratonovichGroupWidget(QGroupBox):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QGroupBox, self).__init__(parent)

        self.stack_widget = self.parent().parent()
        self.main_window = self.parent().parent().parent()
        self.custom_signals = StratonovichGroupSignals()

        btn1 = QPushButton("Convergence order 1.0")
        btn2 = QPushButton("Convergence order 1.5")
        btn3 = QPushButton("Convergence order 2.0")
        btn4 = QPushButton("Convergence order 2.5")
        btn5 = QPushButton("Convergence order 3.0")

        btn1.clicked.connect(lambda: self.custom_signals.show_nonlinear_dialog.emit("T.-Strat. 1.0"))
        btn2.clicked.connect(lambda: self.custom_signals.show_nonlinear_dialog.emit("T.-Strat. 1.5"))
        btn3.clicked.connect(lambda: self.custom_signals.show_nonlinear_dialog.emit("T.-Strat. 2.0"))
        btn4.clicked.connect(lambda: self.custom_signals.show_nonlinear_dialog.emit("T.-Strat. 2.5"))
        btn5.clicked.connect(lambda: self.custom_signals.show_nonlinear_dialog.emit("T.-Strat. 3.0"))

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)

        self.setLayout(layout)

        self.setTitle("Taylor-Stratonovich schemes")
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
