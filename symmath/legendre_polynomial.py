from sympy import S, factorial, diff


def polynomial(n, sym):
    return S(1) / S(2) ** S(n) / factorial(n) * diff((sym ** S(2) - S(1)) ** S(n), sym, n)
