from sympy import S, integrate

from mathematics.sde.nonlinear.legendre_polynomial import polynomial


def get_c(indices: tuple, weights: tuple):
    """
    Calculates C coefficient depending on indices and weights
    Parameters
    ==========
    indices : tuple
        indices of coefficient
    weights : tuple
        weights of coefficient
    Returns
    =======
    sympy.Rational
    """
    from sympy.abc import x, y
    n = len(indices)
    w = list(reversed(weights))
    c = S.One

    for i in reversed(range(1, n)):
        c = integrate(polynomial(indices[i]) * (x + 1) ** w[i] * c, (x, -1, y)).subs(y, x)
    c = integrate(polynomial(indices[0]) * (x + 1) ** w[0] * c, (x, -1, 1))

    if sum(w) % 2 == 0:
        return c
    else:
        return -c
