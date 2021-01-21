import matplotlib.pyplot as plt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QSizePolicy, QFrame, QHBoxLayout, QPushButton, \
    QSpacerItem
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from ui.charts.visuals.toolbar import ToolBar
from ui.main.info import InfoIcon


class ChartsWidget(QFrame):
    """
    Application main window
    """
    hide_label = pyqtSignal(int)
    show_label = pyqtSignal(int)

    def __init__(self, parent=None):
        super(QFrame, self).__init__(parent)

        self.plots = dict()
        self.mode = 0

        self.setFrameStyle(QFrame.StyledPanel)
        self.setStyleSheet("QFrame { background: white; }")

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.mpl_connect('resize_event', self.on_resize)
        self.toolbar = ToolBar(self.canvas, self)

        self.ax = self.figure.add_subplot(111)
        self.ax.grid(axis='both', alpha=.3)
        self.ax.relim(visible_only=True)
        self.ax.autoscale_view()

        self.figure.tight_layout()
        self.canvas.draw()

        self.btn_to_fn = QPushButton("Trajectories")
        self.btn_to_fn.setFlat(True)
        self.btn_to_mx = QPushButton("Means")
        self.btn_to_mx.setFlat(True)
        self.btn_to_dx = QPushButton("Dispersions")
        self.btn_to_dx.setFlat(True)

        toolbar_layout = QHBoxLayout()
        toolbar_layout.setContentsMargins(0, 0, 0, 0)
        toolbar_layout.setSpacing(0)
        toolbar_layout.addItem(QSpacerItem(15, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        toolbar_layout.addWidget(InfoIcon("Click this buttons to switch plot modes\n"
                                          "between trajectories, means and dispersions"))
        toolbar_layout.addItem(QSpacerItem(15, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        toolbar_layout.addWidget(self.btn_to_fn)
        toolbar_layout.addWidget(self.btn_to_mx)
        toolbar_layout.addWidget(self.btn_to_dx)
        toolbar_layout.addWidget(self.toolbar)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addLayout(toolbar_layout)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.btn_to_fn.pressed.connect(self.fn_mode)
        self.btn_to_mx.pressed.connect(self.mx_mode)
        self.btn_to_dx.pressed.connect(self.dx_mode)

    def hide_all(self):
        for f in self.plots.values():
            self.hide_label.emit(f.uid)
            if f.line_fn is not None:
                f.line_fn.set_visible(False)
            if f.line_mx is not None:
                f.line_mx.set_visible(False)
            if f.line_dx is not None:
                f.line_dx.set_visible(False)

    def fn_mode(self):

        self.mode = 0

        self.hide_all()

        for f in self.plots.values():
            if f.line_fn is not None:
                self.show_label.emit(f.uid)
                if f.visible:
                    f.line_fn.set_visible(True)

        self.ax.relim(visible_only=True)
        self.ax.autoscale_view()
        self.canvas.draw()

    def mx_mode(self):

        self.mode = 1

        self.hide_all()

        for f in self.plots.values():
            if f.line_mx is not None:
                self.show_label.emit(f.uid)
                if f.visible:
                    f.line_mx.set_visible(True)

        self.ax.relim(visible_only=True)
        self.ax.autoscale_view()
        self.canvas.draw()

    def dx_mode(self):

        self.mode = 2

        self.hide_all()

        for f in self.plots.values():
            if f.line_dx is not None:
                self.show_label.emit(f.uid)
                if f.visible:
                    f.line_dx.set_visible(True)

        self.ax.relim(visible_only=True)
        self.ax.autoscale_view()
        self.canvas.draw()

    def new_items(self, lines: list):

        for line in lines:
            self.plots[line.uid] = line

        for f in self.plots.values():
            if f.line_fn is None and f.fn is not None:
                f.line_fn = self.ax.plot(f.t, f.fn, linewidth=1, color=f.color)[0]
            if f.line_mx is None and f.mx is not None:
                f.line_mx = self.ax.plot(f.t, f.mx, linewidth=1, color=f.color)[0]
            if f.line_dx is None and f.dx is not None:
                f.line_dx = self.ax.plot(f.t, f.dx, linewidth=1, color=f.color)[0]

        self.hide_all()

        if self.mode == 0:
            self.fn_mode()

        if self.mode == 1:
            self.mx_mode()

        if self.mode == 2:
            self.dx_mode()

        self.ax.relim(visible_only=True)
        self.ax.autoscale_view()
        self.figure.tight_layout()
        self.canvas.draw()

    def delete_item(self, uid: int):
        item = self.plots.pop(uid)
        if item.line_fn is not None:
            item.line_fn.remove()
        if item.line_mx is not None:
            item.line_mx.remove()
        if item.line_dx is not None:
            item.line_dx.remove()

        self.ax.relim(visible_only=True)
        self.ax.autoscale_view()
        self.canvas.draw()

    def hide_item(self, uid: int):
        item = self.plots[uid]
        if item.line_fn is not None:
            item.line_fn.set_visible(False)
        if item.line_mx is not None:
            item.line_mx.set_visible(False)
        if item.line_dx is not None:
            item.line_dx.set_visible(False)
        item.visible = False

        self.ax.relim(visible_only=True)
        self.ax.autoscale_view()
        self.canvas.draw()

    def show_item(self, uid: int):
        item = self.plots[uid]
        if item.line_fn is not None:
            item.line_fn.set_visible(True)
        if item.line_mx is not None:
            item.line_mx.set_visible(True)
        if item.line_dx is not None:
            item.line_dx.set_visible(True)
        item.visible = True

        self.ax.relim(visible_only=True)
        self.ax.autoscale_view()
        self.canvas.draw()

    def on_resize(self, event):
        self.figure.tight_layout()
        self.canvas.draw()
