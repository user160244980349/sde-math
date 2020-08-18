import sympy as sp

from mathematics.sde.nonlinear.functions.coefficients.c import C
from mathematics.sde.nonlinear.functions.g import G
from mathematics.sde.nonlinear.functions.ito.i0 import I0
from mathematics.sde.nonlinear.functions.ito.i00 import I00
from mathematics.sde.nonlinear.functions.ito.i000 import I000
from mathematics.sde.nonlinear.functions.ito.i1 import I1
from mathematics.sde.nonlinear.functions.l import L


class StrongTaylorIto1p5(sp.Function):
    """
    Strong Taylor 1.5 method
    """
    nargs = 9

    def __new__(cls, *args, **kwargs):
        """
        Creates new Taylor1p5 object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i, yp, m_a, m_b, q, q1, dt, ksi, dxs = sp.sympify(args)
        n = m_b.shape[0]
        m = m_b.shape[1]
        a = sp.MatrixSymbol("a", n, 1)
        b = sp.MatrixSymbol("b", n, m)

        if isinstance(q1, sp.Number):
            C.preload(int(q1))

        i1, i2, i3 = sp.symbols("i1 i2 i3")

        formula = \
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
                I1(i1, dt, ksi), (i1, 1, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    sp.Sum(
                        G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs) *
                        I000(i1, i2, i3, q1, dt, ksi),
                        (i3, 1, m - 1)),
                    (i2, 1, m - 1)),
                (i1, 1, m - 1)) + \
            dt ** 2 / 2 * L(a, b, a[i, 0], dxs)

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
        return StrongTaylorIto1p5(*self.args, **hints)
