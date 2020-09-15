import sympy as sp

from mathematics.sde.nonlinear.functions.aj import Aj
from mathematics.sde.nonlinear.functions.g import G
from mathematics.sde.nonlinear.functions.lj import Lj
from mathematics.sde.nonlinear.functions.stratonovich.j0 import J0
from mathematics.sde.nonlinear.functions.stratonovich.j00 import J00
from mathematics.sde.nonlinear.functions.stratonovich.j000 import J000
from mathematics.sde.nonlinear.functions.stratonovich.j0000 import J0000
from mathematics.sde.nonlinear.functions.stratonovich.j00000 import J00000
from mathematics.sde.nonlinear.functions.stratonovich.j000000 import J000000
from mathematics.sde.nonlinear.functions.stratonovich.j0001 import J0001
from mathematics.sde.nonlinear.functions.stratonovich.j001 import J001
from mathematics.sde.nonlinear.functions.stratonovich.j0010 import J0010
from mathematics.sde.nonlinear.functions.stratonovich.j01 import J01
from mathematics.sde.nonlinear.functions.stratonovich.j010 import J010
from mathematics.sde.nonlinear.functions.stratonovich.j0100 import J0100
from mathematics.sde.nonlinear.functions.stratonovich.j02 import J02
from mathematics.sde.nonlinear.functions.stratonovich.j1 import J1
from mathematics.sde.nonlinear.functions.stratonovich.j10 import J10
from mathematics.sde.nonlinear.functions.stratonovich.j100 import J100
from mathematics.sde.nonlinear.functions.stratonovich.j1000 import J1000
from mathematics.sde.nonlinear.functions.stratonovich.j11 import J11
from mathematics.sde.nonlinear.functions.stratonovich.j2 import J2
from mathematics.sde.nonlinear.functions.stratonovich.j20 import J20


