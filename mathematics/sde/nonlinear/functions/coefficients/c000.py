import sympy as sp

from mathematics.sde.nonlinear.functions.coefficients.c import C


class C000(sp.Function):
    """
    Gives coefficient with requested indices and weights
    """
    nargs = 4

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
        sympy.Rational or C000
            calculated value or symbolic expression
        """
        j3, j2, j1, dt = sp.sympify(args)
        if isinstance(j1, sp.Number) and isinstance(j2, sp.Number) and \
                isinstance(j3, sp.Number) and isinstance(dt, sp.Number):
            return sp.sqrt((j1 * 2 + 1) * (j2 * 2 + 1) * (j3 * 2 + 1)) * \
                   dt ** sp.Rational(3, 2) * C((j3, j2, j1), (0, 0, 0)) / 8
        else:
            return super(C000, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        C000
        """
        return C000(*self.args, **hints)
