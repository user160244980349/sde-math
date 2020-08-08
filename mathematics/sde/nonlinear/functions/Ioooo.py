import sympy as sp

from .Ind import Ind
from .Coooo import Coooo


class Ioooo(sp.Function):
    """
    Iterated stochastic Ito integral
    """
    nargs = 7

    def __new__(cls, *args, **kwargs):
        i1, i2, i3, i4, q3, dt, ksi = sp.sympify(args)
        if isinstance(i1, sp.Number) and isinstance(i2, sp.Number) \
                and isinstance(i3, sp.Number) and isinstance(q3, sp.Number):
            j1, j2, j3, j4 = sp.symbols('j1 j2 j3 j4')
            return \
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            sp.Sum(
                                Coooo(j4, j3, j2, j1, dt) *
                                (ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] * ksi[j4, i4] -
                                 Ind(i1, i2) * Ind(j1, j2) * ksi[j3, i3] * ksi[j4, i4] -
                                 Ind(i1, i3) * Ind(j1, j3) * ksi[j2, i2] * ksi[j4, i4] -
                                 Ind(i1, i4) * Ind(j1, j4) * ksi[j2, i2] * ksi[j3, i3] -
                                 Ind(i2, i3) * Ind(j2, j3) * ksi[j1, i1] * ksi[j4, i4] -
                                 Ind(i2, i4) * Ind(j2, j4) * ksi[j1, i1] * ksi[j3, i3] -
                                 Ind(i3, i4) * Ind(j3, j4) * ksi[j1, i1] * ksi[j2, i2] +
                                 Ind(i1, i2) * Ind(j1, j2) * Ind(i3, i4) * Ind(j3, j4) +
                                 Ind(i1, i3) * Ind(j1, j3) * Ind(i2, i4) * Ind(j2, j4) +
                                 Ind(i1, i4) * Ind(j1, j4) * Ind(i2, i3) * Ind(j2, j3)),
                                (j4, 0, q3)).doit(),
                            (j3, 0, q3)).doit(),
                        (j2, 0, q3)).doit(),
                    (j1, 0, q3)).doit()
        else:
            return super(Ioooo, cls).__new__(cls, *args, **kwargs)

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
        return Ioooo(*self.args, **hints)
