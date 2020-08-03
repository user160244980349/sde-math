from sympy import Function


class Unwrap(Function):
    nargs = 1

    @classmethod
    def eval(cls, m):
        if m.is_Matrix and not m.is_symbol:
            return m[0, 0]
