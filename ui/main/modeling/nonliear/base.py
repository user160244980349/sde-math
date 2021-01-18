from pprint import pprint

from PyQt5.QtCore import QThreadPool, pyqtSignal, QObject
from PyQt5.QtWidgets import QCheckBox, QPushButton, QStyle, QApplication, QSizePolicy, QHBoxLayout, \
    QSpacerItem, QVBoxLayout, QStackedWidget, QWidget

import numpy as np
from sympy import Matrix

import config
from mathematics.sde.nonlinear.drivers.euler import euler
from mathematics.sde.nonlinear.drivers.milstein import milstein
from mathematics.sde.nonlinear.drivers.strong_taylor_ito_1p5 import strong_taylor_ito_1p5
from mathematics.sde.nonlinear.drivers.strong_taylor_ito_2p0 import strong_taylor_ito_2p0
from mathematics.sde.nonlinear.drivers.strong_taylor_ito_2p5 import strong_taylor_ito_2p5
from mathematics.sde.nonlinear.drivers.strong_taylor_ito_3p0 import strong_taylor_ito_3p0
from mathematics.sde.nonlinear.drivers.strong_taylor_stratonovich_1p0 import strong_taylor_stratonovich_1p0
from mathematics.sde.nonlinear.drivers.strong_taylor_stratonovich_1p5 import strong_taylor_stratonovich_1p5
from mathematics.sde.nonlinear.drivers.strong_taylor_stratonovich_2p0 import strong_taylor_stratonovich_2p0
from mathematics.sde.nonlinear.drivers.strong_taylor_stratonovich_2p5 import strong_taylor_stratonovich_2p5
from mathematics.sde.nonlinear.drivers.strong_taylor_stratonovich_3p0 import strong_taylor_stratonovich_3p0
from mathematics.sde.nonlinear.symbolic.coefficients.c import C
from tools import database
from ui.worker import Worker
from ui.main.modeling.nonliear.step1 import Step1
from ui.main.modeling.nonliear.step2 import Step2
from ui.main.modeling.nonliear.step3 import Step3
from ui.main.modeling.nonliear.step4 import Step4
from ui.main.modeling.nonliear.step5 import Step5


class NonlinearModelingSignals(QObject):
    show_main_menu = pyqtSignal()
    start_progress = pyqtSignal(str)
    stop_progress = pyqtSignal(str)
    draw_chart = pyqtSignal(str, object)


class NonlinearModelingWidget(QWidget):
    """
    Application main window
    """

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        main_window = self.parent().parent()
        self.custom_signals = NonlinearModelingSignals()
        self.page = 0
        self.chart_uid = 0
        self.scheme_id = None
        self.schemes = {
            "Euler": euler,
            "Milstein": milstein,
            "T.-Ito 1.5": strong_taylor_ito_1p5,
            "T.-Ito 2.0": strong_taylor_ito_2p0,
            "T.-Ito 2.5": strong_taylor_ito_2p5,
            "T.-Ito 3.0": strong_taylor_ito_3p0,
            "T.-Strat. 1.0": strong_taylor_stratonovich_1p0,
            "T.-Strat. 1.5": strong_taylor_stratonovich_1p5,
            "T.-Strat. 2.0": strong_taylor_stratonovich_2p0,
            "T.-Strat. 2.5": strong_taylor_stratonovich_2p5,
            "T.-Strat. 3.0": strong_taylor_stratonovich_3p0,
        }

        charts_check = QCheckBox("Charts window", self)
        charts_check.clicked.connect(main_window.plot_window.checkbox_changed)
        main_window.plot_window.custom_signals.charts_show.connect(lambda: charts_check.setChecked(True))
        main_window.plot_window.custom_signals.charts_hide.connect(lambda: charts_check.setChecked(False))
        self.custom_signals.draw_chart.connect(main_window.plot_window.charts_list.new_items)
        self.custom_signals.draw_chart.connect(main_window.plot_window.plot_widget.new_items)

        self.custom_signals.stop_progress.connect(main_window.plot_window.show)

        back_btn = QPushButton("Back", self)
        back_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_ArrowBack))
        back_btn.clicked.connect(self.custom_signals.show_main_menu.emit)
        back_btn.clicked.connect(self.reset_page)

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
        self.run_btn.clicked.connect(self.reset_page)
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

        self.stack_widget.addWidget(self.step1)
        self.stack_widget.addWidget(self.step2)
        self.stack_widget.addWidget(self.step3)
        self.stack_widget.addWidget(self.step4)
        self.stack_widget.addWidget(self.step5)

        layout = QVBoxLayout()
        layout.addLayout(bar_layout)
        layout.addWidget(self.stack_widget)
        layout.addLayout(bottom_bar)

        self.setLayout(layout)

    def next_frame(self):
        self.page += 1

        if self.page == 4:
            self.run_btn.show()
            self.next_step_btn.hide()

        if self.page == 1:
            self.step2.matrix.resize_matrix(int(self.step1.lineedit_n.text()), 1)
            self.step3.matrix.resize_matrix(int(self.step1.lineedit_n.text()), int(self.step1.lineedit_m.text()))
            self.step4.matrix.resize_matrix(int(self.step1.lineedit_n.text()), 1)
            self.prev_step_btn.show()

        self.stack_widget.setCurrentIndex(self.page)

    def prev_frame(self):
        self.page -= 1

        if self.page == 3:
            self.run_btn.hide()
            self.next_step_btn.show()

        if self.page == 0:
            self.prev_step_btn.hide()

        self.stack_widget.setCurrentIndex(self.page)

    def reset_page(self):
        self.page = 0
        self.stack_widget.setCurrentIndex(0)
        self.run_btn.hide()
        self.prev_step_btn.hide()
        self.next_step_btn.show()

    def run_modeling(self):

        worker = Worker(self.routine)
        worker.custom_signals.result.connect(self.on_modeling_finish)

        QThreadPool.globalInstance().start(worker)
        self.custom_signals.start_progress.emit("The modeling is being performed...")

    def routine(self):

        a = Matrix(self.step2.matrix.matrix)
        b = Matrix(self.step3.matrix.matrix)

        x0 = np.ndarray(shape=(self.step4.matrix.size_y, self.step4.matrix.size_x), dtype=float)
        for i in range(self.step4.matrix.size_y):
            for j in range(self.step4.matrix.size_x):
                x0[i][j] = float(self.step4.matrix.matrix[i][j])

        database.connect(config.database)

        if self.scheme_id != "Euler":
            C.preload(56, 56, 56, 56, 56)
            result = self.schemes[self.scheme_id](
                x0, a, b,
                float(self.step5.lineedit_c.text()),
                (float(self.step5.lineedit_t0.text()),
                 float(self.step5.lineedit_dt.text()),
                 float(self.step5.lineedit_t1.text())))
        else:
            result = self.schemes[self.scheme_id](
                x0, a, b,
                (float(self.step5.lineedit_t0.text()),
                 float(self.step5.lineedit_dt.text()),
                 float(self.step5.lineedit_t1.text())))

        database.disconnect()

        return result

    def on_modeling_finish(self, result):
        self.chart_uid += 1
        self.custom_signals.stop_progress.emit("The modeling has been completed!")

        name = f"{self.scheme_id}, " \
               f"t=({self.step5.lineedit_t0.text()}, " \
               f"{self.step5.lineedit_dt.text()}, " \
               f"{self.step5.lineedit_t1.text()})"

        if self.scheme_id != "Euler":
            name = f"{name}, C={self.step5.lineedit_c.text()}"

        self.custom_signals.draw_chart.emit(name, result)
