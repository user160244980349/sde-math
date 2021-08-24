from PyQt5.QtCore import QThreadPool, pyqtSignal
from PyQt5.QtWidgets import QStackedWidget, QMainWindow

from init.initialization import initialization
from tools.fsys import is_locked
from ui.async_calls.worker import Worker
from ui.charts.charts_window import PlotWindow
from ui.main.greetings import GreetingsWidget
from ui.main.menu.base import MainMenuWidget
from ui.main.modeling.linear.base import LinearModelingWidget
from ui.main.modeling.nonliear.base import NonlinearModelingWidget
from ui.main.progress.complex_progress import ComplexProgressWidget
from ui.main.progress.simple_progress import SimpleProgressWidget


class MainWindow(QMainWindow):
    """
    Application main window
    """
    main_window_close = pyqtSignal()
    start_simple_progress = pyqtSignal(str)
    stop_simple_progress = pyqtSignal(str)

    def __init__(self):
        super(QMainWindow, self).__init__()

        self.plot_window = PlotWindow()

        self.stack_widget = QStackedWidget(self)

        self.main_menu = MainMenuWidget(self.stack_widget)
        self.complex_progress = ComplexProgressWidget(self.stack_widget)
        self.simple_progress = SimpleProgressWidget(self.stack_widget)
        self.greetings = GreetingsWidget(self.stack_widget)
        self.linear_modeling = LinearModelingWidget(self.stack_widget)
        self.nonlinear_modeling = NonlinearModelingWidget(self.stack_widget)

        self.stack_widget.addWidget(self.main_menu)
        self.stack_widget.addWidget(self.nonlinear_modeling)
        self.stack_widget.addWidget(self.linear_modeling)
        self.stack_widget.addWidget(self.greetings)
        self.stack_widget.addWidget(self.simple_progress)
        self.stack_widget.addWidget(self.complex_progress)

        self.setCentralWidget(self.stack_widget)

        self.exec_init()

        self.setWindowTitle("SDE-MATH: software package")
        self.setMinimumSize(640, 480)
        self.resize(800, 600)
        self.show()

        # stack widget events

        self.main_menu.group1.show_nonlinear_dialog.connect(self.show_nonlinear)
        self.main_menu.group2.show_nonlinear_dialog.connect(self.show_nonlinear)
        self.main_menu.group3.show_linear_dialog.connect(
            lambda: self.stack_widget.setCurrentWidget(self.linear_modeling))

        self.nonlinear_modeling.show_main_menu.connect(
            lambda: self.stack_widget.setCurrentWidget(self.main_menu))
        self.nonlinear_modeling.start_progress.connect(
            lambda: self.stack_widget.setCurrentWidget(self.complex_progress))

        self.linear_modeling.show_main_menu.connect(
            lambda: self.stack_widget.setCurrentWidget(self.main_menu))
        self.linear_modeling.start_progress.connect(
            lambda: self.stack_widget.setCurrentWidget(self.complex_progress))

        self.greetings.show_main_menu.connect(
            lambda: self.stack_widget.setCurrentWidget(self.main_menu))

        self.greetings.show_main_menu.connect(
            lambda: self.stack_widget.setCurrentWidget(self.main_menu))

        self.greetings.show_main_menu.connect(
            lambda: self.stack_widget.setCurrentWidget(self.main_menu))

        self.complex_progress.back_btn.clicked.connect(
            lambda: self.stack_widget.setCurrentWidget(self.main_menu))

        # plot events

        self.main_window_close.connect(self.plot_window.close)

        self.main_menu.charts_check.clicked.connect(self.plot_window.setVisible)
        self.plot_window.charts_show.connect(lambda: self.main_menu.charts_check.setChecked(True))
        self.plot_window.charts_hide.connect(lambda: self.main_menu.charts_check.setChecked(False))

        self.nonlinear_modeling.draw_chart.connect(self.plot_window.charts_list.new_items)
        self.nonlinear_modeling.draw_chart.connect(self.plot_window.plot_widget.new_items)
        self.nonlinear_modeling.draw_chart.connect(self.plot_window.show)

        self.nonlinear_modeling.charts_check.stateChanged.connect(self.plot_window.setVisible)
        self.plot_window.charts_show.connect(lambda: self.nonlinear_modeling.charts_check.setChecked(True))
        self.plot_window.charts_hide.connect(lambda: self.nonlinear_modeling.charts_check.setChecked(False))

        self.linear_modeling.draw_chart.connect(self.plot_window.charts_list.new_items)
        self.linear_modeling.draw_chart.connect(self.plot_window.plot_widget.new_items)
        self.linear_modeling.draw_chart.connect(self.plot_window.show)

        self.linear_modeling.charts_check.clicked.connect(self.plot_window.setVisible)
        self.plot_window.charts_show.connect(lambda: self.linear_modeling.charts_check.setChecked(True))
        self.plot_window.charts_hide.connect(lambda: self.linear_modeling.charts_check.setChecked(False))

        self.linear_modeling.start_progress.connect(self.complex_progress.spin)
        self.nonlinear_modeling.start_progress.connect(self.complex_progress.spin)
        self.linear_modeling.stop_progress.connect(self.complex_progress.stop)
        self.nonlinear_modeling.stop_progress.connect(self.complex_progress.stop)

    def closeEvent(self, event):
        self.main_window_close.emit()

    def exec_init(self):
        self.simple_progress.spin("Preparing the database...")
        self.stack_widget.setCurrentWidget(self.simple_progress)

        worker = Worker(initialization)
        worker.signals.finished.connect(self.init_done)

        QThreadPool.globalInstance().start(worker)

    def init_done(self):
        if not is_locked(".welcome.lock"):
            self.stack_widget.setCurrentWidget(self.greetings)
        else:
            self.stack_widget.setCurrentWidget(self.main_menu)
        self.simple_progress.stop()

    def show_nonlinear(self, scheme_id):
        self.nonlinear_modeling.set_scheme(scheme_id)
        self.stack_widget.setCurrentWidget(self.nonlinear_modeling)
