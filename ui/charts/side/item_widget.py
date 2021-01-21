from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QHBoxLayout, QStyle, \
    QApplication, QCheckBox, QVBoxLayout, QLabel, QSpacerItem, QFrame


class ItemWidget(QFrame):
    """
    Application main window
    """
    on_delete = pyqtSignal(object)
    on_hide = pyqtSignal(int)
    on_show = pyqtSignal(int)

    def __init__(self, name, color, parent=None):
        super(QFrame, self).__init__(parent)

        self.uid = 0

        self.setFrameShape(QFrame.StyledPanel)
        self.setStyleSheet("QFrame { background: white; }")

        checkbox = QCheckBox(name)
        checkbox.setChecked(True)

        btn = QPushButton()
        btn.setFlat(True)
        btn.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogCancelButton))

        underline = QLabel()
        underline.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum))
        underline.setMaximumHeight(3)
        underline.setStyleSheet(f"QLabel {{ background: {color}; }}")

        layout = QHBoxLayout()
        layout.setContentsMargins(3, 3, 3, 3)
        layout.setSpacing(0)
        layout.addWidget(checkbox)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addWidget(btn)

        layout_underlined = QVBoxLayout()
        layout_underlined.setContentsMargins(0, 0, 0, 0)
        layout_underlined.setSpacing(0)
        layout_underlined.addLayout(layout)
        layout_underlined.addWidget(underline)

        self.setLayout(layout_underlined)

        checkbox.stateChanged.connect(self.checkbox_changed)
        btn.clicked.connect(lambda: self.on_delete.emit(self.uid))

    def checkbox_changed(self, v):
        if v > 0:
            self.on_show.emit(self.uid)
        else:
            self.on_hide.emit(self.uid)
