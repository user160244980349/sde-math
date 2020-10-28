from math import sqrt

from sympy import sympify, Number, Function


class I2(Function):
    """
    Stochastic Ito integral
    """
    nargs = 3

    def __new__(cls, *args, **kwargs):
        """
        Creates new I2 object with given args

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
            return super(I2, cls).__new__(cls, *args, **kwargs)

        return (ksi[0, i1] + ksi[1, i1] * sqrt(3) / 2 +
                ksi[2, i1] / sqrt(5) / 2) * dt ** 2.5 / 3

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        I2
        """
        return I2(*self.args, **hints)
