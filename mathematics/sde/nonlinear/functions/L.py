import sympy as sp

from .Operator import Operator
from .Unwrap import Unwrap


class L(Operator):
    """
    Performs L operation on function
    """
    nargs = 4

    def __new__(cls, *args, **kwargs):
        """
        Creates new L object with given args

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
        if (isinstance(f, sp.Number) or f.has(*dxs)) and not f.has(Operator):
            from sympy.abc import t
            return (sp.Derivative(f, t) +
                    Unwrap(sp.Transpose(sp.Matrix([sp.Derivative(f, dxi)
                                                   for dxi in dxs])) * a) +
                    sp.Rational(1, 2) * sp.Trace(sp.Transpose(b) * sp.Matrix([[sp.Derivative(f, dxi, dxj)
                                                                               for dxi in dxs]
                                                                              for dxj in dxs]) * b))
        else:
            return super(L, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        L
        """
        return L(*self.args, **hints)
