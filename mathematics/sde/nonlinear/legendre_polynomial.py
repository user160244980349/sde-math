import sympy as sp


def polynomial(n: int):
    from sympy.abc import x
    return (sp.Rational(1, 2) ** n / sp.factorial(n) *
            sp.Derivative((x ** 2 - 1) ** n, x, n)).doit()
