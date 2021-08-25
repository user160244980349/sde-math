from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow, QSplitter

from ui.charts.side.available_charts_widget import AvailableChartsWidget
from ui.charts.visuals.charts_widget import ChartsWidget


class PlotWindow(QMainWindow):
    """
    Application main window
    """
    charts_show = pyqtSignal()
    charts_hide = pyqtSignal()

    def __init__(self):
        super(QMainWindow, self).__init__()

        self.plot_widget = ChartsWidget(self)
        self.charts_list = AvailableChartsWidget(self)

        splitter = QSplitter()
        splitter.addWidget(self.charts_list)
        splitter.addWidget(self.plot_widget)
        splitter.setContentsMargins(5, 5, 5, 5)
        splitter.setSizes([splitter.width() / 0.85,
                           splitter.width() / 0.15])
        self.setCentralWidget(splitter)

        self.setWindowTitle("SDE-MATH: charts window")
        self.resize(1200, 800)

        self.charts_list.on_show_all.connect(self.plot_widget.show_all)
        self.charts_list.on_hide_all.connect(self.plot_widget.hide_all)
        self.charts_list.on_remove_all.connect(self.plot_widget.delete_all)

    def showEvent(self, event):
        self.charts_show.emit()

    def closeEvent(self, event):
        self.charts_hide.emit()
