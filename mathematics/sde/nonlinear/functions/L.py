from sympy import S, Function, Matrix, Symbol, Transpose, Trace

from mathematics.sde.nonlinear.functions.Grad import Grad
from mathematics.sde.nonlinear.functions.Hess import Hess
from mathematics.sde.nonlinear.helpers import unwrap_1x1_matrix


class L(Function):
    nargs = 4

    @classmethod
    def eval(cls, f, a, b, dx):
        if f.is_Expr:
            t = Symbol('t')
            return f.diff(t) + unwrap_1x1_matrix(Transpose(Grad(f, dx)) * a) \
                   + S(1) / 2 * Trace(Transpose(b) * Hess(f, dx) * b)


class L2(Function):
    nargs = 4

    @classmethod
    def eval(cls, f, a, b, dx):
        if f.is_Matrix:
            return Matrix([f2 for f2 in [L(f1, b, dx) for f1 in f]])
