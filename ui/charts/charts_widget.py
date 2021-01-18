import random

import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QSizePolicy, QGroupBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np


class Line:

    def __init__(self, t, y):
        self.t = t
        self.y = y
        self.line2d = None


class PlotWidget(QGroupBox):
    """
    Application main window
    """

    # constructor
    def __init__(self, parent=None):
        super(QGroupBox, self).__init__(parent)

        self.counter = 0
        self.plots = dict()

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.ax = self.figure.add_subplot()
        self.figure.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.1)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

        self.setTitle("Plot")
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

    def new_items(self, name: str, values: tuple):

        for i in range(len(values[0])):
            self.plots[self.counter] = Line(np.array(values[1]).astype(float),
                                            np.array(values[0][i, :]).astype(float))
            self.counter += 1

        for f in self.plots.values():
            f.line2d = self.ax.plot(f.t, f.y)[0]

        self.canvas.draw()

    def delete_item(self,  uid: int):
        self.plots[uid].line2d.remove()
        self.plots.pop(uid)
        self.canvas.draw()

    def hide_item(self, uid: int):
        self.plots[uid].line2d.set_visible(False)
        self.canvas.draw()

    def show_item(self, uid: int):
        self.plots[uid].line2d.set_visible(True)
        self.canvas.draw()
