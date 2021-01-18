from PyQt5.QtCore import QThreadPool, QObject, pyqtSignal
from PyQt5.QtWidgets import QStackedWidget, QMainWindow

from init.init import init
from tools.fsys import is_locked
from ui.main.modeling.nonliear.base import NonlinearModelingWidget
from ui.worker import Worker
from ui.charts.charts_window import PlotWindow
from ui.main.greetings import GreetingsWidget
from ui.main.modeling.linear.base import LinearModelingWidget
from ui.main.menu.main_menu import MainMenuWidget
from ui.main.progress.complex_progress_widget import ComplexProgressWidget
from ui.main.progress.simple_progress_widget import SimpleProgressWidget


class MainWindowSignals(QObject):
    main_window_close = pyqtSignal()
    start_simple_progress = pyqtSignal(str)
    stop_simple_progress = pyqtSignal(str)


class MainWindow(QMainWindow):
    """
    Application main window
    """

    def __init__(self):
        super(QMainWindow, self).__init__()

        self.custom_signals = MainWindowSignals()
        self.plot_window = PlotWindow(self)
        self.stack_widget = QStackedWidget(self)

        self.main_menu = MainMenuWidget(self.stack_widget)

        self.main_menu.group1.custom_signals.show_nonlinear_dialog.connect(self.show_nonlinear)
        self.main_menu.group2.custom_signals.show_nonlinear_dialog.connect(self.show_nonlinear)
        self.main_menu.group3.custom_signals.show_linear_dialog.connect(lambda: self.stack_widget.setCurrentIndex(2))

        self.nonlinear_modeling = NonlinearModelingWidget(self.stack_widget)
        self.nonlinear_modeling.custom_signals.show_main_menu.connect(lambda: self.stack_widget.setCurrentIndex(0))
        self.nonlinear_modeling.custom_signals.start_progress.connect(lambda: self.stack_widget.setCurrentIndex(5))

        self.linear_modeling = LinearModelingWidget(self.stack_widget)
        self.linear_modeling.custom_signals.show_main_menu.connect(lambda: self.stack_widget.setCurrentIndex(0))
        self.linear_modeling.custom_signals.start_progress.connect(lambda: self.stack_widget.setCurrentIndex(5))

        self.greetings = GreetingsWidget(self.stack_widget)
        self.greetings.custom_signals.show_main_menu.connect(lambda: self.stack_widget.setCurrentIndex(0))

        self.simple_progress = SimpleProgressWidget(self.stack_widget)
        self.greetings.custom_signals.show_main_menu.connect(lambda: self.stack_widget.setCurrentIndex(0))

        self.complex_progress = ComplexProgressWidget(self.stack_widget)
        self.greetings.custom_signals.show_main_menu.connect(lambda: self.stack_widget.setCurrentIndex(0))

        self.stack_widget.addWidget(self.main_menu)
        self.stack_widget.addWidget(self.nonlinear_modeling)
        self.stack_widget.addWidget(self.linear_modeling)
        self.stack_widget.addWidget(self.greetings)
        self.stack_widget.addWidget(self.simple_progress)
        self.stack_widget.addWidget(self.complex_progress)

        self.setCentralWidget(self.stack_widget)

        self.exec_init()

        self.setWindowTitle("SDE-MATH: software package")
        self.resize(800, 600)
        self.show()

    def closeEvent(self, event):
        self.custom_signals.main_window_close.emit()

    def exec_init(self):
        worker = Worker(init)
        worker.custom_signals.finished.connect(self.init_done)

        self.simple_progress.spin("Observing the database...")
        QThreadPool.globalInstance().start(worker)
        self.stack_widget.setCurrentIndex(4)

    def init_done(self):
        if not is_locked(".welcome.lock"):
            self.stack_widget.setCurrentIndex(3)
        else:
            self.stack_widget.setCurrentIndex(0)
        self.simple_progress.stop()

    def show_nonlinear(self, scheme_id):
        self.stack_widget.setCurrentIndex(1)
        self.nonlinear_modeling.scheme_id = scheme_id

        if scheme_id == "Euler":
            self.nonlinear_modeling.step5.info_c.hide()
            self.nonlinear_modeling.step5.label_c.hide()
            self.nonlinear_modeling.step5.lineedit_c.hide()
        else:
            self.nonlinear_modeling.step5.info_c.show()
            self.nonlinear_modeling.step5.label_c.show()
            self.nonlinear_modeling.step5.lineedit_c.show()