class StrongTaylorStratonovich3p0(sp.Function):
    """
    Strong Taylor 3.0 method
    """
    nargs = 8

    def __new__(cls, *args, **kwargs):
        """
        Creates new Taylor3p0 object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i, yp, m_a, m_b, dt, ksi, dxs, q = sp.sympify(args)
        q = args[7]
        n, m = m_b.shape[0], m_b.shape[1]
        a = sp.MatrixSymbol("a", n, 1)
        b = sp.MatrixSymbol("b", n, m)

        i1, i2, i3, i4, i5, i6 = sp.symbols("i1 i2 i3 i4 i5 i6")
        aj = Aj(i, a, b, dxs)
        formula = \
            yp[i, 0] + aj[i, 0] * dt + \
            sp.Sum(
                b[i, i1] * J0(i1, dt, ksi),
                (i1, 0, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    G(b[:, i1], b[i, i2], dxs) *
                    J00(i1, i2, q[0], dt, ksi),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1)) + \
            sp.Sum(
                G(b[:, i1], aj[i, 0], dxs) *
                (dt * J0(i1, dt, ksi) + J1(i1, dt, ksi)) -
                Lj(a, b[i, i1], dxs) *
                J1(i1, dt, ksi),
                (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs) *
                        J000(i1, i2, i3, q[1], dt, ksi),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            dt ** 2 / 2 * Lj(a, aj[i, 0], dxs) + \
            sp.Sum(
                sp.Sum(
                    G(b[:, i1], Lj(a, b[i, i2], dxs), dxs) *
                    (J10(i1, i2, q[2], dt, ksi) - J01(i1, i2, q[2], dt, ksi)) -
                    Lj(a, G(b[:, i1], b[i, i1], dxs), dxs) * J10(i1, i2, q[2], dt, ksi) +
                    G(b[:, i1], G(b[:, i2], aj[i, 0], dxs), dxs) *
                    (J10(i1, i2, q[2], dt, ksi) + dt * J00(i1, i2, q[0], dt, ksi)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            G(b[:, i1], G(b[:, i2], G(b[:, i3], b[i, i4], dxs), dxs), dxs) *
                            J0000(i1, i2, i3, i4, q[3], dt, ksi),
                            (i4, 1, m - 1)),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            sp.Sum(G(b[:, i1], Lj(a, aj[i, 0], dxs), dxs) *
                   (J2(i1, dt, ksi) / 2 + dt * J1(i1, dt, ksi) + dt ** 2 / 2 * J0(i1, dt, ksi)) +
                   Lj(a, Lj(a, b[i, i1], dxs), dxs) * J2(i1, dt, ksi) / 2 -
                   Lj(a, G(b[:, i1], aj[i, 0], dxs), dxs) * (J2(i1, dt, ksi) + dt * J1(i1, dt, ksi)),
                   (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        G(b[:, i1], Lj(a, G(b[:, i2], b[i, i1], dxs), dxs), dxs) *
                        (J100(i1, i2, i3, q[6], dt, ksi) - J010(i1, i2, i3, q[5], dt, ksi)) +
                        G(b[:, i1], G(b[:, i2], Lj(a, b[i, i3], dxs), dxs), dxs) *
                        (J010(i1, i2, i3, q[5], dt, ksi) - J001(i1, i2, i3, q[4], dt, ksi)) +
                        G(b[:, i1], G(b[:, i2], G(b[:, i3], aj[i, 0], dxs), dxs), dxs) *
                        (dt * J000(i1, i2, i3, q[1], dt, ksi) - J001(i1, i2, i3, q[4], dt, ksi)) -
                        Lj(a, G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs), dxs) *
                        J100(i1, i2, i3, q[6], dt, ksi),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            sp.Sum(
                                G(b[:, i1], G(b[:, i2], G(b[:, i3], G(b[:, i4], b[i, i5], dxs), dxs), dxs), dxs) *
                                J00000(i1, i2, i3, i4, i5, q[7], dt, ksi),
                                (i5, 1, m - 1)),
                            (i4, 1, m - 1)),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            dt ** 3 / 6 * Lj(a, Lj(a, aj[i, 0], dxs), dxs) + \
            sp.Sum(
                sp.Sum(
                    G(b[:, i1], G(b[:, i2], Lj(a, Lj(a, aj[i, 0], dxs), dxs), dxs), dxs) *
                    (J02(i1, i2, q[6], dt, ksi) / 2 + dt * J01(i1, i2, q[2], dt, ksi) +
                     dt ** 2 / 2 * J00(i1, i2, q[2], dt, ksi)) +
                    Lj(a, Lj(a, G(b[:, i1], b[i, i2], dxs), dxs), dxs) / 2 *
                    J20(i1, i2, q[10], dt, ksi) +
                    G(b[:, i1], Lj(a, G(b[:, i2], aj[i, 0], dxs), dxs), dxs) *
                    (J11(i1, i2, q[9], dt, ksi) - J02(i1, i2, q[8], dt, ksi) +
                     dt * (J10(i1, i2, q[2], dt, ksi) - J01(i1, i2, q[2], dt, ksi))) +
                    Lj(a, G(b[:, i1], Lj(a, b[i, i2], dxs), dxs), dxs) *
                    (J11(i1, i2, q[9], dt, ksi) - J20(i1, i2, q[10], dt, ksi)) +
                    G(b[:, i1], Lj(a, Lj(a, b[i, i2], dxs), dxs), dxs) *
                    (J02(i1, i2, q[8], dt, ksi) / 2 + J20(i1, i2, q[10], dt, ksi) / 2 - J11(i1, i2, q[9], dt, ksi)) -
                    Lj(a, G(b[:, i1], G(b[:, i2], aj[i, 0], dxs), dxs), dxs) *
                    (dt * J10(i1, i2, q[2], dt, ksi) + J11(i1, i2, q[9], dt, ksi)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            G(b[:, i1], G(b[:, i2], G(b[:, i3], G(b[:, i4], aj[i, 0], dxs), dxs), dxs), dxs) *
                            (dt * J0000(i1, i2, i3, i4, q[3], dt, ksi) + J0001(i1, i2, i3, i4, q[11], dt, ksi)) +
                            G(b[:, i1], G(b[:, i2], Lj(a, G(b[:, i3], b[i, i4], dxs), dxs), dxs), dxs) *
                            (J0100(i1, i2, i3, i4, q[13], dt, ksi) - J0010(i1, i2, i3, i4, q[12], dt, ksi)) -
                            Lj(a, G(b[:, i1], G(b[:, i2], G(b[:, i3], b[i, i4], dxs), dxs), dxs), dxs) *
                            J1000(i1, i2, i3, i4, q[14], dt, ksi) +
                            G(b[:, i1], Lj(a, G(b[:, i2], G(b[:, i3], b[i, i4], dxs), dxs), dxs), dxs) *
                            (J1000(i1, i2, i3, i4, q[14], dt, ksi) - J0100(i1, i2, i3, i4, q[13], dt, ksi)) +
                            G(b[:, i1], G(b[:, i2], G(b[:, i3], Lj(a, b[i, i4], dxs), dxs), dxs), dxs) *
                            (J0010(i1, i2, i3, i4, q[12], dt, ksi) - J0001(i1, i2, i3, i4, q[11], dt, ksi)),
                            (i4, 1, m - 1)),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            sp.Sum(
                                sp.Sum(
                                    G(b[:, i1],
                                      G(b[:, i2], G(b[:, i3], G(b[:, i4], G(b[:, i5], b[i, i6], dxs), dxs), dxs), dxs),
                                      dxs) *
                                    J000000(i1, i2, i3, i4, i5, i6, q[15], dt, ksi),
                                    (i6, 1, m - 1)),
                                (i5, 1, m - 1)),
                            (i4, 1, m - 1)),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1))

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
        return StrongTaylorStratonovich3p0(*self.args, **hints)
