import sympy as sp

from mathematics.sde.nonlinear.symbolic.g import G
from mathematics.sde.nonlinear.symbolic.ito.i0 import I0
from mathematics.sde.nonlinear.symbolic.ito.i00 import I00
from mathematics.sde.nonlinear.symbolic.ito.i000 import I000
from mathematics.sde.nonlinear.symbolic.ito.i0000 import I0000
from mathematics.sde.nonlinear.symbolic.ito.i00000 import I00000
from mathematics.sde.nonlinear.symbolic.ito.i000000 import I000000
from mathematics.sde.nonlinear.symbolic.ito.i0001 import I0001
from mathematics.sde.nonlinear.symbolic.ito.i001 import I001
from mathematics.sde.nonlinear.symbolic.ito.i0010 import I0010
from mathematics.sde.nonlinear.symbolic.ito.i01 import I01
from mathematics.sde.nonlinear.symbolic.ito.i010 import I010
from mathematics.sde.nonlinear.symbolic.ito.i0100 import I0100
from mathematics.sde.nonlinear.symbolic.ito.i02 import I02
from mathematics.sde.nonlinear.symbolic.ito.i1 import I1
from mathematics.sde.nonlinear.symbolic.ito.i10 import I10
from mathematics.sde.nonlinear.symbolic.ito.i100 import I100
from mathematics.sde.nonlinear.symbolic.ito.i1000 import I1000
from mathematics.sde.nonlinear.symbolic.ito.i11 import I11
from mathematics.sde.nonlinear.symbolic.ito.i2 import I2
from mathematics.sde.nonlinear.symbolic.ito.i20 import I20
from mathematics.sde.nonlinear.symbolic.l import L


