from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QSizePolicy, QSpacerItem, QGroupBox


class LinearGroupSignals(QObject):

    show_linear_dialog = pyqtSignal()


class LinearGroupWidget(QGroupBox):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QGroupBox, self).__init__(parent)

        self.custom_signals = LinearGroupSignals()

        linear_btn = QPushButton("Dispersion spectral decomposition")
        linear_btn.clicked.connect(lambda: self.custom_signals.show_linear_dialog.emit())

        layout = QVBoxLayout()
        layout.addWidget(linear_btn)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.setLayout(layout)

        self.setTitle("Linear Ito SDEs modeling methods")
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))