from sympy import Symbol, MatrixSymbol, Function, Sum, symbols

from mathematics.sde.nonlinear.functions.Io import Io


class Euler(Function):
    """
    Milstein method with focus on columns
    """
    nargs = 2

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
        obj = super(Euler, cls).__new__(cls, *args, **kwargs)
        n, m = args
        obj.m, obj.n = n, m
        obj.t = Symbol('t')
        obj.dt = Symbol('dt')
        obj.a = MatrixSymbol('a', n, 1)
        obj.b = MatrixSymbol('b', n, m)
        obj.yp = MatrixSymbol('yp', n, 1)
        obj.ksi = MatrixSymbol('ksi', 1, m)
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
        i1 = symbols('i1')
        return self.yp[self.i, 0] + self.a[self.i, 0] * self.dt + \
               Sum(self.b[self.i, i1] * Io(i1, self.dt, self.ksi), (i1, 0, self.m - 1)).doit()


class EulerC(Function):
    """
    Milstein method with focus on columns
    """
    nargs = 2

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
        obj = super(EulerC, cls).__new__(cls, *args, **kwargs)
        n, m = args
        obj.m, obj.n = n, m
        obj.t = Symbol('t')
        obj.dt = Symbol('dt')
        obj.a = MatrixSymbol('a', n, 1)
        obj.b = MatrixSymbol('b', n, m)
        obj.yp = MatrixSymbol('yp', n, 1)
        obj.ksi = MatrixSymbol('ksi', 1, m)
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
        i1 = symbols('i1')
        return self.yp[:, 0] + self.a[:, 0] * self.dt + \
               Sum(self.b[:, i1] * Io(i1, self.dt, self.ksi), (i1, 0, self.m - 1)).doit()
