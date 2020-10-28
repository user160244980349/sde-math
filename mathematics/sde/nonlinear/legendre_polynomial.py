from sympy import Rational, factorial, diff


def polynomial(n: int):
    """
    Returns legendre polynomial in symbolic format
    Parameters
    ==========
    n : int
        degree of polynomial
    Returns
    =======
    sympy.Expr
    """
    from sympy.abc import x
    return Rational(1, 2) ** n / factorial(n) * diff((x ** 2 - 1) ** n, x, n)
