import sympy as sp

from .G import G
from .Io import Io
from .Ioo import Ioo


class Milstein(sp.Function):
    """
    Milstein method with focus on columns
    """
    nargs = 4

    i = sp.Symbol('i')

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
        obj = super(Milstein, cls).__new__(cls, *args, **kwargs)
        n, m, q, dxs = args
        obj.n, obj.m, obj.q, obj.dxs = n, m, q, dxs
        obj.t = sp.Symbol('t')
        obj.dt = sp.Symbol('dt')
        obj.a = sp.MatrixSymbol('a', n, 1)
        obj.b = sp.MatrixSymbol('b', n, m)
        obj.yp = sp.MatrixSymbol('yp', n, 1)
        obj.ksi = sp.MatrixSymbol('ksi', q + 1, m)
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
        i1, i2 = sp.symbols('i1 i2')
        Io.dt, Io.ksi = self.dt, self.ksi
        return self.yp[self.i, 0] + self.a[self.i, 0] * self.dt + \
               sp.Sum(self.b[self.i, i1] * Io(i1), (i1, 0, self.m - 1)).doit() + \
               sp.Sum(sp.Sum(G(self.b[:, i1], self.b[self.i, i2], self.dxs) *
                             Ioo(i1, i2, self.q, self.dt, self.ksi), (i2, 0, self.m - 1)).doit(),
                      (i1, 0, self.m - 1)).doit()
