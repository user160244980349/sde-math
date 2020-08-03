from sympy import Function, Matrix, Expr, derive_by_array


class Hess(Function):
    @classmethod
    def eval(cls, f: Expr, dx):
        return Matrix(derive_by_array(derive_by_array(f, dx), dx))
