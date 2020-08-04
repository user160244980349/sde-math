from numpy import zeros, array
from numpy.random import randn
from sympy import Matrix, symbols, Symbol
from sympy.utilities.lambdify import lambdify

from mathematics.sde.nonlinear.functions.Milstein import MilsteinS, MilsteinC


def milstein_s(y0: array, mat_a: Matrix, mat_b: Matrix, q: int, times: tuple):
    """
    Performs modeling with Milstein method with scalar substitutions in cycle
    Parameters
    ----------
        y0 - initial conditions
        mat_a - matrix a
        mat_b - matrix b
        q - amount of independent random variables
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
    i = Symbol('i')
    args = symbols("x1:%d" % (n + 1))
    MilsteinS.context(i, n, m, q, args)
    ticks = int((t2 - t1) / dt)

    # Symbols
    y = MilsteinS()
    args_extended = list()
    args_extended.extend(args)
    args_extended.extend([MilsteinS.t, MilsteinS.ksi])

    # Static substitutions
    y = y.subs([(MilsteinS.yp, Matrix(args)),
                (MilsteinS.b, mat_b),
                (MilsteinS.a, mat_a),
                (MilsteinS.dt, dt)]).doit()

    # Compilation of formulas
    y_compiled = list()
    for tr in range(n):
        y_compiled.append(lambdify(args_extended, y.subs(i, tr), 'numpy'))

    # Substitution values
    t = [t1 + i * dt for i in range(0, ticks)]
    y = zeros((n, ticks))
    y[:, 0] = y0[:, 0]

    # Dynamic substitutions with integration
    for p in range(ticks - 1):
        ksi = randn(q + 1, m)
        values = list(y[:, p])
        values.extend([t[p], ksi])
        for tr in range(n):
            y[tr, p + 1] = y_compiled[tr](*values)

    return y, t


def milstein_c(y0: array, mat_a: Matrix, mat_b: Matrix, q: int, times: tuple):
    """
    Performs modeling with Milstein method with matrix substitutions in cycle
    Parameters
    ----------
        y0 - initial conditions
        mat_a - matrix a
        mat_b - matrix b
        q - amount of independent random variables
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
    args = symbols("x1:%d" % (n + 1))
    MilsteinC.context(n, m, q, args)
    ticks = int((t2 - t1) / dt)

    # Symbols
    y = MilsteinC()
    args_extended = list()
    args_extended.extend(args)
    args_extended.extend([MilsteinC.t, MilsteinC.ksi])

    # Static substitutions
    y = y.subs([(MilsteinC.yp, Matrix(args)),
                (MilsteinC.b, mat_b),
                (MilsteinC.a, mat_a),
                (MilsteinC.dt, dt)]).doit()

    # Compilation of formulas
    mil_compiled = lambdify(args_extended, y, 'numpy')

    # Substitution values
    t = [t1 + i * dt for i in range(0, ticks)]
    y = zeros((n, ticks))
    y[:, 0] = y0[:, 0]

    # Dynamic substitutions with integration
    for p in range(ticks - 1):
        values = list(y[:, p])
        values.extend([t[p], randn(q + 1, m)])
        y[:, p + 1] = mil_compiled(*values)[:, 0]

    return y, t
