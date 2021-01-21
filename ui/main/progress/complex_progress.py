import logging

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, \
    QListWidget, QLabel, QPushButton, QApplication, QStyle
from pyqtspinner.spinner import WaitingSpinner

from ui.main.progress.log_handler import LogHandler


class ComplexProgressWidget(QWidget):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.spinner = WaitingSpinner(self, radius=5.0, lines=10, line_length=5.0, centerOnParent=False)
        self.list_widget = QListWidget(self)
        self.handler = LogHandler(self.handle_message)

        self.label = QLabel(self)
        font = self.label.font()
        font.setPointSize(15)
        self.label.setFont(font)

        self.back_btn = QPushButton("Ok")
        self.back_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogApplyButton))
        self.back_btn.hide()

        # layout configuration

        spinner_layout = QHBoxLayout()
        spinner_layout.addWidget(self.spinner)
        spinner_layout.addWidget(self.label)
        spinner_layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        bottom_bar = QHBoxLayout()
        bottom_bar.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        bottom_bar.addWidget(self.back_btn)

        layout = QVBoxLayout()
        layout.addLayout(spinner_layout)
        layout.addWidget(self.list_widget)
        layout.addLayout(bottom_bar)

        self.setLayout(layout)

    def handle_message(self, text):
        self.list_widget.addItem(text)
        self.list_widget.scrollToBottom()

    def spin(self, text):
        self.list_widget.clear()
        logging.getLogger().addHandler(self.handler)
        self.back_btn.hide()
        self.spinner.start()
        self.label.setText(text)

    def stop(self, text):
        self.back_btn.show()
        self.list_widget.scrollToBottom()
        self.label.setText(text)
        self.spinner.stop()
        logging.getLogger().removeHandler(self.handler)
