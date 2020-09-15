from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QVBoxLayout, QCheckBox, QComboBox, QDateEdit, QDateTimeEdit, QDial, \
    QDoubleSpinBox, QFontComboBox, QLCDNumber, QLabel, QLineEdit, QProgressBar, QPushButton, QRadioButton, QSlider, \
    QSpinBox, QTimeEdit, QWidget


class MainWindow(QtWidgets.QMainWindow):
    """
    Application main window
    """

    def __init__(self):
        super(MainWindow, self).__init__()

        self.title = "SDE math"
        self.left = 0
        self.top = 0
        self.right = 800
        self.bot = 600

        layout = QVBoxLayout()
        widgets = [QCheckBox,
                   QComboBox,
                   QDateEdit,
                   QDateTimeEdit,
                   QDial,
                   QDoubleSpinBox,
                   QFontComboBox,
                   QLCDNumber,
                   QLabel,
                   QLineEdit,
                   QProgressBar,
                   QPushButton,
                   QRadioButton,
                   QSlider,
                   QSpinBox,
                   QTimeEdit]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.right, self.bot)
        self.center()

    def center(self):
        """
        Centers the window
        """
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
