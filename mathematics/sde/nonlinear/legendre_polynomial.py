from sympy import Rational, RisingFactorial, Derivative


def polynomial(n: int):
    from sympy.abc import x
    return Rational(1, 2) ** n / RisingFactorial(n) * Derivative((x ** 2 - 1) ** n, x, n)
