from sympy import S, symbols, integrate

from symmath.legendre_polynomial import polynomial

x, y = symbols('x y')


def getc(indices):
    n = len(indices)
    c = S(1)

    for i in reversed(range(1, n)):
        c = integrate(polynomial(indices[i], x) * c, (x, -1, y)).subs(y, x)
    c = integrate(polynomial(indices[0], x) * c, (x, -1, 1))

    return c


def getcw(indices):
    n = len(indices)
    c = S(1)

    for i in reversed(range(1, n)):
        c = integrate(polynomial(indices[i], x) * c, (x, -1, y)).subs(y, x)
    c = integrate(polynomial(indices[0], x) * c, (x, -1, 1))

    return -c


def getcw(indices, weights):
    n = len(indices)
    w = list(reversed(weights))
    c = S(1)

    for i in reversed(range(1, n)):
        c = integrate(polynomial(indices[i], x) * w[i] * c, (x, -1, y)).subs(y, x)
    c = integrate(polynomial(indices[0], x) * w[0] * c, (x, -1, 1))

    return -c
