from math import sqrt

from sympy import sympify, Number, Function

from mathematics.sde.nonlinear.symbolic.coefficients.c import C


class C000(Function):
    """
    Gives coefficient with requested indices and weights
    """
    nargs = 4

    def __new__(cls, *args, **kwargs):
        """
        Creates C coefficient object with needed
        indices and weights and calculates it

        Parameters
        ----------
        indices: tuple
            requested indices
        weights: tuple
            requested weights
        Returns
        -------
        symbolic.Rational or C000
            calculated value or symbolic expression
        """
        j3, j2, j1, dt = sympify(args)

        if not (isinstance(j1, Number) and
                isinstance(j2, Number) and
                isinstance(j3, Number) and
                isinstance(dt, Number)):
            return super(C000, cls).__new__(cls, *args, **kwargs)

        return sqrt(
            (j1 * 2 + 1) *
            (j2 * 2 + 1) *
            (j3 * 2 + 1)) * \
               dt ** 1.5 * \
               C((j3, j2, j1), (0, 0, 0)) / 8

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        C000
        """
        return C000(*self.args, **hints)
