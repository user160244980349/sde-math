from sympy import S, Symbol, Function, Sum, sqrt

from mathematics.sde.nonlinear.functions.Ind import Ind


class Ioo(Function):
    """
    Iterated stochastic Ito integral
    """
    nargs = 5

    is_scalar = True
    is_commutative = True

    @classmethod
    def eval(cls, i1, i2, q, dt, ksi):
        """
        Function evaluation method
        If i1, i2, q are numbers then evaluation performs
        Parameters
        ----------
            i1 - index
            dt - delta time
            ksi - matrix of independent random variables

        Returns
        -------
            Calculated value or symbolic expression
        """
        if i1.is_Number and i2.is_Number and q.is_Number:
            i = Symbol('i')
            return dt / 2 * (ksi[0, i1] * ksi[0, i2] +
                             Sum(S(1) / sqrt(S(4) * i ** 2 - 1) * (ksi[i - 1, i1] * ksi[i, i2] -
                                                                   ksi[i, i1] * ksi[i - 1, i2]),
                                 (i, 1, q)).doit() - Ind(i1, i2))
