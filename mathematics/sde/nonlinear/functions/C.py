import sympy as sp

from .Cd import Cd


class C(sp.Function):
    """
    Function to perform G operation with function
    """
    nargs = 4

    def __new__(cls, *args, **kwargs):
        j1, j2, j3, dt = sp.sympify(args)
        if isinstance(j1, sp.Number) and isinstance(j2, sp.Number) and \
                isinstance(j3, sp.Number) and isinstance(dt, sp.Number):
            return sp.sqrt((j1 * 2 + 1) * (j2 * 2 + 1) * (j3 * 2 + 1)) * \
                   dt ** (sp.Rational(3, 2)) * Cd(j1, j2, j3).doit() / 8
        else:
            return super(C, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Applies G operator on function
        Parameters
        ----------
            c - b matrix column to apply G operator
            f - function to apply operator
            dxs - arguments to apply Grad

        Returns
        -------
            Scalar result of G operator
        """
        return C(*self.args, **hints)
