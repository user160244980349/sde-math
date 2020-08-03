from sympy import S, Function


class Ind(Function):
    nargs = 2

    @classmethod
    def eval(cls, i1, i2):
        if i1.is_Number and i2.is_Number:
            if i1 == i2:
                return S.One
            else:
                return S.Zero
