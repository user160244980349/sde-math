import sympy as sp

from mathematics.sde.nonlinear.functions.g import G
from mathematics.sde.nonlinear.functions.ito.i0 import I0
from mathematics.sde.nonlinear.functions.ito.i00 import I00


class Milstein(sp.Function):
    """
    Milstein method
    """
    nargs = 8

    def __new__(cls, *args, **kwargs):
        """
        Creates new Milstein object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i, yp, m_a, m_b, q, dt, ksi, dxs = sp.sympify(args)
        n, m = m_b.shape[0], m_b.shape[1]
        a = sp.MatrixSymbol("a", n, 1)
        b = sp.MatrixSymbol("b", n, m)
        i1, i2 = sp.symbols("i1 i2")

        formula = \
            yp[i, 0] + a[i, 0] * dt + \
            sp.Sum(
                b[i, i1] * I0(i1, dt, ksi),
                (i1, 0, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    G(b[:, i1], b[i, i2], dxs) *
                    I00(i1, i2, q, dt, ksi),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1))

        if m_a.is_Matrix and m_b.is_Matrix:
            return formula.subs([(a, m_a), (b, m_b)])
        else:
            return formula

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        sympy.Expr
        """
        return Milstein(*self.args, **hints)
