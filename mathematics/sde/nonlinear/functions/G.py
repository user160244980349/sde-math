from sympy import Function, Transpose, MatMul

from mathematics.sde.nonlinear.functions.Grad import Grad


class G(Function):
    nargs = 3

    @classmethod
    def eval(cls, c, f, dx):
        if c.is_Matrix and not c.is_symbol and not f.is_symbol:
            return MatMul(Transpose(c), Grad(f, dx))[0, 0]
