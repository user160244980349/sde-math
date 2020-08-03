from sympy import Function, Transpose, MatMul


class Unwrap(Function):
    nargs = 3

    @classmethod
    def eval(cls, m):
        if m.is_Matrix and not m.is_symbol:
            return m[0, 0]
