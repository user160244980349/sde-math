import sympy as sp

from ..G import G
from ..Aj import Aj
from ..Lj import Lj
from ..stratonovich.J1 import J1
from ..stratonovich.J10 import J10
from ..stratonovich.J0 import J0
from ..stratonovich.J01 import J01
from ..stratonovich.J00 import J00
from ..stratonovich.J000 import J000
from ..stratonovich.J0000 import J0000


class StrongTaylorStratonovich2p0(sp.Function):
    """
    Strong Taylor 2.0 method
    """
    nargs = 11

    def __new__(cls, *args, **kwargs):
        """
        Creates new Taylor2p0 object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i, yp, a, b, q, q1, q2, q3, dt, ksi, dxs = sp.sympify(args)
        m = b.shape[1]
        i1, i2, i3, i4 = sp.symbols('i1 i2 i3 i4')
        return \
            yp[i, 0] + Aj(i, a, b, dxs) * dt + \
            sp.Sum(
                b[i, i1] * J0(i1, dt, ksi),
                (i1, 0, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    G(b[:, i1], b[i, i2], dxs) *
                    J00(i1, i2, q, dt, ksi),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1)) + \
            sp.Sum(
                G(b[:, i1], Aj(i, a, b, dxs), dxs) *
                (dt * J0(i1, dt, ksi) + J1(i1, dt, ksi)) -
                Lj(a, b, b[i, i1], dxs) *
                J1(i1, dt, ksi),
                (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs) *
                        J000(i1, i2, i3, q1, dt, ksi),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            dt ** 2 / 2 * Lj(a, b, Aj(i, a, b, dxs), dxs) + \
            sp.Sum(
                sp.Sum(
                    G(b[:, i1], Lj(a, b, b[i, i2], dxs), dxs) *
                    (J10(i1, i2, q2, dt, ksi) - dt * J01(i1, i2, q2, dt, ksi)) -
                    Lj(a, b, G(b[:, i1], b[i, i1], dxs), dxs) * J10(i1, i2, q2, dt, ksi) +
                    G(b[:, i1], G(b[:, i2], Aj(i, a, b, dxs), dxs), dxs) *
                    (J10(i1, i2, q2, dt, ksi) + dt * J00(i1, i2, q, dt, ksi)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            G(b[:, i1], G(b[:, i2], G(b[:, i3], b[i, i4], dxs), dxs), dxs) *
                            J0000(i1, i2, i3, i4, q3, dt, ksi),
                            (i4, 1, m - 1)),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1))
