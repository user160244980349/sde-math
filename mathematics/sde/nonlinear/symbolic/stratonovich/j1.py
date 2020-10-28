from math import sqrt

from sympy import Function, sympify, Number


class J1(Function):
    """
    Stochastic Stratonovich integral
    """
    nargs = 3

    def __new__(cls, *args, **kwargs):
        """
        Creates new J1 object with given args

        Parameters
        −−−−−−−−−−
        i1 : int
            integral index
        dt : float
            delta time
        ksi : numpy.ndarray
            matrix of Gaussian variables
        Returns
        −−−−−−−
        sympy . Expr
            formula to simplify and substitute
        """
        i1, dt, ksi = sympify(args)

        if not isinstance(i1, Number):
            return super(J1, cls).__new__(cls, *args, **kwargs)

        return -(ksi[0, i1] + ksi[1, i1] / sqrt(3)) * dt ** 1.5 / 2

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        J1
        """
        return J1(*self.args, **hints)
