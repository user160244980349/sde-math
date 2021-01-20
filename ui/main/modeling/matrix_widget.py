from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QSizePolicy


class MatrixWidget(QTableWidget):

    def __init__(self, parent=None):
        super(QTableWidget, self).__init__(parent)

        self.itemChanged.connect(self.item_changed)
        self.m = [["0"]]

        self.setRowCount(1)
        self.setColumnCount(1)
        self.setItem(0, 0, QTableWidgetItem("0"))

        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

    def resize_w(self, w: int):
        old_w = self.columnCount()
        self.setColumnCount(w)
        h = self.rowCount()

        self.m = [[self.m[i][j] if i < h and j < old_w else "0"
                   for j in range(w)]
                  for i in range(h)]

        for i in range(h):
            for j in range(w):
                item = self.item(i, j)
                if item is not None:
                    item.setText(self.m[i][j])
                else:
                    self.setItem(i, j, QTableWidgetItem(self.m[i][j]))

    def resize_h(self, h: int):
        old_h = self.rowCount()
        w = self.columnCount()
        self.setRowCount(h)

        self.m = [[self.m[i][j] if i < old_h and j < w else "0"
                   for j in range(w)]
                  for i in range(h)]

        for i in range(h):
            for j in range(w):
                item = self.item(i, j)
                if item is not None:
                    item.setText(self.m[i][j])
                else:
                    self.setItem(i, j, QTableWidgetItem(self.m[i][j]))

    def item_changed(self, item):
        self.m[item.row()][item.column()] = item.text()
