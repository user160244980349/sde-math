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
    Euler.context(n, m)
    ticks = int((t2 - t1) / dt)

    # Symbols
    y = Euler()
    args = symbols("x1:%d" % (n + 1))
    args_extended = list()
    args_extended.extend(args)
    args_extended.extend([Euler.t, Euler.ksi])

    # Static substitutions
    y = y.subs([(Euler.dt, dt),
                (Euler.yp, Matrix(args)),
                (Euler.dt, dt),
                (Euler.b, mat_b),
                (Euler.a, mat_a)]).doit()

    # Compilation of formula
    yp1_compiled = lambdify(args_extended, y, 'numpy')

    # Substitution values
    t = [t1 + i * dt for i in range(0, ticks)]
    y = zeros((n, ticks))
    y[:, 0] = y0[:, 0]

    # Dynamic substitutions with integration
    for p in range(0, ticks - 1):
        values = list(y[:, p])
        values.extend([t[p], randn(1, m)])
        y[:, p + 1] = yp1_compiled(*values)[:, 0]

    return y, t
