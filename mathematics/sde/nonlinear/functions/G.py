import sympy as sp

from .Operator import Operator
from .Unwrap import Unwrap


class G(Operator):
    """
    Function to perform G operation with function
    """
    nargs = 3

    def __new__(cls, *args, **kwargs):
        obj = super(G, cls).__new__(cls, *args, **kwargs)
        return obj

    def diff(self, *symbols, **assumptions):
        c, f, dxs = self.args
        c = c.doit()
        f = f.doit()
        return G(c, f, dxs).doit()

    def doit(self):
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
        c, f, dxs = self.args
        c = c.doit()
        f = f.doit()
        if (isinstance(f, sp.Number) or f.has(*dxs)) and not isinstance(f, Operator):
            return (Unwrap(sp.MatMul(sp.Transpose(c.doit()), sp.Matrix([sp.Derivative(f, dxi)
                                                                        for dxi in dxs])))).doit()
        else:
            return G(c, f, dxs)
