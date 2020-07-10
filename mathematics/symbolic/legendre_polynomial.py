from sympy import S, factorial, diff


def polynomial(n, sym):
    return S(1) / 2 ** n / factorial(n) * diff((sym ** 2 - 1) ** n, sym, n)
