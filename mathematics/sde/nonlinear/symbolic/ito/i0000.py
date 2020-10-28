from sympy import Function, sympify, Number, Add

from mathematics.sde.nonlinear.symbolic.coefficients.c0000 import C0000
from mathematics.sde.nonlinear.symbolic.ind import Ind


class I0000(Function):
    """
    Iterated Ito stochastic integral
    """
    nargs = 7

    def __new__(cls, *args, **kwargs):
        """
        Creates new I0000 object with given args
        Parameters
        ==========
        i1 : int
            integral index
        i2 : int
            integral index
        i3 : int
            integral index
        i4 : int
            integral index
        q : int
            amount of terms in approximation of integral
        dt : float
            delta time
        ksi : numpy.ndarray
            matrix of Gaussian variables
        Returns
        =======
        sympy.Expr
            formula to simplify and substitute
        """
        i1, i2, i3, i4, q, dt, ksi = sympify(args)

        if not (isinstance(i1, Number) and
                isinstance(i2, Number) and
                isinstance(i3, Number) and
                isinstance(i4, Number) and
                isinstance(q, Number)):
            return super(I0000, cls).__new__(cls, *args, **kwargs)

        return Add(*[
            C0000(j4, j3, j2, j1, dt) *
            (ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] * ksi[j4, i4] -
             Ind(i1, i2) * Ind(j1, j2) * ksi[j3, i3] * ksi[j4, i4] -
             Ind(i1, i3) * Ind(j1, j3) * ksi[j2, i2] * ksi[j4, i4] -
             Ind(i1, i4) * Ind(j1, j4) * ksi[j2, i2] * ksi[j3, i3] -
             Ind(i2, i3) * Ind(j2, j3) * ksi[j1, i1] * ksi[j4, i4] -
             Ind(i2, i4) * Ind(j2, j4) * ksi[j1, i1] * ksi[j3, i3] -
             Ind(i3, i4) * Ind(j3, j4) * ksi[j1, i1] * ksi[j2, i2] +
             Ind(i1, i2) * Ind(j1, j2) * Ind(i3, i4) * Ind(j3, j4) +
             Ind(i1, i3) * Ind(j1, j3) * Ind(i2, i4) * Ind(j2, j4) +
             Ind(i1, i4) * Ind(j1, j4) * Ind(i2, i3) * Ind(j2, j3))
            for j4 in range(q + 1)
            for j3 in range(q + 1)
            for j2 in range(q + 1)
            for j1 in range(q + 1)])

    def doit(self, **hints):
        """
        Tries to expand or calculate function
        Returns
        =======
        I0000
        """
        return I0000(*self.args, **hints)
