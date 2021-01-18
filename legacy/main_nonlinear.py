#!/usr/bin/env python
import logging
from sys import setrecursionlimit

import numpy as np
import plotly.graph_objects as go
from sympy import Matrix

import config as c
import tools.database as db
from init.init import init
from mathematics.sde.nonlinear.drivers.euler import euler
from mathematics.sde.nonlinear.drivers.milstein import milstein
from mathematics.sde.nonlinear.drivers. \
    strong_taylor_ito_1p5 import strong_taylor_ito_1p5
from mathematics.sde.nonlinear.symbolic.coefficients.c import C


# from mathematics.sde.nonlinear.drivers. \
#     strong_taylor_stratonovich_1p0 import strong_taylor_stratonovich_1p0
# from mathematics.sde.nonlinear.drivers. \
#     strong_taylor_stratonovich_1p5 import strong_taylor_stratonovich_1p5
# from mathematics.sde.nonlinear.drivers. \
#     strong_taylor_stratonovich_2p0 import strong_taylor_stratonovich_2p0
# from mathematics.sde.nonlinear.drivers. \
#     strong_taylor_stratonovich_2p5 import strong_taylor_stratonovich_2p5
# from mathematics.sde.nonlinear.drivers. \
#     strong_taylor_stratonovich_3p0 import strong_taylor_stratonovich_3p0


def main():
    """
    Performs modeling of nonlinear stochastic systems
    """

    logging.basicConfig(level=logging.INFO)
    setrecursionlimit(c.recursion_limit)

    init()

    db.connect(c.database)

    y0 = np.array([
        [1],
        [1.5]
    ])

    m_a = Matrix([
        "-5 * x1",
        "-5 * x2"
    ])

    m_b = Matrix([
        ["0.5 * sin(x1)", "x2"],
        ["x2", "0.5 * cos(x1)"]
    ])

    # m_b = Matrix([
    #     ["1 / (1 + x1**2 * x2 ** 2)", "1 / (1 + x1**2)"],
    #     ["1 / (1 + x2**2)", "1 / (1 + cos(x1)**2)"]
    # ])
    #
    # m_b = Matrix([
    #     ["0.5 * x1 - 0.5 * x2", "0.5 * x2 - 0.5 * x1"],
    #     ["-0.5 * sin(x1) + 0.5 * cos(x2)", "-0.5 * sin(x1) + 0.5 * cos(x2)"]
    # ])
    #
    # m_b = Matrix([
    #     ["sin(2 * x1)", "x2"],
    #     ["x2", "cos(3 * x1)"]
    # ])
    #
    # m_a = Matrix([
    #     "5 * x2 - 5 * x1",
    #     "5 * x1 - 5 * x2"
    # ])
    #
    # m_b = Matrix([
    #     "x1",
    #     "x2"
    # ])

    taylor_low_order = (y0, m_a, m_b, (0, 0.07, 20))
    taylor_higher_orders = (y0, m_a, m_b, 0.1, (0, 0.07, 20))

    C.preload(56, 56, 56, 56, 56)

    fig1 = go.Figure()
    fig2 = go.Figure()

    # Euler
    np.random.seed(703)
    y, t = euler(*taylor_low_order)
    fig1.add_trace(
        go.Scatter(
            x=t, y=np.array(y[0, :]).astype(float),
            mode="lines",
            name="Order 0.5"
        )
    )
    fig2.add_trace(
        go.Scatter(
            x=t, y=np.array(y[1, :]).astype(float),
            mode="lines",
            name="Order 0.5"
        )
    )

    # Taylor 1.0
    np.random.seed(703)
    y, t = milstein(*taylor_higher_orders)
    fig1.add_trace(
        go.Scatter(
            x=t, y=np.array(y[0, :]).astype(float),
            mode="lines",
            name="Order 1.0"
        )
    )
    fig2.add_trace(
        go.Scatter(
            x=t, y=np.array(y[1, :]).astype(float),
            mode="lines",
            name="Order 1.0"
        )
    )

    # Taylor 1.5
    np.random.seed(703)
    y, t = strong_taylor_ito_1p5(*taylor_higher_orders)
    fig1.add_trace(
        go.Scatter(
            x=t, y=np.array(y[0, :]).astype(float),
            mode="lines",
            name="Order 1.5"
        )
    )
    fig2.add_trace(
        go.Scatter(
            x=t, y=np.array(y[1, :]).astype(float),
            mode="lines",
            name="Order 1.5"
        )
    )

    # Taylor 2.0
    # np.random.seed(703)
    # y, t = strong_taylor_ito_2p0(*taylor_higher_orders)
    # fig1.add_trace(
    #     go.Scatter(
    #         x=t, y=np.array(y[0, :]).astype(float),
    #         mode="lines",
    #         name="Order 2.0"
    #     )
    # )
    # fig2.add_trace(
    #     go.Scatter(
    #         x=t, y=np.array(y[1, :]).astype(float),
    #         mode="lines",
    #         name="Order 2.0"
    #     )
    # )

    # Taylor 2.5
    # np.random.seed(703)
    # y, t = strong_taylor_ito_2p5(*taylor_higher_orders)
    # fig1.add_trace(
    #     go.Scatter(
    #         x=t, y=np.array(y[0, :]).astype(float),
    #         mode="lines",
    #         name="Order 2.5"
    #     )
    # )
    # fig2.add_trace(
    #     go.Scatter(
    #         x=t, y=np.array(y[1, :]).astype(float),
    #         mode="lines",
    #         name="Order 2.5"
    #     )
    # )

    # Taylor 3.0
    # np.random.seed(703)
    # y, t = strong_taylor_ito_3p0(*taylor_higher_orders)
    # fig1.add_trace(
    #     go.Scatter(
    #         x=t, y=np.array(y[0, :]).astype(float),
    #         mode="lines",
    #         name="Order 3.0"
    #     )
    # )
    # fig2.add_trace(
    #     go.Scatter(
    #         x=t, y=np.array(y[1, :]).astype(float),
    #         mode="lines",
    #         name="Order 3.0"
    #     )
    # )
    fig1.show()
    fig2.show()

    db.disconnect()


if __name__ == "__main__":
    main()
