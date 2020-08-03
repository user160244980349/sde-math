from numpy import zeros
from numpy.random import randn
from sympy import Matrix, symbols, pprint, Symbol
from sympy.utilities.lambdify import lambdify

from mathematics.sde.nonlinear.functions.Milstein import Milstein


def milstein(n, m, y0, mat_a, mat_b, first_t, last_t, val_dt):
    # Ranges
    q = 10
    i = Symbol('i')

    # Defining context
    args = symbols("x1:%d" % (n + 1))
    Milstein.context(i, n, m, q, args)
    iterations_count = int((last_t - first_t) / val_dt)

    # Symbols
    y_formula = Milstein()
    args_extended = list()
    args_extended.extend(args)
    args_extended.extend([Milstein.t, Milstein.ksi])

    # Static substitutions
    y_formula = y_formula.subs([(Milstein.yp, Matrix(args)),
                                (Milstein.b, mat_b),
                                (Milstein.a, mat_a),
                                (Milstein.dt, val_dt)]).doit()
    pprint(y_formula.doit())

    # Compilation of formulas
    mil_compiled = list()
    for tr in range(n):
        mil_compiled.append(lambdify(args_extended, y_formula.subs(i, tr).doit().evalf(), modules="sympy"))

    # Substitution values
    t = [first_t + i * val_dt for i in range(0, iterations_count)]
    y = zeros((n, iterations_count))
    y[:, 0] = y0[:, 0]

    # Dynamic substitutions with integration
    for p in range(iterations_count - 1):
        for tr in range(n):
            values = list(y[:, p])
            values.extend([t[p], randn(q, m)])
            y[tr, p + 1] = mil_compiled[tr](*values)

    return y, t
