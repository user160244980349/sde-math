import logging
from pprint import pprint
from time import sleep

import numpy as np
from PyQt5.QtCore import QThreadPool, pyqtSignal
from PyQt5.QtWidgets import QCheckBox, QPushButton, QStyle, QApplication, QSizePolicy, QHBoxLayout, \
    QSpacerItem, QVBoxLayout, QStackedWidget, QWidget

from mathematics.sde.linear.dindet import dindet
from mathematics.sde.linear.distortions import Symbolic, ComplexDistortion
from mathematics.sde.linear.integration import Integral
from mathematics.sde.linear.stoch import stoch
from ui.async_calls.worker import Worker
from ui.charts.visuals.line import Line
from ui.main.modeling.linear.step1 import Step1
from ui.main.modeling.linear.step2 import Step2
from ui.main.modeling.linear.step3 import Step3
from ui.main.modeling.linear.step4 import Step4
from ui.main.modeling.linear.step5 import Step5
from ui.main.modeling.linear.step6 import Step6
from ui.main.modeling.linear.step7 import Step7
from ui.main.modeling.linear.step8 import Step8


class LinearModelingWidget(QWidget):
    """
    Application main window
    """
    show_main_menu = pyqtSignal()
    start_progress = pyqtSignal(str)
    stop_progress = pyqtSignal(str)
    draw_chart = pyqtSignal(list)

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        # widgets creation

        self.stack_widget = QStackedWidget(self)

        self.step1 = Step1()
        self.step2 = Step2()
        self.step3 = Step3()
        self.step4 = Step4()
        self.step5 = Step5()
        self.step6 = Step6()
        self.step7 = Step7()
        self.step8 = Step8()

        back_btn = QPushButton("Back", self)
        back_btn.setIcon(QApplication.style().standardIcon(QStyle.SP_ArrowBack))

        self.charts_check = QCheckBox("Charts window", self)

        # configuring layout

        bar_layout = QHBoxLayout()
        bar_layout.addWidget(back_btn)
        bar_layout.addItem(QSpacerItem(0, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))
        bar_layout.addWidget(self.charts_check)

        self.stack_widget.addWidget(self.step1)
        self.stack_widget.addWidget(self.step2)
        self.stack_widget.addWidget(self.step3)
        self.stack_widget.addWidget(self.step4)
        self.stack_widget.addWidget(self.step5)
        self.stack_widget.addWidget(self.step6)
        self.stack_widget.addWidget(self.step7)
        self.stack_widget.addWidget(self.step8)

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
        self.step5.next_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step6))
        self.step6.prev_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step5))
        self.step6.next_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step7))
        self.step7.prev_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step6))
        self.step7.next_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step8))
        self.step8.prev_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step7))

        self.step8.run_btn.clicked.connect(lambda: self.run_modeling())
        self.step8.run_btn.clicked.connect(lambda: self.stack_widget.setCurrentWidget(self.step1))

        self.step1.n_valid.connect(self.step2.matrix.resize_h)
        self.step1.n_valid.connect(self.step2.matrix.resize_w)

        self.step1.n_valid.connect(self.step3.matrix.resize_h)
        self.step1.k_valid.connect(self.step3.matrix.resize_w)

        self.step1.n_valid.connect(self.step4.matrix.resize_h)
        self.step1.m_valid.connect(self.step4.matrix.resize_w)

        self.step1.k_valid.connect(self.step5.matrix.resize_h)

        self.step1.n_valid.connect(self.step6.matrix.resize_w)

        self.step1.n_valid.connect(self.step7.matrix.resize_h)

    def run_modeling(self):
        self.start_progress.emit("The modeling is being performed...")

        worker = Worker(self.routine)
        worker.signals.result.connect(self.on_modeling_finish)
        QThreadPool.globalInstance().start(worker)

    def routine(self):

        n = int(self.step1.lineedit_n.text())
        m = int(self.step1.lineedit_m.text())
        k = int(self.step1.lineedit_k.text())
        t0 = float(self.step8.lineedit_t0.text())
        dt = float(self.step8.lineedit_dt.text())
        t1 = float(self.step8.lineedit_t1.text())

        integral = Integral(n)

        integral.k, integral.m, integral.dt, integral.t0, integral.tk = \
            k, m, dt, t0, t1

        integral.m_a = np.array([[float(self.step2.matrix.m[i][j]) for j in range(self.step2.matrix.columnCount())] for i in range(self.step2.matrix.rowCount())])
        integral.mat_b = np.array([[float(self.step3.matrix.m[i][j]) for j in range(self.step3.matrix.columnCount())] for i in range(self.step3.matrix.rowCount())])
        integral.mat_f = np.array([[float(self.step4.matrix.m[i][j]) for j in range(self.step4.matrix.columnCount())] for i in range(self.step4.matrix.rowCount())])
        integral.m_h = np.array([[float(self.step6.matrix.m[i][j]) for j in range(self.step6.matrix.columnCount())] for i in range(self.step6.matrix.rowCount())])
        integral.m_x0 = np.array([[float(self.step7.matrix.m[i][j]) for j in range(self.step7.matrix.columnCount())] for i in range(self.step7.matrix.rowCount())])
        integral.m_mx0 = np.array([[float(self.step7.matrix.m[i][j]) for j in range(self.step7.matrix.columnCount())] for i in range(self.step7.matrix.rowCount())])

        integral.m_dx0 = np.zeros((integral.n, integral.n))
        integral.m_ad, integral.m_bd = dindet(integral.n, integral.k, integral.m_a, integral.mat_b, integral.dt)
        integral.m_fd = stoch(integral.n, integral.m_a, integral.mat_f, integral.dt)

        mat_u = np.array([[object]] * self.step5.matrix.rowCount())
        for i in range(self.step5.matrix.rowCount()):
            mat_u[i][0] = Symbolic(self.step5.matrix.m[i][0])

        integral.distortion = ComplexDistortion(self.step5.matrix.rowCount(), mat_u)
        integral.integrate()

        return integral.m_xt, integral.v_t

    def on_modeling_finish(self, result):
        self.stop_progress.emit("The modeling has been completed!")

        name = f"Linear, " \
               f"t=({self.step8.lineedit_t0.text()}, " \
               f"{self.step8.lineedit_dt.text()}, " \
               f"{self.step8.lineedit_t1.text()})"

        lines = [Line(name,
                      np.array(result[1]).astype(float),
                      np.array(result[0][i, :]).astype(float))
                 for i in range(len(result[0]))]

        self.draw_chart.emit(lines)
