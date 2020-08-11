import sympy as sp

from .G import G
from .Operator import Operator


class Aj(Operator):
    """
    Stochastic Ito integral
    """
    nargs = 4

    def __new__(cls, *args, **kwargs):
        """
        Creates new Aj object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i, a, b, dxs = sp.sympify(args)
        m = b.shape[1]
        from sympy.abc import j
        return a[i, 0] - sp.Rational(1, 2) * sp.Sum(G(b[:, j], b[i, j], dxs), (j, 1, m - 1))
