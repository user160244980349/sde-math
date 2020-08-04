from sympy import Function, Sum, symbols, Symbol, MatrixSymbol

from mathematics.sde.nonlinear.functions.G import G, G2
from mathematics.sde.nonlinear.functions.Io import Io
from mathematics.sde.nonlinear.functions.Ioo import Ioo


class MilsteinS(Function):
    """
    Milstein method with focus on trajectories
    """
    nargs = 0

    @classmethod
    def context(cls, i: int, n: int, m: int, q: int, dxs: tuple):
        """
        Creating method context with sizes of it`s components and symbols
        Parameters
        ----------
            i - trajectory
            n - a column size
            m - b matrix width
            q - independent random variables dimension size
            dxs - tuple of variables to perform differentiation

        Returns
        -------
            Calculated value or symbolic expression
        """
        cls.i = i
        cls.m = m
        cls.n = n
        cls.q = q
        cls.t = Symbol('t')
        cls.dt = Symbol('dt')
        cls.a = MatrixSymbol('a', n, 1)
        cls.b = MatrixSymbol('b', n, m)
        cls.yp = MatrixSymbol('yp', n, 1)
        cls.ksi = MatrixSymbol('ksi', q + 1, m)
        cls.dxs = dxs

    @classmethod
    def eval(cls):
        """
        Function evaluation method
        This formula works as it is with symbols such it
        has no limits for it`s components
        Returns
        -------
            Calculated value or symbolic expression
        """
        i1, i2 = symbols('i1 i2')
        return cls.yp[cls.i, 0] + cls.a[cls.i, 0] * cls.dt + \
               Sum(cls.b[cls.i, i1] * Io(i1, cls.dt, cls.ksi), (i1, 0, cls.m - 1)).doit() + \
               Sum(Sum(G(cls.b[:, i1], cls.b[cls.i, i2], cls.dxs) *
                       Ioo(i1, i2, cls.q, cls.dt, cls.ksi), (i2, 0, cls.m - 1)).doit(), (i1, 0, cls.m - 1)).doit()


class MilsteinC(Function):
    """
    Milstein method with focus on columns
    """
    nargs = 0

    @classmethod
    def context(cls, n: int, m: int, q: int, dxs: tuple):
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
        cls.m = m
        cls.n = n
        cls.q = q
        cls.t = Symbol('t')
        cls.dt = Symbol('dt')
        cls.a = MatrixSymbol('a', n, 1)
        cls.b = MatrixSymbol('b', n, m)
        cls.yp = MatrixSymbol('yp', n, 1)
        cls.ksi = MatrixSymbol('ksi', q + 1, m)
        cls.dxs = dxs

    @classmethod
    def eval(cls):
        """
        Function evaluation method
        This formula works as it is with symbols such it
        has no limits for it`s components
        Returns
        -------
            Calculated value or symbolic expression
        """
        i1, i2 = symbols('i1 i2')
        return cls.yp[:, 0] + cls.a[:, 0] * cls.dt + \
               Sum(cls.b[:, i1] * Io(i1, cls.dt, cls.ksi), (i1, 0, cls.m - 1)).doit() + \
               Sum(Sum(G2(cls.b[:, i1], cls.b[:, i2], cls.dxs) *
                       Ioo(i1, i2, cls.q, cls.dt, cls.ksi), (i2, 0, cls.m - 1)).doit(), (i1, 0, cls.m - 1)).doit()
