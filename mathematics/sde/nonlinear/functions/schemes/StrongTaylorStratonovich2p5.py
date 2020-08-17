import sympy as sp

from mathematics.sde.nonlinear.functions.ajics.sde.nonlinear.functions.G import G

from mathematics.sde.nonlinear.functions.Aj import Aj
from mathematics.sde.nonlinear.functions.L import L
from mathematics.sde.nonlinear.functions.Lj import Lj
from mathematics.sde.nonlinear.functions.coefficients.C import C
from mathematics.sde.nonlinear.functions.stratonovich.J0 import J0
from mathematics.sde.nonlinear.functions.stratonovich.J00 import J00
from mathematics.sde.nonlinear.functions.stratonovich.J000 import J000
from mathematics.sde.nonlinear.functions.stratonovich.J0000 import J0000
from mathematics.sde.nonlinear.functions.stratonovich.J00000 import J00000
from mathematics.sde.nonlinear.functions.stratonovich.J001 import J001
from mathematics.sde.nonlinear.functions.stratonovich.J01 import J01
from mathematics.sde.nonlinear.functions.stratonovich.J010 import J010
from mathematics.sde.nonlinear.functions.stratonovich.J1 import J1
from mathematics.sde.nonlinear.functions.stratonovich.J10 import J10
from mathematics.sde.nonlinear.functions.stratonovich.J100 import J100
from mathematics.sde.nonlinear.functions.stratonovich.J2 import J2


class StrongTaylorStratonovich2p5(sp.Function):
    """
    Strong Taylor 2.0 method
    """
    nargs = 13

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
        i, yp, a, b, q, q1, q2, q3, q4, q5, dt, ksi, dxs = sp.sympify(args)
        m = b.shape[1]

        if isinstance(q1, sp.Number) and isinstance(q2, sp.Number) and isinstance(q3, sp.Number):
            C.preload(int(q1), int(q3), int(q5))

        i1, i2, i3, i4, i5 = sp.symbols("i1 i2 i3 i4 i5")
        aj = Aj(i, a, b, dxs)
        return \
            yp[i, 0] + aj * dt + \
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
                G(b[:, i1], aj, dxs) *
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
            dt ** 2 / 2 * Lj(a, b, aj, dxs) + \
            sp.Sum(
                sp.Sum(
                    G(b[:, i1], Lj(a, b, b[i, i2], dxs), dxs) *
                    (J10(i1, i2, q2, dt, ksi) - J01(i1, i2, q2, dt, ksi)) -
                    Lj(a, b, G(b[:, i1], b[i, i1], dxs), dxs) * J10(i1, i2, q2, dt, ksi) +
                    G(b[:, i1], G(b[:, i2], aj, dxs), dxs) *
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
                (i1, 1, m - 1)) + \
            sp.Sum(G(b[:, i1], Lj(a, b, aj, dxs), dxs) *
                   (J2(i1, dt, ksi) / 2 + dt * J1(i1, dt, ksi) + dt ** 2 / 2 * J0(i1, dt, ksi)) +
                   Lj(a, b, Lj(a, b, b[i, i1], dxs), dxs) * J2(i1, dt, ksi) / 2 -
                   Lj(a, b, G(b[:, i1], aj, dxs), dxs) * (J2(i1, dt, ksi) + dt * J1(i1, dt, ksi)),
                   (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        G(b[:, i1], Lj(a, b, G(b[:, i2], b[i, i1], dxs), dxs), dxs) *
                        (J100(i1, i2, i3, q4, dt, ksi) - J010(i1, i2, i3, q4, dt, ksi)) +
                        G(b[:, i1], G(b[:, i2], Lj(a, b, b[i, i3], dxs), dxs), dxs) *
                        (J010(i1, i2, i3, q4, dt, ksi) - J001(i1, i2, i3, q4, dt, ksi)) +
                        G(b[:, i1], G(b[:, i2], G(b[:, i3], aj, dxs), dxs), dxs) *
                        (dt * J000(i1, i2, i3, q1, dt, ksi) - J001(i1, i2, i3, q4, dt, ksi)) -
                        Lj(a, b, G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs), dxs) *
                        J100(i1, i2, i3, q4, dt, ksi),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            sp.Sum(
                                G(b[:, i1], G(b[:, i2], G(b[:, i3], G(b[:, i4], b[i, i5], dxs), dxs), dxs), dxs) *
                                J00000(i1, i2, i3, i4, i5, q5, dt, ksi),
                                (i5, 1, m - 1)),
                            (i4, 1, m - 1)),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            dt ** 3 / 6 * L(a, b, L(a, b, a[i, 0], dxs), dxs)
