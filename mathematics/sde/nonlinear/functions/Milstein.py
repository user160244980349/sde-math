import sympy as sp

from .G import G
from .Io import Io
from .Ioo import Ioo


class Milstein(sp.Function):
    """
    Milstein method with focus on columns
    """
    nargs = 8

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
        i, yp, a, b, q, dt, ksi, dxs = sp.sympify(args)
        m = b.shape[1]
        i1, i2 = sp.symbols('i1 i2')
        return \
            yp[i, 0] + a[i, 0] * dt + \
            sp.Sum(
                b[i, i1] * Io(i1, dt, ksi),
                (i1, 0, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    G(b[:, i1], b[i, i2], dxs) *
                    Ioo(i1, i2, q, dt, ksi),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1))
