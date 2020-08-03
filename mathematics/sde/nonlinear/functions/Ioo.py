from sympy import S, Symbol, Function, Sum, sqrt

from mathematics.sde.nonlinear.functions.Ind import Ind


class Ioo(Function):
    nargs = 5

    @classmethod
    def eval(cls, i1, i2, q, dt, ksi):
        if i1.is_Number and i2.is_Number and q.is_Number:
            i = Symbol('i')
            return dt / 2 * \
                   (ksi[0, i1] * ksi[0, i2] +
                    Sum(S(1) / sqrt(S(4) * i ** 2 - 1) *
                        (ksi[i - 1, i1] * ksi[i, i2] -
                         ksi[i, i1] * ksi[i - 1, i2]),
                        (i, 1, q - 1)).doit() - Ind(i1, i2))
