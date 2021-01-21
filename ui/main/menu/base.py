from PyQt5.QtWidgets import QWidget, QSizePolicy, QSpacerItem, QHBoxLayout, QVBoxLayout, QCheckBox, QLabel

from ui.main.info import InfoIcon
from ui.main.menu.linear import LinearGroupWidget
from ui.main.menu.taylor_ito import ItoGroupWidget
from ui.main.menu.taylor_stratonovich import StratonovichGroupWidget


class MainMenuWidget(QWidget):
    """
    Main menu widget
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.charts_check = QCheckBox("Charts window", self)

        icon = InfoIcon("This is charts window checkbox, it will\n"
                        "follow you on every application dialog, so\n"
                        "you can easily open or close window with available charts")

        bar_layout = QHBoxLayout()
        bar_layout.addItem(QSpacerItem(0, 50, QSizePolicy.Expanding, QSizePolicy.Minimum))
        bar_layout.addWidget(icon)
        bar_layout.addWidget(self.charts_check)

        # Ito`s cap
        header = QLabel("Strong Numerical Schemes for Ito SDEs", parent=self)
        font = header.font()
        font.setPointSize(15)
        header.setFont(font)

        icon = InfoIcon("You are now in main menu, you can choose\n"
                        "any scheme to perform modeling")

        header_layout = QHBoxLayout()
        header_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        header_layout.addWidget(icon)
        header_layout.addWidget(header)
        header_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.group3 = LinearGroupWidget(self)
        self.group1 = ItoGroupWidget(self)
        self.group2 = StratonovichGroupWidget(self)

        menu_layout = QHBoxLayout()
        menu_layout.addWidget(self.group1)
        menu_layout.addWidget(self.group2)
        menu_layout.addWidget(self.group3)

        layout = QVBoxLayout()
        layout.addLayout(bar_layout)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        layout.addLayout(header_layout)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        layout.addLayout(menu_layout)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.setLayout(layout)
