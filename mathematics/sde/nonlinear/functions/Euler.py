from sympy import Matrix, Symbol, MatrixSymbol, Function, Sum, sqrt


class Euler(Function):
    nargs = 0

    @classmethod
    def context(cls, n, m):
        cls.m = m
        cls.n = n
        cls.t = Symbol('t')
        cls.dt = Symbol('dt')
        cls.a = MatrixSymbol('a', n, 1)
        cls.b = MatrixSymbol('b', n, m)
        cls.yp = MatrixSymbol('yp', n, 1)
        cls.ksi = MatrixSymbol('ksi', 1, m)

    @classmethod
    def eval(cls):
        from sympy.abc import j
        return cls.yp + cls.a * cls.dt + \
               sqrt(cls.dt) * Sum(Matrix(cls.b[:, j]) * cls.ksi[0, j], (j, 0, cls.m - 1)).doit()
