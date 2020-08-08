import sympy as sp

from .Io import Io


class Euler(sp.Function):
    """
    Milstein method with focus on columns
    """
    nargs = 2

    i = None

    def __new__(cls, *args, **kwargs):
        """
        Creating method context with sizes of it`s components and symbols

        Parameters
        ----------
            n - a column size
            m - b matrix width
            q - independent random variables dimension size
            dxs - tuple of variables to perform differentiation

        Returns
        -------
            Calculated value or symbolic expression
        """
        obj = super(Euler, cls).__new__(cls, *args, **kwargs)
        n, m = args
        obj.n, obj.m = n, m
        obj.t = sp.Symbol('t')
        obj.dt = sp.Symbol('dt')
        obj.a = sp.MatrixSymbol('a', n, 1)
        obj.b = sp.MatrixSymbol('b', n, m)
        obj.yp = sp.MatrixSymbol('yp', n, 1)
        obj.ksi = sp.MatrixSymbol('ksi', 1, m)
        return obj

    def doit(self, **hints):
        """
        Function evaluation method
        This formula works as it is with symbols such it
        has no limits for it`s components
        Returns
        -------
            Calculated value or symbolic expression
        """
        i1 = sp.symbols('i1')
        return self.yp[self.i, 0] + self.a[self.i, 0] * self.dt + \
               sp.Sum(self.b[self.i, i1] * Io(i1, self.dt, self.ksi), (i1, 0, self.m - 1)).doit()
