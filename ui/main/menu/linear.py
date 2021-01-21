from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QSizePolicy, QSpacerItem, QGroupBox


class LinearGroupWidget(QGroupBox):
    """
    Application main window
    """
    show_linear_dialog = pyqtSignal()

    def __init__(self, parent=None):
        super(QGroupBox, self).__init__(parent)

        linear_btn = QPushButton("Dispersion spectral decomposition")

        # layout configuration

        layout = QVBoxLayout()
        layout.addWidget(linear_btn)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.setLayout(layout)

        self.setTitle("Linear Ito SDEs modeling methods")
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        #  events

        linear_btn.clicked.connect(lambda: self.show_linear_dialog.emit())
