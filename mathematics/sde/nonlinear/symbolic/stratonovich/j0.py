from math import sqrt

from sympy import Function, sympify, Number


class J0(Function):
    """
    Stochastic Stratonovich integral
    """
    nargs = 3

    def __new__(cls, *args, **kwargs):
        """
        Calculates J0 integral approximation
        Parameters
        ==========
        i1 : int
            integral index
        dt : float
            delta time
        ksi : numpy.ndarray
            matrix of Gaussian variables
        Returns
        =======
        sympy.Expr
            formula to simplify and substitute
        """
        i1, dt, ksi = sympify(args)

        if not isinstance(i1, Number):
            return super(J0, cls).__new__(cls, *args, **kwargs)

        return ksi[0, i1] * sqrt(dt)

    def doit(self, **hints):
        """
        Tries to expand or calculate function
        Returns
        =======
        J0
        """
        return J0(*self.args, **hints)
