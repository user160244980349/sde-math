from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QSizePolicy, QSpacerItem, QGroupBox


class ItoGroupSignals(QObject):
    show_nonlinear_dialog = pyqtSignal(str)


class ItoGroupWidget(QGroupBox):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QGroupBox, self).__init__(parent)

        self.custom_signals = ItoGroupSignals()
        self.main_window = self.parent().parent().parent()
        self.stack_widget = self.main_window.stack_widget

        btn1 = QPushButton("Euler")
        btn2 = QPushButton("Milstein")
        btn3 = QPushButton("Convergence order 1.5")
        btn4 = QPushButton("Convergence order 2.0")
        btn5 = QPushButton("Convergence order 2.5")
        btn6 = QPushButton("Convergence order 3.0")

        btn1.clicked.connect(lambda: self.custom_signals.show_nonlinear_dialog.emit("Euler"))
        btn2.clicked.connect(lambda: self.custom_signals.show_nonlinear_dialog.emit("Milstein"))
        btn3.clicked.connect(lambda: self.custom_signals.show_nonlinear_dialog.emit("T.-Ito 1.5"))
        btn4.clicked.connect(lambda: self.custom_signals.show_nonlinear_dialog.emit("T.-Ito 2.0"))
        btn5.clicked.connect(lambda: self.custom_signals.show_nonlinear_dialog.emit("T.-Ito 2.5"))
        btn6.clicked.connect(lambda: self.custom_signals.show_nonlinear_dialog.emit("T.-Ito 3.0"))

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)
        layout.addWidget(btn6)

        self.setLayout(layout)

        self.setTitle("Taylor-Ito schemes")
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
