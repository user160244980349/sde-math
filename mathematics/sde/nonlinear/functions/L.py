import sympy as sp

from .Operator import Operator
from .Unwrap import Unwrap


class L(Operator):
    """
    Function to perform G operation with function
    """
    nargs = 4

    is_Operator = True

    def __new__(cls, *args, **kwargs):
        a, b, f, dxs = sp.sympify(args)
        if (isinstance(f, sp.Number) or f.has(*dxs)) and not isinstance(f, Operator):
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
        Applies G operator on function
        TIPS:
            Always use doit on args,
            Check for instance type,
            Use is_symbol to filter dummies
        Parameters
        ----------
            c - b matrix column to apply G operator
            f - function to apply operator
            dxs - arguments to apply Grad

        Returns
        -------
            Scalar result of G operator
        """
        return L(*self.args, **hints)
