import sympy as sp

from .G import G
from .I0 import I0
from .I00 import I00


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
        i, yp, a, b, q, dt, ksi, dxs = sp.sympify(args)
        m = b.shape[1]
        i1, i2 = sp.symbols('i1 i2')
        return \
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
