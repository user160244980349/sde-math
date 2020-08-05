from sympy import Rational, factorial, Derivative


def polynomial(n: int):
    from sympy.abc import x
    return (Rational(1, 2) ** n / factorial(n) * Derivative((x ** 2 - 1) ** n, x, n)).doit()
