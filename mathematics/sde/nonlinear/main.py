from plotly import graph_objects
from sympy.abc import j
from sympy import Matrix, MatrixSymbol, Symbol, Sum, sqrt, zeros, pprint
from numpy.random import randn, seed
from numpy import array
from time import time

from mathematics.sde.nonlinear.helpers import filter_args


def main():

    # Ranges
    last_t = 1
    val_dt = 0.001
    iterations_count = int(last_t / val_dt)
    n = 2
    m = 1

    # Symbols
    dt = Symbol('dt')
    t = Symbol('t')
    yp = MatrixSymbol('y', n, 1)
    a = MatrixSymbol('a', n, 1)
    b = MatrixSymbol('b', n, m)
    ksi = MatrixSymbol('ksi', 1, m)

    # Values
    mat_y = zeros(n, iterations_count)
    mat_y[0, 0] = 1
    mat_a = Matrix(['5 * x2 - 5 * x1',
                    '5 * x1 - 5 * x2'])
    mat_b = Matrix([['0.2 * x1'],
                    ['0.2 * x2']])
    mat_ksi = Matrix(randn(iterations_count, m))

    # Formula
    yp1 = yp + a * dt + sqrt(dt) * Sum(b[:, j] * ksi[0, j], (j, 0, m - 1)).doit()
    # pprint(yp1)

    # Static substitutions
    yp1 = yp1.subs([(dt, val_dt)])
    # pprint(yp1)

    # TODO: make dynamic list of a(x, t) and b(x, t)
    args1 = filter_args(mat_a.free_symbols, [t])
    args1.append(t)
    args2 = filter_args(mat_b.free_symbols, [t])
    args2.append(t)
    pprint(args1)
    pprint(args2)

    # Dynamic substitutions with integration
    seed(0)
    t1 = int(round(time() * 1000))
    for i in range(0, iterations_count - 1):
        
        subs_a = list(zip(args1, list(mat_y[:, i])))
        subs_a.append((t, i * val_dt))
        subs_b = list(zip(args2, list(mat_y[:, i])))
        subs_b.append((t, i * val_dt))

        mat_y[:, i + 1] = yp1.subs([(yp, mat_y[:, i]),
                                    (a, mat_a.subs(subs_a)),
                                    (b, mat_b.subs(subs_b)),
                                    (ksi, mat_ksi[i, :])]).as_mutable()

    # pprint(mat_y)
    t2 = int(round(time() * 1000))
    print("%d" % (t2 - t1))

    ts = [i * val_dt for i in range(0, iterations_count)]
    y1 = array(list(mat_y[0, :])).astype(float)
    y2 = array(list(mat_y[1, :])).astype(float)

    fig1 = graph_objects.Figure()
    fig1.add_trace(graph_objects.Scatter(x=ts, y=y1,
                                         mode='lines',
                                         name="component 1"))
    fig1.add_trace(graph_objects.Scatter(x=ts, y=y2,
                                         mode='lines',
                                         name="component 2"))
    fig1.show()


if __name__ == '__main__':
    main()
