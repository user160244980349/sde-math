from array import array

from sympy import S, symbols, integrate

from mathematics.symbolic.legendre_polynomial import polynomial


def getc(indices: array):
    x, y = symbols('x y')
    n = len(indices)
    c = S(1)

    for i in reversed(range(1, n)):
        c = integrate(polynomial(indices[i], x) * c, (x, -1, y)).subs(y, x)
    c = integrate(polynomial(indices[0], x) * c, (x, -1, 1))

    return c


def getcw(indices: array, weights: array):
    x, y = symbols('x y')
    n = len(indices)
    w = list(reversed(weights))
    c = S(1)

    for i in reversed(range(1, n)):
        c = integrate(polynomial(indices[i], x) * w[i] * c, (x, -1, y)).subs(y, x)
    c = integrate(polynomial(indices[0], x) * w[0] * c, (x, -1, 1))

    return -c
