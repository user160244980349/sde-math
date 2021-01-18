from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QSizePolicy, QSpacerItem, QGroupBox, \
    QScrollArea

from ui.charts.charts_list.item_widget import ItemWidget


class AvailableChartsWidget(QGroupBox):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QGroupBox, self).__init__(parent)

        self.counter = 0

        self.spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.plot_widget = self.parent().plot_widget

        self.layout = QVBoxLayout()

        scroll_widget = QWidget(self)
        scroll_widget.setLayout(self.layout)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        self.layout.addItem(self.spacer)

        layout = QVBoxLayout()
        layout.addWidget(scroll_area)

        self.setLayout(layout)

        self.setTitle("Series")
        self.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

    def new_items(self, name: str, values: tuple):

        self.layout.removeItem(self.spacer)

        for i in range(len(values[0])):
            item_widget = ItemWidget(f"{name}, [{i}]", parent=self)
            item_widget.uid = self.counter
            self.counter += 1
            item_widget.on_show.connect(self.plot_widget.show_item)
            item_widget.on_hide.connect(self.plot_widget.hide_item)
            item_widget.on_delete.connect(self.plot_widget.delete_item)
            item_widget.on_delete.connect(self.delete_item)

            self.layout.addWidget(item_widget)

        self.layout.addItem(self.spacer)

    def delete_item(self):
        s = self.sender()
        s.setParent(None)
        self.layout.removeWidget(s)
