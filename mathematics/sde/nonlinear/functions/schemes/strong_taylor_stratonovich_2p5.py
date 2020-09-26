import sympy as sp

from mathematics.sde.nonlinear.functions.aj import Aj
from mathematics.sde.nonlinear.functions.g import G
from mathematics.sde.nonlinear.functions.l import L
from mathematics.sde.nonlinear.functions.lj import Lj
from mathematics.sde.nonlinear.functions.stratonovich.j0 import J0
from mathematics.sde.nonlinear.functions.stratonovich.j00 import J00
from mathematics.sde.nonlinear.functions.stratonovich.j000 import J000
from mathematics.sde.nonlinear.functions.stratonovich.j0000 import J0000
from mathematics.sde.nonlinear.functions.stratonovich.j00000 import J00000
from mathematics.sde.nonlinear.functions.stratonovich.j001 import J001
from mathematics.sde.nonlinear.functions.stratonovich.j01 import J01
from mathematics.sde.nonlinear.functions.stratonovich.j010 import J010
from mathematics.sde.nonlinear.functions.stratonovich.j1 import J1
from mathematics.sde.nonlinear.functions.stratonovich.j10 import J10
from mathematics.sde.nonlinear.functions.stratonovich.j100 import J100
from mathematics.sde.nonlinear.functions.stratonovich.j2 import J2


class StrongTaylorStratonovich2p5(sp.Function):
    """
    Strong Taylor 2.5 method
    """
    nargs = 8

    def __new__(cls, *args, **kwargs):
        """
        Creates new StrongTaylorStratonovich2p5 object with given args

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

        i1, i2, i3, i4, i5 = sp.symbols("i1 i2 i3 i4 i5")
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
                (i1, 0, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs) *
                        J000(i1, i2, i3, q[1], dt, ksi),
                        (i3, 0, m - 1)),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1)) + \
            dt ** 2 / 2 * Lj(a, aj[i, 0], dxs) + \
            sp.Sum(
                sp.Sum(
                    G(b[:, i1], Lj(a, b[i, i2], dxs), dxs) *
                    (J10(i1, i2, q[2], dt, ksi) - J01(i1, i2, q[2], dt, ksi)) -
                    Lj(a, G(b[:, i1], b[i, i1], dxs), dxs) * J10(i1, i2, q[2], dt, ksi) +
                    G(b[:, i1], G(b[:, i2], aj[i, 0], dxs), dxs) *
                    (J10(i1, i2, q[2], dt, ksi) + dt * J00(i1, i2, q[0], dt, ksi)),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            G(b[:, i1], G(b[:, i2], G(b[:, i3], b[i, i4], dxs), dxs), dxs) *
                            J0000(i1, i2, i3, i4, q[3], dt, ksi),
                            (i4, 0, m - 1)),
                        (i3, 0, m - 1)),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1)) + \
            sp.Sum(G(b[:, i1], Lj(a, aj[i, 0], dxs), dxs) *
                   (J2(i1, dt, ksi) / 2 + dt * J1(i1, dt, ksi) + dt ** 2 / 2 * J0(i1, dt, ksi)) +
                   Lj(a, Lj(a, b[i, i1], dxs), dxs) * J2(i1, dt, ksi) / 2 -
                   Lj(a, G(b[:, i1], aj[i, 0], dxs), dxs) * (J2(i1, dt, ksi) + dt * J1(i1, dt, ksi)),
                   (i1, 0, m - 1)) + \
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
                        (i3, 0, m - 1)),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            sp.Sum(
                                G(b[:, i1], G(b[:, i2], G(b[:, i3], G(b[:, i4], b[i, i5], dxs), dxs), dxs), dxs) *
                                J00000(i1, i2, i3, i4, i5, q[7], dt, ksi),
                                (i5, 0, m - 1)),
                            (i4, 0, m - 1)),
                        (i3, 0, m - 1)),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1)) + \
            dt ** 3 / 6 * L(a, b, L(a, b, a[i, 0], dxs), dxs)

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
        return StrongTaylorStratonovich2p5(*self.args, **hints)
