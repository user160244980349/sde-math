import logging
from pprint import pprint
from time import sleep

from PyQt5.QtCore import QThreadPool, pyqtSignal, QObject
from PyQt5.QtWidgets import QCheckBox, QPushButton, QStyle, QApplication, QSizePolicy, QHBoxLayout, \
    QSpacerItem, QVBoxLayout, QStackedWidget, QWidget

from ui.worker import Worker
from ui.main.modeling.linear.step1 import Step1
from ui.main.modeling.linear.step2 import Step2
from ui.main.modeling.linear.step3 import Step3
from ui.main.modeling.linear.step4 import Step4
from ui.main.modeling.linear.step5 import Step5
from ui.main.modeling.linear.step6 import Step6
from ui.main.modeling.linear.step7 import Step7


class LinearModelingSignals(QObject):

    show_main_menu = pyqtSignal()
    start_progress = pyqtSignal(str)
    stop_progress = pyqtSignal(str)


class LinearModelingWidget(QWidget):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        main_window = self.parent().parent()

        self.custom_signals = LinearModelingSignals()
        self.index = 0

        charts_check = QCheckBox("Charts window", self)
        charts_check.clicked.connect(main_window.plot_window.checkbox_changed)
        main_window.plot_window.custom_signals.charts_show.connect(lambda: charts_check.setChecked(True))
        main_window.plot_window.custom_signals.charts_hide.connect(lambda: charts_check.setChecked(False))

        self.custom_signals.stop_progress.connect(main_window.plot_window.show)

        back_btn = QPushButton("Back", self)
        back_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_ArrowBack))
        back_btn.clicked.connect(self.custom_signals.show_main_menu.emit)

        self.next_step_btn = QPushButton("Next", self)
        self.next_step_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_ArrowForward))
        self.next_step_btn.clicked.connect(self.next_frame)

        self.prev_step_btn = QPushButton("Back", self)
        self.prev_step_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_ArrowBack))
        self.prev_step_btn.clicked.connect(self.prev_frame)
        self.prev_step_btn.hide()

        self.run_btn = QPushButton("Perform modeling", self)
        self.run_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_ArrowForward))
        self.run_btn.clicked.connect(self.run_modeling)
        self.run_btn.hide()

        bottom_bar = QHBoxLayout()
        bottom_bar.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        bottom_bar.addWidget(self.prev_step_btn)
        bottom_bar.addWidget(self.next_step_btn)
        bottom_bar.addWidget(self.run_btn)

        bar_layout = QHBoxLayout()
        bar_layout.addWidget(back_btn)
        bar_layout.addItem(QSpacerItem(0, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))
        bar_layout.addWidget(charts_check)

        self.stack_widget = QStackedWidget(self)

        self.step1 = Step1(self.stack_widget)
        self.step2 = Step2(self.stack_widget)
        self.step3 = Step3(self.stack_widget)
        self.step4 = Step4(self.stack_widget)
        self.step5 = Step5(self.stack_widget)
        self.step6 = Step6(self.stack_widget)
        self.step7 = Step7(self.stack_widget)

        self.stack_widget.addWidget(self.step1)
        self.stack_widget.addWidget(self.step2)
        self.stack_widget.addWidget(self.step3)
        self.stack_widget.addWidget(self.step4)
        self.stack_widget.addWidget(self.step5)
        self.stack_widget.addWidget(self.step6)
        self.stack_widget.addWidget(self.step7)

        layout = QVBoxLayout()
        layout.addLayout(bar_layout)
        layout.addWidget(self.stack_widget)
        layout.addLayout(bottom_bar)

        self.setLayout(layout)

    def next_frame(self):
        self.index += 1

        if self.index == 6:
            self.run_btn.show()
            self.next_step_btn.hide()

        if self.index == 1:
            self.step2.matrix.resize_matrix(int(self.step1.lineedit_n.text()), 1)
            self.step3.matrix.resize_matrix(int(self.step1.lineedit_n.text()), int(self.step1.lineedit_m.text()))
            self.step4.matrix.resize_matrix(int(self.step1.lineedit_n.text()), 1)
            self.step5.matrix.resize_matrix(int(self.step1.lineedit_n.text()), 1)
            self.step6.matrix.resize_matrix(int(self.step1.lineedit_n.text()), 1)
            self.prev_step_btn.show()

        self.stack_widget.setCurrentIndex(self.index)

    def prev_frame(self):
        self.index -= 1

        if self.index == 5:
            self.run_btn.hide()
            self.next_step_btn.show()

        if self.index == 0:
            self.prev_step_btn.hide()

        self.stack_widget.setCurrentIndex(self.index)

    def run_modeling(self):

        worker = Worker(self.modeling_routine)
        worker.custom_signals.finished.connect(self.on_modeling_finish)

        QThreadPool.globalInstance().start(worker)
        self.custom_signals.start_progress.emit("The modeling is being performed...")

    def modeling_routine(self, a, b, times: tuple):

        pprint(a)
        pprint(b)
        pprint(times)

        logger = logging.getLogger(__name__)
        for _ in range(25):
            sleep(0.5)
            logger.info("plotting")

    def on_modeling_finish(self):
        self.custom_signals.stop_progress.emit("The modeling has been performed!")
