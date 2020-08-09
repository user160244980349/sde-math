import sympy as sp

from .G import G
from .Ii import Ii
from .Io import Io
from .Ioo import Ioo
from .Iooo import Iooo
from .L import L


class Taylor1p5(sp.Function):
    """
    Milstein method with focus on columns
    """
    nargs = 9

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
        i, yp, a, b, q, q1, dt, ksi, dxs = sp.sympify(args)
        m = b.shape[1]
        i1, i2, i3 = sp.symbols('i1 i2 i3')
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
                (i1, 0, m - 1)) + \
            sp.Sum(
                G(b[:, i1], a[i, 0], dxs) *
                (dt * Io(i1, dt, ksi) + Ii(i1, dt, ksi)) -
                L(a, b, b[i, i1], dxs) *
                Ii(i1, dt, ksi), (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs) *
                        Iooo(i1, i2, i3, q1, dt, ksi),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            dt ** 2 / 2 * L(a, b, a[i, 0], dxs)
