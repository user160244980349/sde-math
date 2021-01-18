from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QSizePolicy


class MatrixWidget(QTableWidget):

    def __init__(self, parent=None):
        super(QTableWidget, self).__init__(parent)

        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.itemChanged.connect(self.item_changed)
        self.matrix = None
        self.size_x = 0
        self.size_y = 0

    def resize_matrix(self, h: int, w: int):
        self.setColumnCount(w)
        self.setRowCount(h)

        self.matrix = [[self.matrix[i][j] if i < self.size_y and j < self.size_x else "0"
                        for j in range(w)]
                       for i in range(h)]

        self.size_x = w
        self.size_y = h

        for i in range(self.size_y):
            for j in range(self.size_x):
                item = self.item(i, j)
                if item is not None:
                    item.setText(self.matrix[i][j])
                else:
                    self.setItem(i, j, QTableWidgetItem(self.matrix[i][j]))

    def item_changed(self, item):
        self.matrix[item.row()][item.column()] = item.text()
