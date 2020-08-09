import sympy as sp

from .Ind import Ind


class Ioo(sp.Function):
    """
    Iterated stochastic Ito integral
    """
    nargs = 5

    def __new__(cls, *args, **kwargs):
        i1, i2, q, dt, ksi = sp.sympify(args)
        if isinstance(i1, sp.Number) and isinstance(i2, sp.Number) \
                and isinstance(q, sp.Number):
            from sympy.abc import i
            return dt / 2 * (ksi[0, i1] * ksi[0, i2] +
                             sp.Sum(
                                 (ksi[i - 1, i1] * ksi[i, i2] -
                                  ksi[i, i1] * ksi[i - 1, i2]) /
                                 sp.sqrt(i ** 2 * 4 - 1),
                                 (i, 1, q)) - Ind(i1, i2))
        else:
            return super(Ioo, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
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
        return Ioo(*self.args, **hints)
