from math import sqrt

from sympy import sympify, Number, Function

from mathematics.sde.nonlinear.symbolic.coefficients.c import C


class C000000(Function):
    """
    Gives coefficient with requested indices and weights
    """
    nargs = 7

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
        symbolic.Rational or C000000
            calculated value or symbolic expression
        """
        j6, j5, j4, j3, j2, j1, dt = sympify(args)

        if not (isinstance(j1, Number) and
                isinstance(j2, Number) and
                isinstance(j3, Number) and
                isinstance(j4, Number) and
                isinstance(j5, Number) and
                isinstance(dt, Number)):
            return super(C000000, cls).__new__(cls, *args, **kwargs)

        return sqrt(
            (j1 * 2 + 1) *
            (j2 * 2 + 1) *
            (j3 * 2 + 1) *
            (j4 * 2 + 1) *
            (j5 * 2 + 1) *
            (j6 * 2 + 1)) * \
               dt ** 3 * \
               C((j6, j5, j4, j3, j2, j1), (0, 0, 0, 0, 0, 0)) / 64

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        C000000
        """
        return C000000(*self.args, **hints)
