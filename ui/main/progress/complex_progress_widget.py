import logging

from PyQt5.QtCore import QTimer, QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, \
    QListWidget, QLabel, QPushButton, QApplication, QStyle
from pyqtspinner.spinner import WaitingSpinner

from ui.main.progress.list_widget_handler import LogHandler


class ComplexProgressWidget(QWidget):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.main_window = self.parent().parent()
        self.stack_widget = self.parent().parent().stack_widget
        self.spinner = WaitingSpinner(self, radius=5.0, lines=10, line_length=5.0, centerOnParent=False)
        self.list_widget = QListWidget(self)
        self.handler = LogHandler(self.handle_message)

        self.main_window.linear_modeling.custom_signals.start_progress.connect(self.spin)
        self.main_window.nonlinear_modeling.custom_signals.start_progress.connect(self.spin)
        self.main_window.linear_modeling.custom_signals.stop_progress.connect(self.stop)
        self.main_window.nonlinear_modeling.custom_signals.stop_progress.connect(self.stop)

        self.label = QLabel(self)
        font = self.label.font()
        font.setPointSize(15)
        self.label.setFont(font)

        spinner_layout = QHBoxLayout()
        spinner_layout.addWidget(self.spinner)
        spinner_layout.addWidget(self.label)
        spinner_layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.to_main_menu_btn = QPushButton("Ok")
        self.to_main_menu_btn.clicked.connect(lambda: self.stack_widget.setCurrentIndex(0))
        self.to_main_menu_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogOkButton))
        self.to_main_menu_btn.hide()

        to_main_menu_layout = QHBoxLayout()
        to_main_menu_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        to_main_menu_layout.addWidget(self.to_main_menu_btn)

        layout = QVBoxLayout()
        layout.addLayout(spinner_layout)
        layout.addWidget(self.list_widget)
        layout.addLayout(to_main_menu_layout)

        self.setLayout(layout)

    def handle_message(self, text):
        self.list_widget.addItem(text)
        self.list_widget.scrollToBottom()

    def spin(self, text):
        self.list_widget.clear()

        logging.getLogger().addHandler(self.handler)

        self.to_main_menu_btn.hide()
        self.spinner.start()
        self.label.setText(text)

    def stop(self, text):
        logging.getLogger().removeHandler(self.handler)

        self.to_main_menu_btn.show()
        self.list_widget.scrollToBottom()
        self.label.setText(text)
        self.spinner.stop()

