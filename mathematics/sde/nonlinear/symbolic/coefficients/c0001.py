from math import sqrt

from sympy import sympify, Function, Number

from mathematics.sde.nonlinear.symbolic.coefficients.c import C


class C0001(Function):
    """
    Gives coefficient with requested indices and weights
    """
    nargs = 5

    def __new__(cls, *args, **kwargs):
        """
        Creates C coefficient object with needed
        indices and weights and calculates it
        Parameters
        ==========
        indices: tuple
            requested indices
        weights: tuple
            requested weights
        Returns
        =======
        symbolic.Rational or C0001
            calculated value or symbolic expression
        """
        j4, j3, j2, j1, dt = sympify(args)

        if not (isinstance(j1, Number) and
                isinstance(j2, Number) and
                isinstance(j3, Number) and
                isinstance(j4, Number) and
                isinstance(dt, Number)):
            return super(C0001, cls).__new__(cls, *args, **kwargs)

        return sqrt(
            (j1 * 2 + 1) *
            (j2 * 2 + 1) *
            (j3 * 2 + 1) *
            (j4 * 2 + 1)) * \
               dt ** 3 * \
               C((j4, j3, j2, j1), (0, 0, 0, 1)) / 32

    def doit(self, **hints):
        """
        Tries to expand or calculate function
        Returns
        =======
        C0001
        """
        return C0001(*self.args, **hints)
