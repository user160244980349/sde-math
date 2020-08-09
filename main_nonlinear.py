import numpy as np
import plotly.graph_objects as go
import sympy as sp

import config as c
import init
import mathematics.sde.nonlinear.methods as met
import tools.database as db


def main():
    init.init()
    db.connect(c.database)

    y0 = np.array([[1],
                   [0]])

    mat_a = sp.Matrix(['-5 * x1',
                       '-5 * x2'])

    mat_b = sp.Matrix([['sin(x1)', 'x2'],
                       ['x2', 'cos(x1)']])

    # mat_b = sp.Matrix([['1 / (1 + x1**2 * x2 ** 2)', '1 / (1 + x1**2)'],
    #                    ['1 / (1 + x2**2)', '1 / (1 + cos(x1)**2)']])

    # mat_b = sp.Matrix([['0.5 * x1 - 0.5 * x2', '0.5 * x2 - 0.5 * x1'],
    #                    ['-0.5 * sin(x1) + 0.5 * cos(x2)', '-0.5 * sin(x1) + 0.5 * cos(x2)']])

    # mat_b = sp.Matrix([['sin(2 * x1)', 'x2'],
    #                    ['x2', 'cos(3 * x1)']])

    # mat_a = sp.Matrix(['5 * x2 - 5 * x1',
    #                    '5 * x1 - 5 * x2'])

    # mat_b = sp.Matrix(['x1',
    #                    'x2'])

    euler_args = [y0, mat_a, mat_b, (0, 0.1, 5)]
    milstein_args = [y0, mat_a, mat_b, 40, (0, 0.1, 5)]
    taylor1p5_args = [y0, mat_a, mat_b, 40, 5, (0, 0.1, 5)]
    taylor2p0_args = [y0, mat_a, mat_b, 40, 5, 3, 3, (0, 0.1, 5)]

    # Euler
    np.random.seed(703)
    y1, t = met.euler(*euler_args)

    # Milstein
    np.random.seed(703)
    y2, t = met.milstein(*milstein_args)

    # Taylor 1.5
    np.random.seed(703)
    y3, t = met.taylor1p5(*taylor1p5_args)

    # Taylor 2.0
    np.random.seed(703)
    y4, t = met.taylor2p0(*taylor2p0_args)

    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=t, y=np.array(list(y1[0, :])).astype(float),
                              mode='lines',
                              name="Euler"))
    fig1.add_trace(go.Scatter(x=t, y=np.array(list(y2[0, :])).astype(float),
                              mode='lines',
                              name="Milstein"))
    fig1.add_trace(go.Scatter(x=t, y=np.array(y3[0, :]).astype(float),
                              mode='lines',
                              name="Taylor1.5"))
    fig1.add_trace(go.Scatter(x=t, y=np.array(y4[0, :]).astype(float),
                              mode='lines',
                              name="Taylor2.0"))
    fig1.show()

    db.disconnect()


if __name__ == '__main__':
    main()
