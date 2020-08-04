from sympy import Matrix, Symbol, MatrixSymbol, Function, Sum, sqrt


class Euler(Function):
    """
    Euler method
    """
    nargs = 0

    @classmethod
    def context(cls, n, m):
        """
        Function evaluation method
        If i1, i2, q are numbers then evaluation performs
        TODO: greek alphabet
        Parameters
        ----------
            i1 - index
            dt - delta time
            ksi - matrix of independent random variables

        Returns
        -------
            Calculated value or symbolic expression
        """
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
        """
        Function evaluation method
        If i1, i2, q are numbers then evaluation performs
        Important: sum iterators may be messed
        Returns
        -------
            Calculated value or symbolic expression
        """
        from sympy.abc import i
        return cls.yp + cls.a * cls.dt + \
               sqrt(cls.dt) * Sum(Matrix(cls.b[:, i]) * cls.ksi[0, i], (i, 0, cls.m - 1)).doit()
