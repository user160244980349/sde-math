#!/usr/bin/env python
import logging

import numpy as np
import plotly.graph_objects as go
import sympy as sp

import config as c
import tools.database as db
from init.init import init
from mathematics.sde.nonlinear.schemes.euler import euler
from mathematics.sde.nonlinear.schemes. \
    strong_taylor_stratonovich_1p0 import strong_taylor_stratonovich_1p0
from mathematics.sde.nonlinear.schemes. \
    strong_taylor_stratonovich_1p5 import strong_taylor_stratonovich_1p5
from mathematics.sde.nonlinear.schemes. \
    strong_taylor_stratonovich_2p0 import strong_taylor_stratonovich_2p0
from mathematics.sde.nonlinear.schemes. \
    strong_taylor_stratonovich_2p5 import strong_taylor_stratonovich_2p5
from mathematics.sde.nonlinear.schemes. \
    strong_taylor_stratonovich_3p0 import strong_taylor_stratonovich_3p0
# from mathematics.sde.nonlinear.schemes.milstein import milstein
# from mathematics.sde.nonlinear.schemes. \
#     strong_taylor_ito_1p5 import strong_taylor_ito_1p5
# from mathematics.sde.nonlinear.schemes. \
#     strong_taylor_ito_2p0 import strong_taylor_ito_2p0
# from mathematics.sde.nonlinear.schemes. \
#     strong_taylor_ito_2p5 import strong_taylor_ito_2p5
# from mathematics.sde.nonlinear.schemes. \
#     strong_taylor_ito_3p0 import strong_taylor_ito_3p0


def main():
    """
    Performs modeling of nonlinear stochastic systems
    """

    logging.basicConfig(level=logging.INFO)

    db.connect(c.database)

    init()

    y0 = np.array([
        [1],
        [1.5]
    ])

    m_a = sp.Matrix([
        "-5 * x1",
        "-5 * x2"
    ])

    m_b = sp.Matrix([
        ["0.5 * sin(x1)", "x2"],
        ["x2", "0.5 * cos(x1)"]
    ])

    # m_b = sp.Matrix([
    #     ["1 / (1 + x1**2 * x2 ** 2)", "1 / (1 + x1**2)"],
    #     ["1 / (1 + x2**2)", "1 / (1 + cos(x1)**2)"]
    # ])
    #
    # m_b = sp.Matrix([
    #     ["0.5 * x1 - 0.5 * x2", "0.5 * x2 - 0.5 * x1"],
    #     ["-0.5 * sin(x1) + 0.5 * cos(x2)", "-0.5 * sin(x1) + 0.5 * cos(x2)"]
    # ])
    #
    # m_b = sp.Matrix([
    #     ["sin(2 * x1)", "x2"],
    #     ["x2", "cos(3 * x1)"]
    # ])
    #
    # m_a = sp.Matrix([
    #     "5 * x2 - 5 * x1",
    #     "5 * x1 - 5 * x2"
    # ])
    #
    # m_b = sp.Matrix([
    #     "x1",
    #     "x2"
    # ])

    taylor_low_order = (y0, m_a, m_b, (0, 0.1, 10))
    taylor_higher_orders = (y0, m_a, m_b, 1000, (0, 0.1, 10))

    # Euler
    np.random.seed(703)
    y1, t = euler(*taylor_low_order)

    # Taylor 1.0
    np.random.seed(703)
    y2, t = strong_taylor_stratonovich_1p0(*taylor_higher_orders)

    # Taylor 1.5
    np.random.seed(703)
    y3, t = strong_taylor_stratonovich_1p5(*taylor_higher_orders)

    # Taylor 2.0
    np.random.seed(703)
    y4, t = strong_taylor_stratonovich_2p0(*taylor_higher_orders)

    # Taylor 2.5
    np.random.seed(703)
    y5, t = strong_taylor_stratonovich_2p5(*taylor_higher_orders)

    # Taylor 3.0
    np.random.seed(703)
    y6, t = strong_taylor_stratonovich_3p0(*taylor_higher_orders)

    fig1 = go.Figure()
    fig1.add_trace(
        go.Scatter(
            x=t, y=np.array(y1[1, :]).astype(float),
            mode="lines",
            name="Order 0.5"
        )
    )
    fig1.add_trace(
        go.Scatter(
            x=t, y=np.array(y2[1, :]).astype(float),
            mode="lines",
            name="Order 1.0"
        )
    )
    fig1.add_trace(
        go.Scatter(
            x=t, y=np.array(y3[1, :]).astype(float),
            mode="lines",
            name="Order 1.5"
        )
    )
    fig1.add_trace(
        go.Scatter(
            x=t, y=np.array(y4[1, :]).astype(float),
            mode="lines",
            name="Order 2.0"
        )
    )
    fig1.add_trace(
        go.Scatter(
            x=t, y=np.array(y5[1, :]).astype(float),
            mode="lines",
            name="Order 2.5"
        )
    )
    fig1.add_trace(
        go.Scatter(
            x=t, y=np.array(y6[1, :]).astype(float),
            mode="lines",
            name="Order 3.0"
        )
    )
    fig1.show()

    db.disconnect()


if __name__ == "__main__":
    main()
