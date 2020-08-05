from sympy import Function, Transpose, Trace, Derivative, Rational

from mathematics.sde.nonlinear.functions.Grad import Grad
from mathematics.sde.nonlinear.functions.Hess import Hess
from mathematics.sde.nonlinear.functions.Unwrap import Unwrap


class L(Function):
    """
    Function to perform L operation with function
    """
    nargs = 4

    @classmethod
    def eval(cls, f, a, b, dxs):
        """
        Applies G operator on function
        Important: t variable is implicit differentiate argument
        Parameters
        ----------
            f - function to apply G operator
            a - matrix a
            b - matrix b
            dxs - arguments to apply Grad

        Returns
        -------
            Scalar result of L operator
        """
        if not a.is_symbol and not a.is_symbol and not f.is_symbol:
            from sympy.abc import t
            return Derivative(f, t) + Unwrap(Transpose(Grad(f, dxs)) * a) + \
                   Rational(1, 2) * Trace(Transpose(b) * Hess(f, dxs) * b)
