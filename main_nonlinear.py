#!/usr/bin/env python
import numpy as np
import plotly.graph_objects as go
import sympy as sp

import config as c
import tools.database as db
from init import init
from mathematics.sde.nonlinear.schemes.euler import euler
from mathematics.sde.nonlinear.schemes.milstein import milstein
from mathematics.sde.nonlinear.schemes.strong_taylor_ito_1p5 import strong_taylor_ito_1p5
from mathematics.sde.nonlinear.schemes.strong_taylor_ito_2p0 import strong_taylor_ito_2p0
from mathematics.sde.nonlinear.schemes.strong_taylor_ito_2p5 import strong_taylor_ito_2p5
# from mathematics.sde.nonlinear.schemes.strong_taylor_stratonovich_1p0 import strong_taylor_stratonovich_1p0
# from mathematics.sde.nonlinear.schemes.strong_taylor_stratonovich_1p5 import strong_taylor_stratonovich_1p5
# from mathematics.sde.nonlinear.schemes.strong_taylor_stratonovich_2p0 import strong_taylor_stratonovich_2p0
# from mathematics.sde.nonlinear.schemes.strong_taylor_stratonovich_2p5 import strong_taylor_stratonovich_2p5


def main():
    """
    Performs modeling of nonlinear stochastic systems
    """
    init.init()
    db.connect(c.database)

    y0 = np.array([
        [1],
        [0]
    ])

    mat_a = sp.Matrix([
        "-5 * x1",
        "-5 * x2"
    ])

    mat_b = sp.Matrix([
        ["sin(x1)", "x2"],
        ["x2", "cos(x1)"]
    ])

    # mat_b = sp.Matrix([
    #     ["1 / (1 + x1**2 * x2 ** 2)", "1 / (1 + x1**2)"],
    #     ["1 / (1 + x2**2)", "1 / (1 + cos(x1)**2)"]
    # ])
    #
    # mat_b = sp.Matrix([
    #     ["0.5 * x1 - 0.5 * x2", "0.5 * x2 - 0.5 * x1"],
    #     ["-0.5 * sin(x1) + 0.5 * cos(x2)", "-0.5 * sin(x1) + 0.5 * cos(x2)"]
    # ])
    #
    # mat_b = sp.Matrix([
    #     ["sin(2 * x1)", "x2"],
    #     ["x2", "cos(3 * x1)"]
    # ])
    #
    # mat_a = sp.Matrix([
    #     "5 * x2 - 5 * x1",
    #     "5 * x1 - 5 * x2"
    # ])
    #
    # mat_b = sp.Matrix([
    #     "x1",
    #     "x2"
    # ])

    euler_args = [y0, mat_a, mat_b, (0, 0.2, 5)]
    milstein_args = [y0, mat_a, mat_b, 40, (0, 0.2, 5)]
    taylor1p5_args = [y0, mat_a, mat_b, 40, 5, (0, 0.2, 5)]
    taylor2p0_args = [y0, mat_a, mat_b, 40, 5, 3, 3, (0, 0.2, 5)]
    taylor2p5_args = [y0, mat_a, mat_b, 40, 5, 3, 3, 2, 2, (0, 0.2, 5)]

    # Euler
    np.random.seed(703)
    y1, t = euler(*euler_args)

    # Milstein
    np.random.seed(703)
    y2, t = milstein(*milstein_args)

    # Taylor 1.5
    np.random.seed(703)
    y3, t = strong_taylor_ito_1p5(*taylor1p5_args)

    # Taylor 2.0
    np.random.seed(703)
    y4, t = strong_taylor_ito_2p0(*taylor2p0_args)

    # Taylor 2.0
    np.random.seed(703)
    y5, t = strong_taylor_ito_2p5(*taylor2p5_args)

    fig1 = go.Figure()
    fig1.add_trace(
        go.Scatter(
            x=t, y=np.array(y1[0, :]).astype(float),
            mode="lines",
            name="Euler"
        )
    )
    fig1.add_trace(
        go.Scatter(
            x=t, y=np.array(y2[0, :]).astype(float),
            mode="lines",
            name="Milstein"
        )
    )
    fig1.add_trace(
        go.Scatter(
            x=t, y=np.array(y3[0, :]).astype(float),
            mode="lines",
            name="Taylor 1.5"
        )
    )
    fig1.add_trace(
        go.Scatter(
            x=t, y=np.array(y4[0, :]).astype(float),
            mode="lines",
            name="Taylor 2.0"
        )
    )
    fig1.add_trace(
        go.Scatter(
            x=t, y=np.array(y5[0, :]).astype(float),
            mode="lines",
            name="Taylor 2.5"
        )
    )
    fig1.show()

    db.disconnect()


if __name__ == "__main__":
    main()
