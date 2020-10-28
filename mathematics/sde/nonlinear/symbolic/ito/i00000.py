from sympy import Function, Number, sympify, Add

from mathematics.sde.nonlinear.symbolic.coefficients.c00000 import C00000
from mathematics.sde.nonlinear.symbolic.ind import Ind


class I00000(Function):
    """
    Iterated Ito stochastic integral
    """
    nargs = 8

    def __new__(cls, *args, **kwargs):
        """
        Creates new I00000 object with given args
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
        i5 : int
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
        i1, i2, i3, i4, i5, q, dt, ksi = sympify(args)

        if not (isinstance(i1, Number) and
                isinstance(i2, Number) and
                isinstance(i3, Number) and
                isinstance(i4, Number) and
                isinstance(i5, Number) and
                isinstance(q, Number) and
                isinstance(dt, Number)):
            return super(I00000, cls).__new__(cls, *args, **kwargs)

        return Add(*[
            C00000(j5, j4, j3, j2, j1, dt) *
            (ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] * ksi[j4, i4] * ksi[j5, i5] -
             Ind(i1, i2) * Ind(j1, j2) * ksi[j3, i3] * ksi[j4, i4] * ksi[j5, i5] -
             Ind(i1, i3) * Ind(j1, j3) * ksi[j2, i2] * ksi[j4, i4] * ksi[j5, i5] -
             Ind(i1, i4) * Ind(j1, j4) * ksi[j2, i2] * ksi[j3, i3] * ksi[j5, i5] -
             Ind(i1, i5) * Ind(j1, j5) * ksi[j2, i2] * ksi[j3, i3] * ksi[j4, i4] -
             Ind(i2, i3) * Ind(j2, j3) * ksi[j1, i1] * ksi[j4, i4] * ksi[j5, i5] -
             Ind(i2, i4) * Ind(j2, j4) * ksi[j1, i1] * ksi[j3, i3] * ksi[j5, i5] -
             Ind(i2, i5) * Ind(j2, j5) * ksi[j1, i1] * ksi[j3, i3] * ksi[j4, i4] -
             Ind(i3, i4) * Ind(j3, j4) * ksi[j1, i1] * ksi[j2, i2] * ksi[j5, i5] -
             Ind(i3, i5) * Ind(j3, j5) * ksi[j1, i1] * ksi[j2, i2] * ksi[j4, i4] -
             Ind(i4, i5) * Ind(j4, j5) * ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] +
             Ind(i1, i2) * Ind(j1, j2) * Ind(i3, i4) * Ind(j3, j4) * ksi[j5, i5] +
             Ind(i1, i2) * Ind(j1, j2) * Ind(i3, i5) * Ind(j3, j5) * ksi[j4, i4] +
             Ind(i1, i2) * Ind(j1, j2) * Ind(i4, i5) * Ind(j4, j5) * ksi[j3, i3] +
             Ind(i1, i3) * Ind(j1, j3) * Ind(i2, i4) * Ind(j2, j4) * ksi[j5, i5] +
             Ind(i1, i3) * Ind(j1, j3) * Ind(i2, i5) * Ind(j2, j5) * ksi[j4, i4] +
             Ind(i1, i3) * Ind(j1, j3) * Ind(i4, i5) * Ind(j4, j5) * ksi[j2, i2] +
             Ind(i1, i4) * Ind(j1, j4) * Ind(i2, i3) * Ind(j2, j3) * ksi[j5, i5] +
             Ind(i1, i4) * Ind(j1, j4) * Ind(i2, i5) * Ind(j2, j5) * ksi[j3, i3] +
             Ind(i1, i4) * Ind(j1, j4) * Ind(i3, i5) * Ind(j3, j5) * ksi[j2, i2] +
             Ind(i1, i5) * Ind(j1, j5) * Ind(i2, i3) * Ind(j2, j3) * ksi[j4, i4] +
             Ind(i1, i5) * Ind(j1, j5) * Ind(i2, i4) * Ind(j2, j4) * ksi[j3, i3] +
             Ind(i1, i5) * Ind(j1, j5) * Ind(i3, i4) * Ind(j3, j4) * ksi[j2, i2] +
             Ind(i2, i3) * Ind(j2, j3) * Ind(i4, i5) * Ind(j4, j5) * ksi[j1, i1] +
             Ind(i2, i4) * Ind(j2, j4) * Ind(i3, i5) * Ind(j3, j5) * ksi[j1, i1] +
             Ind(i2, i5) * Ind(j2, j5) * Ind(i3, i4) * Ind(j3, j4) * ksi[j1, i1])
            for j5 in range(q + 1)
            for j4 in range(q + 1)
            for j3 in range(q + 1)
            for j2 in range(q + 1)
            for j1 in range(q + 1)])

    def doit(self, **hints):
        """
        Tries to expand or calculate function
        Returns
        =======
        I00000
        """
        return I00000(*self.args, **hints)
