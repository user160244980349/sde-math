from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow, QSplitter

from ui.charts.side.available_charts_widget import AvailableChartsWidget
from ui.charts.visuals.charts_widget import PlotWidget


class PlotWindow(QMainWindow):
    """
    Application main window
    """
    charts_show = pyqtSignal()
    charts_hide = pyqtSignal()

    def __init__(self, main_window):
        super(QMainWindow, self).__init__()

        self.plot_widget = PlotWidget(self)
        self.charts_list = AvailableChartsWidget(self)

        splitter = QSplitter()
        splitter.addWidget(self.charts_list)
        splitter.addWidget(self.plot_widget)
        splitter.setSizes([splitter.width() / 0.75, splitter.width() / 0.25])

        layout = QHBoxLayout(self)
        layout.addWidget(splitter)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("SDE-MATH: charts window")
        self.resize(1200, 800)

    def showEvent(self, event):
        self.charts_show.emit()

    def closeEvent(self, event):
        self.charts_hide.emit()
