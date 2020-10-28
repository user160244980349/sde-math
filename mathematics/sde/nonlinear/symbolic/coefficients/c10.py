from math import sqrt

from sympy import sympify, Function, Number

from mathematics.sde.nonlinear.symbolic.coefficients.c import C


class C10(Function):
    """
    Gives coefficient with requested indices and weights
    """
    nargs = 3

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
        symbolic.Rational or C10
            calculated value or symbolic expression
        """
        j2, j1, dt = sympify(args)

        if not (isinstance(j1, Number) and
                isinstance(j2, Number) and
                isinstance(dt, Number)):
            return super(C10, cls).__new__(cls, *args, **kwargs)

        return sqrt(
            (j1 * 2 + 1) *
            (j2 * 2 + 1)) * \
               dt ** 2 * \
               C((j2, j1), (1, 0)) / 8

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        C10
        """
        return C10(*self.args, **hints)
