from time import time

from numpy import array
from numpy.random import seed
from plotly import graph_objects
from sympy import Matrix

from mathematics.sde.nonlinear.methods.euler import euler


def main():
    seed(0)

    y0 = array([[1],
                [2]])

    mat_a = Matrix(['-5 * x1',
                    '-5 * x2'])

    mat_b = Matrix([['0.1 * x1 - 0.1 * x2', '0.1 * x2 - 0.1 * x1'],
                    ['-0.1 * sin(x1) + 0.1 * cos(x2)', '-0.1 * sin(x1) + 0.1 * cos(x2)']])

    milstein_args = [y0, mat_a, mat_b, 10, (0, 0.001, 1)]
    euler_args = [y0, mat_a, mat_b, (0, 0.001, 1)]

    t1 = int(round(time() * 1000))

    # y, t = taylor(*milstein_args)
    # y, t = milstein(*milstein_args)
    y, t = euler(*euler_args)

    t2 = int(round(time() * 1000))
    print("Solve time: %d" % (t2 - t1))

    fig1 = graph_objects.Figure()
    fig1.add_trace(graph_objects.Scatter(x=t, y=array(list(y[0, :])).astype(float),
                                         mode='lines',
                                         name="component 1"))
    fig1.add_trace(graph_objects.Scatter(x=t, y=array(list(y[1, :])).astype(float),
                                         mode='lines',
                                         name="component 2"))
    fig1.show()


if __name__ == '__main__':
    main()
