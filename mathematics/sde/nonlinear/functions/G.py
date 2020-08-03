from sympy import Function, Transpose, MatMul

from mathematics.sde.nonlinear.functions.Grad import Grad
from mathematics.sde.nonlinear.functions.Unwrap import Unwrap


class G(Function):
    nargs = 3

    @classmethod
    def eval(cls, c, f, dx):
        if c.is_Matrix and not c.is_symbol and not f.is_symbol:
            return Unwrap(MatMul(Transpose(c), Grad(f, dx)))
