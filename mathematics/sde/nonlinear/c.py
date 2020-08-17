import sympy as sp

from mathematics.sde.nonlinear.legendre_polynomial import polynomial


def get_c(indices: tuple, weights: tuple):
    """
    Calculates C coefficient depending on indices and weights

    Parameters
    ----------
    indices : tuple
        indices of coefficient
    weights : tuple
        weights of coefficient
    Returns
    -------
    sympy.Rational
    """
    from sympy.abc import x, y
    n = len(indices)
    w = list(reversed(weights))
    c = sp.S.One

    for i in reversed(range(1, n)):
        c = sp.integrate(polynomial(indices[i]) * (x + 1) ** w[i] * c, (x, -1, y)).subs(y, x)
    c = sp.integrate(polynomial(indices[0]) * (x + 1) ** w[0] * c, (x, -1, 1))

    w = [False if weight != 0 else True for weight in weights]
    if all(w):
        return c
    else:
        return -c
