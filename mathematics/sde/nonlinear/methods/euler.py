from time import time
from numpy import zeros, array
from numpy.random import randn
from sympy import symbols, Matrix
from sympy.utilities.lambdify import lambdify

from mathematics.sde.nonlinear.functions.Euler import Euler


def euler(y0: array, mat_a: Matrix, mat_b: Matrix, times: tuple):
    """
    Performs modeling with Euler method with matrix substitutions in cycle
    Parameters
    ----------
        y0 - initial conditions
        mat_a - matrix a
        mat_b - matrix b
        times - modeling interval

    Returns
    -------
        y - solutions matrix
        t - list of time moments
    """
    # Ranges
    n = mat_b.shape[0]
    m = mat_b.shape[1]
    t1 = times[0]
    dt = times[1]
    t2 = times[2]

    # Defining context
    ticks = int((t2 - t1) / dt)

    # Symbols
    y = Euler(n, m)
    args = symbols("x1:%d" % (n + 1))
    args_extended = list()
    args_extended.extend(args)
    args_extended.extend([y.t, y.ksi])

    # Static substitutions
    tt1 = int(round(time() * 1000))
    y = y.doit().subs([(y.yp, Matrix(args)),
                       (y.dt, dt),
                       (y.b, mat_b),
                       (y.a, mat_a)]).doit()
    tt2 = int(round(time() * 1000))
    print("Sub time: %d" % (tt2 - tt1))

    # Compilation of formulas
    y_compiled = list()
    for tr in range(n):
        y_compiled.append(lambdify(args_extended, y.subs(Euler.i, tr), 'numpy'))

    # Substitution values
    t = [t1 + i * dt for i in range(ticks)]
    y = zeros((n, ticks))
    y[:, 0] = y0[:, 0]

    # Dynamic substitutions with integration
    for p in range(ticks - 1):
        ksi = randn(1, m)
        values = list(y[:, p])
        values.extend([t[p], ksi])
        for tr in range(n):
            y[tr, p + 1] = y_compiled[tr](*values)

    return y, t
