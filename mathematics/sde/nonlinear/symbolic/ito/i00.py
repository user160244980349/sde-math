from math import sqrt

from sympy import sympify, Number, Function, Add

from mathematics.sde.nonlinear.symbolic.ind import Ind


class I00(Function):
    """
    Iterated Ito stochastic integral
    """
    nargs = 5

    def __new__(cls, *args, **kwargs):
        """
        Creates new I00 object with given args
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
                isinstance(i2, Number) and
                isinstance(q, Number)):
            return super(I00, cls).__new__(cls, *args, **kwargs)

        return \
            (ksi[0, i1] * ksi[0, i2] +
             Add(*[
                 (ksi[j1 - 1, i1] * ksi[j1, i2] -
                  ksi[j1, i1] * ksi[j1 - 1, i2]) /
                 sqrt(j1 ** 2 * 4 - 1)
                 for j1 in range(1, q + 1)]) -
             Ind(i1, i2)) * dt / 2

    def doit(self, **hints):
        """
        Tries to expand or calculate function
        Returns
        =======
        I00
        """
        return I00(*self.args, **hints)
