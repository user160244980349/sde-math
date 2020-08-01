from sympy import S, Symbol, factorial, diff


def polynomial(n: int, sym: Symbol):
    return S(1) / 2 ** n / factorial(n) * diff((sym ** 2 - 1) ** n, sym, n)
