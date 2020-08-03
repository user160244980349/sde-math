from sympy import Function, Matrix, Derivative


class Grad(Function):
    nargs = 2

    @classmethod
    def eval(cls, f, dxs):
        if not f.is_symbol:
            return Matrix([Derivative(f, dxi) for dxi in dxs])
