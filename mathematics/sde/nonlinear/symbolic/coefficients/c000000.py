import sympy as sp

from mathematics.sde.nonlinear.symbolic.coefficients.c import C


class C000000(sp.Function):
    """
    Gives coefficient with requested indices and weights
    """
    nargs = 7

    def __new__(cls, *args, **kwargs):
        """
        Creates C coefficient object with needed
        indices and weights and calculates it in
        another normalized form

        Parameters
        ----------
        indices: tuple
            requested indices
        weights: tuple
            requested weights
        Returns
        -------
        symbolic.Rational or C0000
            calculated value or symbolic expression
        """
        j6, j5, j4, j3, j2, j1, dt = sp.sympify(args)
        if isinstance(j1, sp.Number) and \
                isinstance(j2, sp.Number) and \
                isinstance(j3, sp.Number) and \
                isinstance(j4, sp.Number) and \
                isinstance(j5, sp.Number) and \
                isinstance(dt, sp.Number):
            return sp.sqrt((j1 * 2 + 1) * (j2 * 2 + 1) * (j3 * 2 + 1) *
                           (j4 * 2 + 1) * (j5 * 2 + 1) * (j6 * 2 + 1)) * \
                   dt ** 3 * C((j6, j5, j4, j3, j2, j1), (0, 0, 0, 0, 0, 0)) / 64
        else:
            return super(C000000, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        C000000
        """
        return C000000(*self.args, **hints)
