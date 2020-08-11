import sympy as sp

from .G import G
from .L import L
from .Operator import Operator


class Lj(Operator):
    """
    Stochastic Ito integral
    """
    nargs = 4

    def __new__(cls, *args, **kwargs):
        """
        Creates new Lj object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        a, b, f, dxs = sp.sympify(args)
        n = b.shape[0]
        m = b.shape[1]
        from sympy.abc import j
        if (isinstance(f, sp.Number) or f.has(*dxs)) and not f.has(Operator) \
                and a.is_Matrix and b.is_Matrix:
            sym_b, sym_a = sp.MatrixSymbol('a', n, 1), sp.MatrixSymbol('b', n, m)
            return (L(a, b, f, dxs) - sp.Sum(
                G(sym_b[:, j],
                  G(sym_b[:, j], f, dxs), dxs), (j, 1, m - 1))).subs([(sym_a, a), (sym_b, b)])
        else:
            return super(Lj, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        Lj
        """
        return Lj(*self.args, **hints)
