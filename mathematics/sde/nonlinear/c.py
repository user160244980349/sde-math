import sympy as sp

from .legendre_polynomial import polynomial


def getc(indices: list):
    x, y = sp.symbols('x y')
    n = len(indices)
    c = sp.S.One

    for i in reversed(range(1, n)):
        c = sp.integrate(polynomial(indices[i]) * c, (x, -1, y)).subs(y, x)
    c = sp.integrate(polynomial(indices[0]) * c, (x, -1, 1))

    return c


def getcw(indices: list, weights: list):
    x, y = sp.symbols('x y')
    n = len(indices)
    w = list(reversed(weights))
    c = sp.S.One

    for i in reversed(range(1, n)):
        c = sp.integrate(polynomial(indices[i]) * w[i] * c, (x, -1, y)).subs(y, x)
    c = sp.integrate(polynomial(indices[0]) * w[0] * c, (x, -1, 1))

    return -c
