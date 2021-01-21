from PyQt5.QtWidgets import QVBoxLayout, QWidget, QSizePolicy, QSpacerItem, QScrollArea, QLabel, QHBoxLayout

from ui.charts.side.item_widget import ItemWidget
from ui.main.info import InfoIcon


class AvailableChartsWidget(QWidget):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.items = dict()

        self.spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.plot_widget = self.parent().plot_widget

        header_layout = QHBoxLayout()
        header_layout.addWidget(InfoIcon("Here You will see all modeling series\n"
                                         "You can hide them or delete, if you need to"))
        header_layout.addWidget(QLabel("Series"))
        header_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

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
