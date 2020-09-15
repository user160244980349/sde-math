import sympy as sp

from mathematics.sde.nonlinear.functions.g import G
from mathematics.sde.nonlinear.functions.ito.i0 import I0
from mathematics.sde.nonlinear.functions.ito.i00 import I00
from mathematics.sde.nonlinear.functions.ito.i000 import I000
from mathematics.sde.nonlinear.functions.ito.i0000 import I0000
from mathematics.sde.nonlinear.functions.ito.i01 import I01
from mathematics.sde.nonlinear.functions.ito.i1 import I1
from mathematics.sde.nonlinear.functions.ito.i10 import I10
from mathematics.sde.nonlinear.functions.l import L


class StrongTaylorIto2p0(sp.Function):
    """
    Strong Taylor 2.0 method
    """
    nargs = 8

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
        i, yp, m_a, m_b, dt, ksi, dxs, q = sp.sympify(args)
        q = args[7]
        n, m = m_b.shape[0], m_b.shape[1]
        a = sp.MatrixSymbol("a", n, 1)
        b = sp.MatrixSymbol("b", n, m)

        i1, i2, i3, i4 = sp.symbols("i1 i2 i3 i4")
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
                (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs) *
                        I000(i1, i2, i3, q[1], dt, ksi),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            dt ** 2 / 2 * L(a, b, a[i, 0], dxs) + \
            sp.Sum(
                sp.Sum(
                    G(b[:, i1], L(a, b, b[i, i2], dxs), dxs) *
                    (I10(i1, i2, q[2], dt, ksi) - I01(i1, i2, q[2], dt, ksi)) -
                    L(a, b, G(b[:, i1], b[i, i1], dxs), dxs) * I10(i1, i2, q[2], dt, ksi) +
                    G(b[:, i1], G(b[:, i2], a[i, 0], dxs), dxs) *
                    (I10(i1, i2, q[2], dt, ksi) + dt * I00(i1, i2, q[0], dt, ksi)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            G(b[:, i1], G(b[:, i2], G(b[:, i3], b[i, i4], dxs), dxs), dxs) *
                            I0000(i1, i2, i3, i4, q[3], dt, ksi),
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
        return StrongTaylorIto2p0(*self.args, **hints)
