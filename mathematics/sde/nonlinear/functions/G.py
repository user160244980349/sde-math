import sympy as sp

from .Operator import Operator
from .Unwrap import Unwrap


class G(Operator):
    """
    Function to perform G operation with function
    """
    nargs = 3

    def __new__(cls, *args, **kwargs):
        c, f, dxs = sp.sympify(args)
        if (isinstance(f, sp.Number) or f.has(*dxs)) and not isinstance(f, Operator):
            return (Unwrap(sp.MatMul(sp.Transpose(c), sp.Matrix([sp.Derivative(f, dxi)
                                                                 for dxi in dxs]))))
        else:
            return super(G, cls).__new__(cls, *args, **kwargs)

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
        return G(*self.args, **hints)
