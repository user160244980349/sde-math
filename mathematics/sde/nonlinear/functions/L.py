from sympy import Transpose, Trace, Derivative, Rational, Matrix

from mathematics.sde.nonlinear.functions.Operator import Operator
from mathematics.sde.nonlinear.functions.Unwrap import Unwrap


class L(Operator):
    """
    Function to perform G operation with function
    """
    nargs = 4

    # is_commutative = True
    is_Operator = True

    def __new__(cls, *args, **kwargs):
        obj = super(L, cls).__new__(cls, *args, **kwargs)
        return obj

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
        from sympy.abc import t
        a, b, f, dxs = self.args
        a = a.doit()
        b = b.doit()
        f = f.doit()
        if (f.is_Number or f.has(*dxs)) and not isinstance(f, Operator):
            return (Derivative(f, t) +
                    Unwrap(Transpose(Matrix([Derivative(f, dxi)
                                             for dxi in dxs])) * a) +
                    Rational(1, 2) * Trace(Transpose(b) * Matrix([[Derivative(f, dxi, dxj)
                                                                   for dxi in dxs]
                                                                  for dxj in dxs]) * b)).doit()
        else:
            return L(a, b, f, dxs)
