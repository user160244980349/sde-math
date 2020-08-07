from time import time
from numpy import zeros, array
from numpy.random import randn
from sympy import Matrix, symbols, pprint
from sympy.utilities.lambdify import lambdify

from mathematics.sde.nonlinear.functions.Taylor1p5 import Taylor1p5


def taylor1p5(y0: array, mat_a: Matrix, mat_b: Matrix, q: int, q1: int, times: tuple):
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
    args = symbols("x1:%d" % (n + 1))
    ticks = int((t2 - t1) / dt)

    # Symbols
    y = Taylor1p5(n, m, q, q1, args)
    args_extended = list()
    args_extended.extend(args)
    args_extended.extend([y.t, y.ksi])
    
    # pprint(y.subs([
    #     (y.yp, Matrix(args)),
    #     (y.b, mat_b),
    #     (y.a, mat_a),
    #     (y.dt, dt)
    # ]))

    # Static substitutions
    tt1 = int(round(time() * 1000))
    y = y.doit().subs([(y.yp, Matrix(args)),
                       (y.b, mat_b),
                       (y.a, mat_a),
                       (y.dt, dt)]).doit()
    tt2 = int(round(time() * 1000))
    print("Sub time: %d" % (tt2 - tt1))

    # Compilation of formulas
    y_compiled = list()
    for tr in range(n):
        y_compiled.append(lambdify(args_extended, y.subs(Taylor1p5.i, tr).doit(), 'numpy'))

    print('\nTR0-----------------------------------------')
    pprint(y.subs(Taylor1p5.i, 0).doit())
    print('\nTR1-----------------------------------------')
    pprint(y.subs(Taylor1p5.i, 1).doit())

    # Substitution values
    t = [t1 + i * dt for i in range(ticks)]
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

