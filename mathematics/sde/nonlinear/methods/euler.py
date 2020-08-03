from numpy import zeros
from numpy.random import randn
from sympy import symbols, Matrix, pprint
from sympy.utilities.lambdify import lambdify

from mathematics.sde.nonlinear.functions.Euler import Euler


def euler(n, m, y0, mat_a, mat_b, first_t, last_t, val_dt):
    # Defining context
    Euler.context(n, m)
    iterations_count = int((last_t - first_t) / val_dt)

    # Symbols
    args = symbols("x1:%d" % (n + 1))
    args_extended = list()
    args_extended.extend(args)
    args_extended.extend([Euler.t, Euler.ksi])

    # Static substitutions
    y_formula = Euler().subs([(Euler.dt, val_dt),
                              (Euler.yp, Matrix(args)),
                              (Euler.dt, val_dt),
                              (Euler.b, mat_b),
                              (Euler.a, mat_a)]).doit()
    pprint(y_formula)

    # Compilation of formula
    yp1_compiled = lambdify(args_extended, y_formula, 'numpy')

    # Substitution values
    t = [first_t + i * val_dt for i in range(0, iterations_count)]
    y = zeros((n, iterations_count))
    y[:, 0] = y0[:, 0]

    # Dynamic substitutions with integration
    for p in range(0, iterations_count - 1):
        values = list(y[:, p])
        values.extend([t[p], randn(1, m)])
        y[:, p + 1] = yp1_compiled(*values)[:, 0]

    return y, t
