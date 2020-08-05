from sympy import Function, Transpose, MatMul, Matrix, MatrixExpr

from mathematics.sde.nonlinear.functions.Grad import Grad
from mathematics.sde.nonlinear.functions.Unwrap import Unwrap


class G(Function):
    """
    Function to perform G operation with function
    """
    nargs = 3

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


class G2(Function, MatrixExpr):
    """
    Function to perform G operation with functions column
    """
    nargs = 3
    is_commutative = True

    rows = None  # type: int
    cols = None  # type: int
    _simplify = None

    def __new__(cls, *args, **kwargs):
        obj = super(G2, cls).__new__(cls, *args, **kwargs)
        obj.rows = args[0].shape[0]
        obj.cols = args[0].shape[1]
        return obj

    def __abs__(self):
        pass

    def __rpow__(self, other):
        pass

    def __rdiv__(self, other):
        pass

    def _entry(self, i, j, **kwargs):
        exp = self.doit()
        return exp[i, j]

    @property
    def shape(self):
        """
        Gives a shape of G2 operator result column
        Returns
        -------
            Shape tuple
        """
        return self._args[1].shape

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
        c, f, dxs = self.args
        if c.is_Matrix and \
                f.is_Matrix and \
                not c.is_symbol and \
                not f.is_symbol:
            return Matrix([G(c, f[i, 0], dxs) for i in range(c.shape[0])])
        else:
            return G2(c, f, dxs)
