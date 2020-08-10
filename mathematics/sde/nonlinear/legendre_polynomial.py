import sympy as sp


def polynomial(n: int):
    """
    Returns legendre polynomial in symbolic format

    Parameters
    ----------
    n : int
        degree of polynomial
    Returns
    -------
    sympy.Expr
    """
    from sympy.abc import x
    return (sp.Rational(1, 2) ** n / sp.factorial(n) *
            sp.Derivative((x ** 2 - 1) ** n, x, n)).doit()
