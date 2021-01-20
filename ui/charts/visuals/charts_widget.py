from pprint import pprint

import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QSizePolicy, QGroupBox
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class PlotWidget(QGroupBox):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QGroupBox, self).__init__(parent)

        self.counter = 0
        self.plots = dict()

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.ax = self.figure.add_subplot(111)
        self.figure.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.1)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

        self.setTitle("Plot")
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

    def new_items(self, lines: list):

        for line in lines:
            self.plots[line.uid] = line

        for f in self.plots.values():
            if f.line2d is None:
                f.line2d = self.ax.plot(f.t, f.y)[0]

        self.canvas.draw()

    def delete_item(self, uid: int):
        line = self.plots.pop(uid).line2d.remove()
        self.canvas.draw()

    def hide_item(self, uid: int):
        self.plots[uid].line2d.set_visible(False)
        self.canvas.draw()

    def show_item(self, uid: int):
        self.plots[uid].line2d.set_visible(True)
        self.canvas.draw()
