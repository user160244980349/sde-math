from sympy import Function, sympify, Number, Add

from mathematics.sde.nonlinear.symbolic.coefficients.c11 import C11
from mathematics.sde.nonlinear.symbolic.ind import Ind


class I11(Function):
    """
    Iterated Ito stochastic integral
    """
    nargs = 5

    def __new__(cls, *args, **kwargs):
        """
        Creates new I11 object with given args
        Parameters
        ==========
        i1 : int
            integral index
        i2 : int
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
        i1, i2, q, dt, ksi = sympify(args)

        if not (isinstance(i1, Number) and
                isinstance(i2, Number)):
            return super(I11, cls).__new__(cls, *args, **kwargs)

        return Add(*[
            C11(j2, j1, dt) *
            (ksi[j1, i1] * ksi[j2, i2] - Ind(i1, i2) * Ind(j1, j2))
            for j2 in range(q + 1)
            for j1 in range(q + 1)])

    def doit(self, **hints):
        """
        Tries to expand or calculate function
        Returns
        =======
        I20
        """
        return I11(*self.args, **hints)
