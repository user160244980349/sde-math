from sympy import S, symbols, integrate

from mathematics.sde.nonlinear.legendre_polynomial import polynomial


def getc(indices: list):
    x, y = symbols('x y')
    n = len(indices)
    c = S(1)

    for i in reversed(range(1, n)):
        c = integrate(polynomial(indices[i]) * c, (x, -1, y)).subs(y, x)
    c = integrate(polynomial(indices[0]) * c, (x, -1, 1))

    return c


def getcw(indices: list, weights: list):
    x, y = symbols('x y')
    n = len(indices)
    w = list(reversed(weights))
    c = S(1)

    for i in reversed(range(1, n)):
        c = integrate(polynomial(indices[i]) * w[i] * c, (x, -1, y)).subs(y, x)
    c = integrate(polynomial(indices[0]) * w[0] * c, (x, -1, 1))

    return -c
