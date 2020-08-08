import sympy as sp

from .C import C


class Cooo(sp.Function):
    """
    Function to perform G operation with function
    """
    nargs = 4

    def __new__(cls, *args, **kwargs):
        j3, j2, j1, dt = sp.sympify(args)
        if isinstance(j1, sp.Number) and isinstance(j2, sp.Number) and \
                isinstance(j3, sp.Number) and isinstance(dt, sp.Number):
            return sp.sqrt((j1 * 2 + 1) * (j2 * 2 + 1) * (j3 * 2 + 1)) * \
                   dt**sp.Rational(3, 2) * C(j3, j2, j1) / 8
        else:
            return super(Cooo, cls).__new__(cls, *args, **kwargs)

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
        return Cooo(*self.args, **hints)
