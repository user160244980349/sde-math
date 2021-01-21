from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QSizePolicy, QSpacerItem, QScrollArea, QLabel, QHBoxLayout, \
    QPushButton, QApplication, QStyle

from ui.charts.side.item_widget import ItemWidget
from ui.main.info import InfoIcon


class AvailableChartsWidget(QWidget):
    """
    Application main window
    """
    on_hide_all = pyqtSignal()
    on_show_all = pyqtSignal()
    on_remove_all = pyqtSignal()

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.items = dict()

        self.spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.plot_widget = self.parent().plot_widget

        remove_all = QPushButton()
        remove_all.setFlat(True)
        remove_all.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogResetButton))

        hide_all = QPushButton("Hide all")
        hide_all.setFlat(True)

        show_all = QPushButton("Show all")
        show_all.setFlat(True)

        header_layout = QHBoxLayout()
        header_layout.addWidget(InfoIcon("Here You will see all modeling series\n"
                                         "You can hide them or delete, if you need to"))
        header_layout.addWidget(QLabel("Series"))
        header_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        header_layout.addWidget(show_all)
        header_layout.addWidget(hide_all)
        header_layout.addWidget(remove_all)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(3, 3, 3, 3)
        self.layout.setSpacing(2)

        scroll_widget = QWidget(self)
        scroll_widget.setLayout(self.layout)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        self.layout.addItem(self.spacer)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(header_layout)
        layout.addWidget(scroll_area)

        self.setLayout(layout)

        self.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

        show_all.clicked.connect(self.show_all)
        hide_all.clicked.connect(self.hide_all)
        remove_all.clicked.connect(self.delete_all)

    def new_items(self, lines: list):
        self.layout.removeItem(self.spacer)

        for i in range(len(lines)):
            item_widget = ItemWidget(f"{lines[i].name}, [{i}]", lines[i].color, parent=self)
            item_widget.uid = lines[i].uid
            item_widget.on_show.connect(self.plot_widget.show_item)
            item_widget.on_hide.connect(self.plot_widget.hide_item)
            item_widget.on_delete.connect(self.plot_widget.delete_item)
            item_widget.on_delete.connect(self.delete_item)
            self.items[lines[i].uid] = item_widget

            self.plot_widget.hide_label.connect(lambda uid: self.items[uid].hide())
            self.plot_widget.show_label.connect(lambda uid: self.items[uid].show())

            self.layout.addWidget(item_widget)

        self.layout.addItem(self.spacer)

    def delete_item(self):
        s = self.sender()
        s.setParent(None)
        self.items.pop(s.uid)
        self.layout.removeWidget(s)

    def delete_all(self):
        for item in self.items.values():
            item.setParent(None)
            self.layout.removeWidget(item)
        self.items.clear()
        self.on_remove_all.emit()

    def hide_all(self):
        for item in self.items.values():
            item.checkbox.blockSignals(True)
            item.checkbox.setChecked(False)
            item.checkbox.blockSignals(False)
        self.on_hide_all.emit()

    def show_all(self):
        for item in self.items.values():
            item.checkbox.blockSignals(True)
            item.checkbox.setChecked(True)
            item.checkbox.blockSignals(False)
        self.on_show_all.emit()
