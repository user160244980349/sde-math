import sympy as sp

from .Ioo import Ioo


class Iio(sp.Function):
    """
    Iterated stochastic Ito integral
    """
    nargs = 5

    def __new__(cls, *args, **kwargs):
        i1, i2, q2, dt, ksi = sp.sympify(args)
        if isinstance(i1, sp.Number) and isinstance(i2, sp.Number) \
                and isinstance(q2, sp.Number):
            from sympy.abc import i
            return -dt / 2 * Ioo(i1, i2, q2, dt, ksi) - \
                   dt**2 / 4 * (ksi[0, i2] * ksi[1, i1] / sp.sqrt(3) +
                   sp.Sum(
                       ((i + 1) * ksi[i + 2, i2] * ksi[i, i1] - (i + 2) * ksi[i, i2] * ksi[i + 2, i1]) /
                       sp.sqrt((2 * i + 1) * (2 * i + 5)) / (2 * i + 3) +
                       ksi[i, i1] * ksi[i, i2] / (2 * i - 1) / (2 * i + 3),
                       (i, 0, q2)).doit())
        else:
            return super(Iio, cls).__new__(cls, *args, **kwargs)

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
        return Iio(*self.args, **hints)
