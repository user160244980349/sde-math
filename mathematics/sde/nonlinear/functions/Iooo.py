import sympy as sp

from .Ind import Ind
from .Cooo import Cooo


class Iooo(sp.Function):
    """
    Iterated stochastic Ito integral
    """
    nargs = 6

    def __new__(cls, *args, **kwargs):
        i1, i2, i3, q1, dt, ksi = sp.sympify(args)
        if isinstance(i1, sp.Number) and isinstance(i2, sp.Number) \
                and isinstance(i3, sp.Number) and isinstance(q1, sp.Number):
            j1, j2, j3 = sp.symbols('j1 j2 j3')
            return \
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            Cooo(j3, j2, j1, dt) *
                            (ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] -
                             Ind(i1, i2) * Ind(j1, j2) * ksi[j3, i3] -
                             Ind(i1, i3) * Ind(j1, j3) * ksi[j2, i2] -
                             Ind(i2, i3) * Ind(j2, j3) * ksi[j1, i1]),
                            (j3, 0, q1)).doit(),
                        (j2, 0, q1)).doit(),
                    (j1, 0, q1)).doit()
        else:
            return super(Iooo, cls).__new__(cls, *args, **kwargs)

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
        return Iooo(*self.args, **hints)
