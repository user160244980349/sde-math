import sympy as sp

from mathematics.sde.nonlinear.functions.L import L
from mathematics.sde.nonlinear.functions.coefficients.C import C
from mathematics.sde.nonlinear.functions.ito.I0 import I0
from mathematics.sde.nonlinear.functions.ito.I00 import I00
from mathematics.sde.nonlinear.functions.ito.I000 import I000
from mathematics.sde.nonlinear.functions.ito.I0000 import I0000
from mathematics.sde.nonlinear.functions.ito.I00000 import I00000
from mathematics.sde.nonlinear.functions.ito.I001 import I001
from mathematics.sde.nonlinear.functions.ito.I01 import I01
from mathematics.sde.nonlinear.functions.ito.I010 import I010
from mathematics.sde.nonlinear.functions.ito.I1 import I1
from mathematics.sde.nonlinear.functions.ito.I10 import I10
from mathematics.sde.nonlinear.functions.ito.I100 import I100
from mathematics.sde.nonlinear.functions.ito.I2 import I2


class StrongTaylorIto2p5(sp.Function):
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

        if isinstance(q1, sp.Number) and isinstance(q3, sp.Number) and isinstance(q5, sp.Number):
            C.preload(int(q1), int(q3), int(q5))

        i1, i2, i3, i4, i5 = sp.symbols("i1 i2 i3 i4 i5")
        from mathematics.sde.nonlinear.functions.G import G
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
                (i1, 0, m - 1)) + \
            sp.Sum(
                G(b[:, i1], a[i, 0], dxs) *
                (dt * I0(i1, dt, ksi) + I1(i1, dt, ksi)) -
                L(a, b, b[i, i1], dxs) *
                I1(i1, dt, ksi),
                (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs) *
                        I000(i1, i2, i3, q1, dt, ksi),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            dt ** 2 / 2 * L(a, b, a[i, 0], dxs) + \
            sp.Sum(
                sp.Sum(
                    G(b[:, i1], L(a, b, b[i, i2], dxs), dxs) *
                    (I10(i1, i2, q2, dt, ksi) - I01(i1, i2, q2, dt, ksi)) -
                    L(a, b, G(b[:, i1], b[i, i1], dxs), dxs) * I10(i1, i2, q2, dt, ksi) +
                    G(b[:, i1], G(b[:, i2], a[i, 0], dxs), dxs) *
                    (I10(i1, i2, q2, dt, ksi) + dt * I00(i1, i2, q, dt, ksi)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            G(b[:, i1], G(b[:, i2], G(b[:, i3], b[i, i4], dxs), dxs), dxs) *
                            I0000(i1, i2, i3, i4, q3, dt, ksi),
                            (i4, 1, m - 1)),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            sp.Sum(G(b[:, i1], L(a, b, a[i, 0], dxs), dxs) *
                   (I2(i1, dt, ksi) / 2 + dt * I1(i1, dt, ksi) + dt ** 2 / 2 * I0(i1, dt, ksi)) +
                   L(a, b, L(a, b, b[i, i1], dxs), dxs) * I2(i1, dt, ksi) / 2 -
                   L(a, b, G(b[:, i1], a[i, 0], dxs), dxs) * (I2(i1, dt, ksi) + dt * I1(i1, dt, ksi)),
                   (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        G(b[:, i1], L(a, b, G(b[:, i2], b[i, i1], dxs), dxs), dxs) *
                        (I100(i1, i2, i3, q4, dt, ksi) - I010(i1, i2, i3, q4, dt, ksi)) +
                        G(b[:, i1], G(b[:, i2], L(a, b, b[i, i3], dxs), dxs), dxs) *
                        (I010(i1, i2, i3, q4, dt, ksi) - I001(i1, i2, i3, q4, dt, ksi)) +
                        G(b[:, i1], G(b[:, i2], G(b[:, i3], a[i, 0], dxs), dxs), dxs) *
                        (dt * I000(i1, i2, i3, q1, dt, ksi) - I001(i1, i2, i3, q4, dt, ksi)) -
                        L(a, b, G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs), dxs) *
                        I100(i1, i2, i3, q4, dt, ksi),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            sp.Sum(
                                G(b[:, i1], G(b[:, i2], G(b[:, i3], G(b[:, i4], b[i, i5], dxs), dxs), dxs), dxs) *
                                I00000(i1, i2, i3, i4, i5, q5, dt, ksi),
                                (i5, 1, m - 1)),
                            (i4, 1, m - 1)),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            dt ** 3 / 6 * L(a, b, L(a, b, a[i, 0], dxs), dxs)
