from sympy import Function, sqrt


class Io(Function):
    nargs = 3

    @classmethod
    def eval(cls, i1, dt, ksi):
        if i1.is_Number:
            return ksi[0, i1] * sqrt(dt)
