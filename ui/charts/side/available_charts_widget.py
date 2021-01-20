from PyQt5.QtWidgets import QVBoxLayout, QWidget, QSizePolicy, QSpacerItem, QGroupBox, \
    QScrollArea

from ui.charts.side.item_widget import ItemWidget


class AvailableChartsWidget(QGroupBox):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QGroupBox, self).__init__(parent)

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

    def new_items(self, lines: list):
        self.layout.removeItem(self.spacer)

        for i in range(len(lines)):
            item_widget = ItemWidget(f"{lines[i].name}, [{i}]", parent=self)
            item_widget.uid = lines[i].uid
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