class StrongTaylorIto3p0(sp.Function):
    """
    Strong Taylor 3.0 method
    """
    nargs = 8

    def __new__(cls, *args, **kwargs):
        """
        Creates new StrongTaylorIto3p0 object with given args

        Parameters
        ----------
        i : int
            component of stochastic process
        yp : numpy.ndarray
            initial conditions
        m_a : numpy.ndarray
            algebraic, given in the variables x and t
        m_b : numpy.ndarray
            algebraic, given in the variables x and t
        dt : float
            integration step
        ksi : numpy.ndarray
            matrix of Gaussian variables
        dxs : tuple
            variables to differentiate
        q : tuple
            amounts of q for integrals approximations

        Returns
        -------
        sympy.Expr
            formula to simplify and substitute
        """
        i, yp, m_a, m_b, dt, ksi, dxs, q = sp.sympify(args)
        q = args[7]
        n, m = m_b.shape[0], m_b.shape[1]
        a = sp.MatrixSymbol("a", n, 1)
        b = sp.MatrixSymbol("b", n, m)

        i1, i2, i3, i4, i5, i6 = sp.symbols("i1 i2 i3 i4 i5 i6")
        formula = \
            yp[i, 0] + a[i, 0] * dt + \
            sp.Sum(
                b[i, i1] * I0(i1, dt, ksi),
                (i1, 0, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    G(b[:, i1], b[i, i2], dxs) *
                    I00(i1, i2, q[0], dt, ksi),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1)) + \
            sp.Sum(
                G(b[:, i1], a[i, 0], dxs) *
                (dt * I0(i1, dt, ksi) + I1(i1, dt, ksi)) -
                L(a, b, b[i, i1], dxs) *
                I1(i1, dt, ksi),
                (i1, 0, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs) *
                        I000(i1, i2, i3, q[1], dt, ksi),
                        (i3, 0, m - 1)),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1)) + \
            dt ** 2 / 2 * L(a, b, a[i, 0], dxs) + \
            sp.Sum(
                sp.Sum(
                    G(b[:, i1], L(a, b, b[i, i2], dxs), dxs) *
                    (I10(i1, i2, q[2], dt, ksi) - I01(i1, i2, q[2], dt, ksi)) -
                    L(a, b, G(b[:, i1], b[i, i2], dxs), dxs) * I10(i1, i2, q[2], dt, ksi) +
                    G(b[:, i1], G(b[:, i2], a[i, 0], dxs), dxs) *
                    (I01(i1, i2, q[2], dt, ksi) + dt * I00(i1, i2, q[0], dt, ksi)),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            G(b[:, i1], G(b[:, i2], G(b[:, i3], b[i, i4], dxs), dxs), dxs) *
                            I0000(i1, i2, i3, i4, q[3], dt, ksi),
                            (i4, 0, m - 1)),
                        (i3, 0, m - 1)),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1)) + \
            sp.Sum(G(b[:, i1], L(a, b, a[i, 0], dxs), dxs) *
                   (I2(i1, dt, ksi) / 2 + dt * I1(i1, dt, ksi) + dt ** 2 / 2 * I0(i1, dt, ksi)) +
                   L(a, b, L(a, b, b[i, i1], dxs), dxs) * I2(i1, dt, ksi) / 2 -
                   L(a, b, G(b[:, i1], a[i, 0], dxs), dxs) * (I2(i1, dt, ksi) + dt * I1(i1, dt, ksi)),
                   (i1, 0, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        G(b[:, i1], L(a, b, G(b[:, i2], b[i, i3], dxs), dxs), dxs) *
                        (I100(i1, i2, i3, q[6], dt, ksi) - I010(i1, i2, i3, q[5], dt, ksi)) +
                        G(b[:, i1], G(b[:, i2], L(a, b, b[i, i3], dxs), dxs), dxs) *
                        (I010(i1, i2, i3, q[5], dt, ksi) - I001(i1, i2, i3, q[4], dt, ksi)) +
                        G(b[:, i1], G(b[:, i2], G(b[:, i3], a[i, 0], dxs), dxs), dxs) *
                        (dt * I000(i1, i2, i3, q[1], dt, ksi) + I001(i1, i2, i3, q[4], dt, ksi)) -
                        L(a, b, G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs), dxs) *
                        I100(i1, i2, i3, q[6], dt, ksi),
                        (i3, 0, m - 1)),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            sp.Sum(
                                G(b[:, i1], G(b[:, i2], G(b[:, i3], G(b[:, i4], b[i, i5], dxs), dxs), dxs), dxs) *
                                I00000(i1, i2, i3, i4, i5, q[7], dt, ksi),
                                (i5, 0, m - 1)),
                            (i4, 0, m - 1)),
                        (i3, 0, m - 1)),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1)) + \
            dt ** 3 / 6 * L(a, b, L(a, b, a[i, 0], dxs), dxs) + \
            sp.Sum(
                sp.Sum(
                    G(b[:, i1], G(b[:, i2], L(a, b, a[i, 0], dxs), dxs), dxs) *
                    (I02(i1, i2, q[6], dt, ksi) / 2 + dt * I01(i1, i2, q[2], dt, ksi) +
                     dt ** 2 / 2 * I00(i1, i2, q[2], dt, ksi)) +
                    L(a, b, L(a, b, G(b[:, i1], b[i, i2], dxs), dxs), dxs) / 2 *
                    I20(i1, i2, q[10], dt, ksi) +
                    G(b[:, i1], L(a, b, G(b[:, i2], a[i, 0], dxs), dxs), dxs) *
                    (I11(i1, i2, q[9], dt, ksi) - I02(i1, i2, q[8], dt, ksi) +
                     dt * (I10(i1, i2, q[2], dt, ksi) - I01(i1, i2, q[2], dt, ksi))) +
                    L(a, b, G(b[:, i1], L(a, b, b[i, i2], dxs), dxs), dxs) *
                    (I11(i1, i2, q[9], dt, ksi) - I20(i1, i2, q[10], dt, ksi)) +
                    G(b[:, i1], L(a, b, L(a, b, b[i, i2], dxs), dxs), dxs) *
                    (I02(i1, i2, q[8], dt, ksi) / 2 + I20(i1, i2, q[10], dt, ksi) / 2 - I11(i1, i2, q[9], dt, ksi)) -
                    L(a, b, G(b[:, i1], G(b[:, i2], a[i, 0], dxs), dxs), dxs) *
                    (dt * I10(i1, i2, q[2], dt, ksi) + I11(i1, i2, q[9], dt, ksi)),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            G(b[:, i1], G(b[:, i2], G(b[:, i3], G(b[:, i4], a[i, 0], dxs), dxs), dxs), dxs) *
                            (dt * I0000(i1, i2, i3, i4, q[3], dt, ksi) + I0001(i1, i2, i3, i4, q[11], dt, ksi)) +
                            G(b[:, i1], G(b[:, i2], L(a, b, G(b[:, i3], b[i, i4], dxs), dxs), dxs), dxs) *
                            (I0100(i1, i2, i3, i4, q[13], dt, ksi) - I0010(i1, i2, i3, i4, q[12], dt, ksi)) -
                            L(a, b, G(b[:, i1], G(b[:, i2], G(b[:, i3], b[i, i4], dxs), dxs), dxs), dxs) *
                            I1000(i1, i2, i3, i4, q[14], dt, ksi) +
                            G(b[:, i1], L(a, b, G(b[:, i2], G(b[:, i3], b[i, i4], dxs), dxs), dxs), dxs) *
                            (I1000(i1, i2, i3, i4, q[14], dt, ksi) - I0100(i1, i2, i3, i4, q[13], dt, ksi)) +
                            G(b[:, i1], G(b[:, i2], G(b[:, i3], L(a, b, b[i, i4], dxs), dxs), dxs), dxs) *
                            (I0010(i1, i2, i3, i4, q[12], dt, ksi) - I0001(i1, i2, i3, i4, q[11], dt, ksi)),
                            (i4, 0, m - 1)),
                        (i3, 0, m - 1)),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            sp.Sum(
                                sp.Sum(
                                    G(b[:, i1],
                                      G(b[:, i2], G(b[:, i3], G(b[:, i4], G(b[:, i5], b[i, i6], dxs), dxs), dxs), dxs),
                                      dxs) *
                                    I000000(i1, i2, i3, i4, i5, i6, q[15], dt, ksi),
                                    (i6, 0, m - 1)),
                                (i5, 0, m - 1)),
                            (i4, 0, m - 1)),
                        (i3, 0, m - 1)),
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
        return StrongTaylorIto3p0(*self.args, **hints)
