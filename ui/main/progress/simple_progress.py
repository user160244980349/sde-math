from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QSpacerItem, QSizePolicy
from pyqtspinner.spinner import WaitingSpinner


class SimpleProgressWidget(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.spinner = WaitingSpinner(self, radius=15.0, lines=10, line_length=15.0)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        font = self.label.font()
        font.setPointSize(15)
        self.label.setFont(font)

        # layout configuration

        layout = QVBoxLayout()
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        layout.addWidget(self.spinner)
        layout.addItem(QSpacerItem(0, 50, QSizePolicy.Minimum, QSizePolicy.Minimum))
        layout.addWidget(self.label)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.setLayout(layout)

    def spin(self, text):
        self.spinner.start()
        self.label.setText(text)

    def stop(self):
        self.spinner.stop()
