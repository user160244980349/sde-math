import logging

import numpy as np
from PyQt5.QtCore import QThreadPool, pyqtSignal
from PyQt5.QtWidgets import QCheckBox, QPushButton, QStyle, QApplication, QSizePolicy, QHBoxLayout, \
    QSpacerItem, QVBoxLayout, QStackedWidget, QWidget, QLabel
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
from ui.async_calls.worker import Worker
from ui.charts.visuals.line import Line
from ui.main.modeling.nonliear.step1 import Step1
from ui.main.modeling.nonliear.step2 import Step2
from ui.main.modeling.nonliear.step3 import Step3
from ui.main.modeling.nonliear.step4 import Step4
from ui.main.modeling.nonliear.step5 import Step5


class NonlinearModelingWidget(QWidget):
    """
    Application main window
    """
    show_main_menu = pyqtSignal()
    start_progress = pyqtSignal(str)
    stop_progress = pyqtSignal(str)
    draw_chart = pyqtSignal(list)

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        # other variables

        self.logger = logging.getLogger(__name__)
        self.scheme_id = 0
        self.schemes = [
            (euler, "Euler", "Euler Scheme"),
            (milstein, "Milstein", "Milstein Scheme"),
            (strong_taylor_ito_1p5, "Taylor-Ito 1.5",
             "Strong Taylor-Ito Scheme with Convergence Order 1.5"),
            (strong_taylor_ito_2p0, "Taylor-Ito 2.0",
             "Strong Taylor-Ito Scheme with Convergence Order 2.0"),
            (strong_taylor_ito_2p5, "Taylor-Ito 2.5",
             "Strong Taylor-Ito Scheme with Convergence Order 2.5"),
            (strong_taylor_ito_3p0, "Taylor-Ito 3.0",
             "Strong Taylor-Ito Scheme with Convergence Order 3.0"),
            (strong_taylor_stratonovich_1p0, "Taylor-Str. 1.0",
             "Strong Taylor-Stratonovich Scheme with Convergence Order 1.0"),
            (strong_taylor_stratonovich_1p5, "Taylor-Str. 1.5",
             "Strong Taylor-Stratonovich Scheme with Convergence Order 1.5"),
            (strong_taylor_stratonovich_2p0, "Taylor-Str. 2.0",
             "Strong Taylor-Stratonovich Scheme with Convergence Order 2.0"),
            (strong_taylor_stratonovich_2p5, "Taylor-Str. 2.5",
             "Strong Taylor-Stratonovich Scheme with Convergence Order 2.5"),
            (strong_taylor_stratonovich_3p0, "Taylor-Str. 3.0",
             "Strong Taylor-Stratonovich Scheme with Convergence Order 3.0"),
        ]

        # widgets creation

        self.stack_widget = QStackedWidget(self)

        self.step1 = Step1()
        self.step2 = Step2()
        self.step3 = Step3()
        self.step4 = Step4()
        self.step5 = Step5()

        back_btn = QPushButton("Back", self)
        back_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_ArrowBack))

        self.charts_check = QCheckBox("Charts window", self)

        # configuring layout

        self.scheme_name = QLabel()
        self.scheme_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

        bar_layout = QHBoxLayout()
        bar_layout.addWidget(back_btn)
        bar_layout.addItem(QSpacerItem(10, 35, QSizePolicy.Minimum, QSizePolicy.Minimum))
        bar_layout.addWidget(self.scheme_name)
        bar_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        bar_layout.addWidget(self.charts_check)

        self.stack_widget.addWidget(self.step1)
        self.stack_widget.addWidget(self.step2)
        self.stack_widget.addWidget(self.step3)
        self.stack_widget.addWidget(self.step4)
        self.stack_widget.addWidget(self.step5)

        layout = QVBoxLayout()
        layout.addLayout(bar_layout)
        layout.addWidget(self.stack_widget)

        self.setLayout(layout)

        # events binding

        back_btn.clicked.connect(self.show_main_menu.emit)
        back_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step1))

        self.step1.next_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step2))
        self.step2.prev_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step1))
        self.step2.next_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step3))
        self.step3.prev_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step2))
        self.step3.next_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step4))
        self.step4.prev_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step3))
        self.step4.next_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step5))
        self.step5.prev_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step4))

        self.step5.run_btn.clicked.connect(lambda: self.run_modeling())
        self.step5.run_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step1))

        self.step1.n_valid.connect(self.step2.matrix.resize_h)
        self.step1.n_valid.connect(self.step3.matrix.resize_h)
        self.step1.n_valid.connect(self.step4.matrix.resize_h)

        self.step1.m_valid.connect(self.step3.matrix.resize_w)

    def set_scheme(self, scheme_id):
        self.scheme_id = scheme_id
        self.scheme_name.setText(self.schemes[scheme_id][2])
        if scheme_id == 0:
            self.step5.count_c(False)
        else:
            self.step5.count_c(True)

    def run_modeling(self):
        self.start_progress.emit("The modeling is being performed...")

        worker = Worker(self.routine)
        worker.signals.result.connect(self.on_modeling_finish)
        worker.signals.error.connect(self.on_modeling_corrupted)
        QThreadPool.globalInstance().start(worker)

    def routine(self):

        scheme = self.schemes[self.scheme_id]

        a = Matrix(self.step2.matrix.m)
        b = Matrix(self.step3.matrix.m)

        x0 = np.ndarray(shape=(self.step4.matrix.rowCount(), self.step4.matrix.columnCount()), dtype=float)
        for i in range(self.step4.matrix.rowCount()):
            for j in range(self.step4.matrix.columnCount()):
                x0[i][j] = float(self.step4.matrix.m[i][j])

        if self.step5.s != 0:
            np.random.seed(self.step5.s)

        database.connect(config.database)

        if self.scheme_id == 0:
            result = scheme[0](
                x0, a, b,
                (self.step5.t0,
                 self.step5.dt,
                 self.step5.t1)
            )
        else:
            C.preload(56, 56, 56, 56, 56)
            result = scheme[0](
                x0, a, b, self.step5.c,
                (self.step5.t0,
                 self.step5.dt,
                 self.step5.t1)
            )

        database.disconnect()

        lines = [Line(f"{scheme[1]}, x{i + 1}",
                      np.array(result[1]).astype(float),
                      np.array(result[0][i, :]).astype(float))
                 for i in range(len(result[0]))]

        return lines

    def on_modeling_finish(self, result):
        self.stop_progress.emit("The modeling has been completed!")
        self.draw_chart.emit(result)

    def on_modeling_corrupted(self, result):

        self.logger.error(result[0])
        self.logger.error(result[1])
        self.logger.error(result[2])

        self.stop_progress.emit("The modeling failed!")
