from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow, QSplitter

from ui.charts.charts_list.available_charts_widget import AvailableChartsWidget
from ui.charts.charts_list.item_widget import ItemWidget
from ui.charts.charts_widget import PlotWidget


class PlotWindowSignals(QObject):

    charts_show = pyqtSignal()
    charts_hide = pyqtSignal()


class PlotWindow(QMainWindow):
    """
    Application main window
    """

    def __init__(self, main_window):
        super(QMainWindow, self).__init__()

        self.custom_signals = PlotWindowSignals()

        main_window.custom_signals.main_window_close.connect(self.close)

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

    def checkbox_changed(self):
        if self.sender().isChecked():
            self.show()
        else:
            self.close()

    def showEvent(self, event):
        self.custom_signals.charts_show.emit()

    def closeEvent(self, event):
        self.custom_signals.charts_hide.emit()
