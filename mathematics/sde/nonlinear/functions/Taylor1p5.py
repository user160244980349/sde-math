from sympy import Function, Sum, Symbol, MatrixSymbol, symbols, pprint

from mathematics.sde.nonlinear.functions.G import G
from mathematics.sde.nonlinear.functions.L import L
from mathematics.sde.nonlinear.functions.Ii import Ii
from mathematics.sde.nonlinear.functions.Io import Io
from mathematics.sde.nonlinear.functions.Ioo import Ioo
from mathematics.sde.nonlinear.functions.Iooo import Iooo


class Taylor1p5(Function):
    """
    Milstein method with focus on columns
    """
    nargs = 5

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
        obj.n, obj.m, obj.q, obj.q1, obj.dxs = args
        obj.t = Symbol('t')
        obj.dt = Symbol('dt')
        obj.a = MatrixSymbol('a', obj.n, 1)
        obj.b = MatrixSymbol('b', obj.n, obj.m)
        obj.yp = MatrixSymbol('yp', obj.n, 1)
        obj.ksi = MatrixSymbol('ksi', obj.q + 1, obj.m)
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
        i1, i2, i3 = symbols('i1 i2 i3')
        return \
            self.yp[self.i, 0] + self.a[self.i, 0] * self.dt + \
            Sum(self.b[self.i, i1] * Io(i1, self.dt, self.ksi),
                (i1, 0, self.m - 1)).doit() + \
            Sum(
                Sum(G(self.b[:, i1], self.b[self.i, i2], self.dxs) *
                    Ioo(i1, i2, self.q, self.dt, self.ksi), (i2, 0, self.m - 1)).doit(),
                (i1, 0, self.m - 1)).doit() + \
            Sum(G(self.b[:, i1], self.a[self.i, 0], self.dxs) *
                (self.dt * Io(i1, self.dt, self.ksi) + Ii(i1, self.dt, self.ksi)) -
                L(self.a, self.b, self.b[self.i, i1], self.dxs) *
                Ii(i1, self.dt, self.ksi), (i1, 1, self.m - 1)).doit() + \
            Sum(
                Sum(
                    Sum(G(self.b[:, i1], G(self.b[:, i2], self.b[self.i, i3], self.dxs), self.dxs) *
                        Iooo(i1, i2, i3, self.q1, self.dt, self.ksi),
                        (i3, 1, self.m - 1)),
                    (i2, 1, self.m - 1)).doit(),
                (i1, 1, self.m - 1)).doit() + \
            self.dt**2 / 2 * L(self.a, self.b, self.a[self.i, 0], self.dxs)