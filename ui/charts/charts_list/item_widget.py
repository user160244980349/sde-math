from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton, QWidget, QSizePolicy, QSpacerItem, QHBoxLayout, QLabel, QStyle, \
    QApplication, QCheckBox


class ItemWidget(QWidget):
    """
    Application main window
    """
    on_delete = pyqtSignal(object)
    on_hide = pyqtSignal(int)
    on_show = pyqtSignal(int)

    def __init__(self, name, parent=None):
        super(QWidget, self).__init__(parent)

        self.uid = 0

        btn = QPushButton()
        btn.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogCancelButton))
        btn.clicked.connect(lambda: self.on_delete.emit(self.uid))

        checkbox = QCheckBox(name)
        checkbox.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum))
        checkbox.setChecked(True)
        checkbox.clicked.connect(lambda: self.checkbox_changed())

        layout = QHBoxLayout()
        layout.setStretch(0, 0)
        layout.setSpacing(0)

        layout.addWidget(checkbox)
        layout.addWidget(btn)

        self.setLayout(layout)

    def checkbox_changed(self):
        if self.sender().isChecked():
            self.on_show.emit(self.uid)
        else:
            self.on_hide.emit(self.uid)
