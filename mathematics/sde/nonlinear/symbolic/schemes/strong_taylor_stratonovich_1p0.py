import sympy as sp

from mathematics.sde.nonlinear.symbolic.aj import Aj
from mathematics.sde.nonlinear.symbolic.g import G
from mathematics.sde.nonlinear.symbolic.stratonovich.j0 import J0
from mathematics.sde.nonlinear.symbolic.stratonovich.j00 import J00


class StrongTaylorStratonovich1p0(sp.Function):
    """
    Strong Taylor Stratonovich 1.0 method
    """
    nargs = 8

    def __new__(cls, *args, **kwargs):
        """
        Creates new StrongTaylorStratonovich1p0 object with given args

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

        i1, i2 = sp.symbols("i1 i2")
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
        return StrongTaylorStratonovich1p0(*self.args, **hints)
