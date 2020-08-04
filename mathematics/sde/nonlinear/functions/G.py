from sympy import Function, Transpose, MatMul, Matrix, MatrixExpr

from mathematics.sde.nonlinear.functions.Grad import Grad
from mathematics.sde.nonlinear.functions.Unwrap import Unwrap


class G(Function):
    """
    Function to perform G operation with function
    """
    nargs = 3

    is_scalar = True
    is_commutative = True

    @classmethod
    def eval(cls, c, f, dxs):
        """
        Applies G operator on function
        Parameters
        ----------
            c - b matrix column to apply G operator
            f - function to apply operator
            dxs - arguments to apply Grad

        Returns
        -------
            Scalar result of G operator
        """
        if c.is_Matrix and not c.is_symbol and not f.is_symbol:
            return Unwrap(MatMul(Transpose(c), Grad(f, dxs)))


# TODO: beautify output!!!
class G2(MatrixExpr):
    """
    Function to perform G operation with functions column
    """
    is_scalar = False
    is_commutative = False

    @property
    def shape(self):
        """
        Gives a shape of G2 operator result column
        Returns
        -------
            Shape tuple
        """
        return self.arg[1].shape

    @property
    def arg(self):
        return self.args

    def __rpow__(self, other):
        pass

    def __rdiv__(self, other):
        pass

    def __abs__(self):
        pass

    def _entry(self, i, j, **kwargs):
        pass

    def doit(self):
        """
        Applies G operator on functions column
        Parameters
        ----------
            c - b matrix to apply G operator
            f - functions column to apply operator
            dxs - arguments to apply gradient

        Returns
        -------
            Column result of G operator
        """
        args = self.arg
        if args[0].is_Matrix and args[1].is_Matrix and not args[0].is_symbol and not args[1].is_symbol:
            c = args[0]
            f = args[1]
            dxs = args[2]
            return Matrix([G(c, f[i, 0], dxs) for i in range(c.shape[0])])
        else:
            return G2(*args)
