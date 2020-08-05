from sympy import Function, Sum, Symbol, MatrixSymbol, symbols

from mathematics.sde.nonlinear.functions.G import G
from mathematics.sde.nonlinear.functions.Io import Io
from mathematics.sde.nonlinear.functions.Ioo import Ioo


class Taylor1p5(Function):
    """
    Milstein method with focus on columns
    """
    nargs = 4

    i = Symbol('i')

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
        obj = super(Taylor1p5, cls).__new__(cls, *args, **kwargs)
        n, m, q, dxs = args
        obj.m, obj.n, obj.q, obj.dxs = n, m, q, dxs
        obj.t = Symbol('t')
        obj.dt = Symbol('dt')
        obj.a = MatrixSymbol('a', n, 1)
        obj.b = MatrixSymbol('b', n, m)
        obj.yp = MatrixSymbol('yp', n, 1)
        obj.ksi = MatrixSymbol('ksi', q + 1, m)
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
        i1, i2 = symbols('i1 i2')
        return self.yp[self.i, 0] + self.a[self.i, 0] * self.dt + \
               Sum(self.b[self.i, i1] * Io(i1, self.dt, self.ksi), (i1, 0, self.m - 1)).doit() + \
               Sum(Sum(G(self.b[:, i1], self.b[self.i, i2], self.dxs) *
                       Ioo(i1, i2, self.q, self.dt, self.ksi), (i2, 0, self.m - 1)).doit(), (i1, 0, self.m - 1)).doit()
