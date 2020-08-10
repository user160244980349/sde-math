import sympy as sp

from .I0 import I0


class Euler(sp.Function):
    """
    Euler method
    """
    nargs = 6

    def __new__(cls, *args, **kwargs):
        """
        Creates new Euler object with given args
        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i, yp, a, b, dt, ksi = sp.sympify(args)
        m = b.shape[1]
        i1 = sp.symbols('i1')
        return \
            yp[i, 0] + a[i, 0] * dt + \
            sp.Sum(
                b[i, i1] * I0(i1, dt, ksi),
                (i1, 0, m - 1))
