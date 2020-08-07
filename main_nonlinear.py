from time import time

from numpy.random import randn
from numpy import array
from numpy.random import seed
from plotly import graph_objects
from sympy import Matrix

import config as c
import tools.database as db
from mathematics.sde.nonlinear.methods.euler import euler
from mathematics.sde.nonlinear.methods.milstein import milstein
from mathematics.sde.nonlinear.methods.taylor1p5 import taylor1p5


def main():
    
    db.connect(c.database)

    y0 = array([[1],
                [0]])

    mat_a = Matrix(['-5 * x1',
                    '-5 * x2'])
    
    mat_b = Matrix([['sin(x1)', 'x2'],
                    ['x2', 'cos(x1)']])

    # mat_b = Matrix([['1 / (1 + x1**2 * x2 ** 2)', '1 / (1 + x1**2)'],
    #                 ['1 / (1 + x2**2)', '1 / (1 + cos(x1)**2)']])

    # mat_b = Matrix([['0.5 * x1 - 0.5 * x2', '0.5 * x2 - 0.5 * x1'],
    #                 ['-0.5 * sin(x1) + 0.5 * cos(x2)', '-0.5 * sin(x1) + 0.5 * cos(x2)']])

    # mat_b = Matrix([['sin(2 * x1)', 'x2'],
    #                 ['x2', 'cos(3 * x1)']])

    # mat_a = Matrix(['5 * x2 - 5 * x1',
    #                 '5 * x1 - 5 * x2'])

    # mat_b = Matrix(['x1',
    #                 'x2'])

    taylor_args = [y0, mat_a, mat_b, 20, 1, (0, 0.1, 5)]
    milstein_args = [y0, mat_a, mat_b, 20, (0, 0.1, 5)]
    euler_args = [y0, mat_a, mat_b, (0, 0.1, 5)]

    # Euler
    t1 = int(round(time() * 1000))
    seed(703)
    y1, t = euler(*euler_args)
    t2 = int(round(time() * 1000))
    print("Euler solve time: %d" % (t2 - t1))

    # Milstein
    t1 = int(round(time() * 1000))
    seed(703)
    y2, t = milstein(*milstein_args)
    t2 = int(round(time() * 1000))
    print("Milstein solve time: %d" % (t2 - t1))

    # Taylor
    t1 = int(round(time() * 1000))
    seed(703)
    y3, t = taylor1p5(*taylor_args)
    t2 = int(round(time() * 1000))
    print("Taylor solve time: %d" % (t2 - t1))

    fig1 = graph_objects.Figure()
    fig1.add_trace(graph_objects.Scatter(x=t, y=array(list(y1[0, :])).astype(float),
                                         mode='lines',
                                         name="Euler"))
    fig1.add_trace(graph_objects.Scatter(x=t, y=array(list(y2[0, :])).astype(float),
                                         mode='lines',
                                         name="Milstein"))
    fig1.add_trace(graph_objects.Scatter(x=t, y=array(list(y3[0, :])).astype(float),
                                         mode='lines',
                                         name="Taylor"))
    fig1.show()
    
    db.disconnect()


if __name__ == '__main__':
    main()
