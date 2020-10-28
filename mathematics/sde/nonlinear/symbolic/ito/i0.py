from math import sqrt

from sympy import Function, sympify, Number


class I0(Function):
    """
    Stochastic Ito integral
    """
    nargs = 3

    def __new__(cls, *args, **kwargs):
        """
        Calculates I0 integral approximation

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
            return super(I0, cls).__new__(cls, *args, **kwargs)

        return ksi[0, i1] * sqrt(dt)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        I0
        """
        return I0(*self.args, **hints)
