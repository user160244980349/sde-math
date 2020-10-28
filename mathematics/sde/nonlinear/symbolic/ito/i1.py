from math import sqrt

from sympy import Function, sympify, Number


class I1(Function):
    """
    Stochastic Ito integral
    """
    nargs = 3

    def __new__(cls, *args, **kwargs):
        """
        Creates new I1 object with given args

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
            return super(I1, cls).__new__(cls, *args, **kwargs)

        return -(ksi[0, i1] + ksi[1, i1] / sqrt(3)) * dt ** 1.5 / 2

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        I1
        """
        return I1(*self.args, **hints)
