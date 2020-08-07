from sympy import Function, Transpose, MatMul, Matrix, MatrixExpr, Expr, pprint, S, Derivative

from mathematics.sde.nonlinear.functions.Unwrap import Unwrap
from mathematics.sde.nonlinear.functions.Operator import Operator


class G(Operator):
    """
    Function to perform G operation with function
    """
    nargs = 3

    # is_commutative = True
    is_Operator = True

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
        if (f.is_Number or f.has(*dxs)) and not isinstance(f, Operator):
        # if f.is_Number or f.has(*dxs):
        #     print('\n-----------------------------------------')
        #     pprint((Unwrap(MatMul(Transpose(c.doit()), Matrix([Derivative(f, dxi)
        #                                                        for dxi in dxs])))).doit())
            return (Unwrap(MatMul(Transpose(c.doit()), Matrix([Derivative(f, dxi)
                                                               for dxi in dxs])))).doit()
        else:
            return G(c, f, dxs)
