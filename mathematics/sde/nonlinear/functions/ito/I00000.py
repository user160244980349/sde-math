import sympy as sp

from ..coefficients.C00000 import C00000
from ..Ind import Ind


class I00000(sp.Function):
    """
    Iterated stochastic Ito integral
    """
    nargs = 8

    def __new__(cls, *args, **kwargs):
        """
        Creates new I0000 object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i1, i2, i3, i4, i5, q, dt, ksi = sp.sympify(args)
        if isinstance(i1, sp.Number) and isinstance(i2, sp.Number) \
                and isinstance(i3, sp.Number) and isinstance(i4, sp.Number) \
                and isinstance(i5, sp.Number) and isinstance(q, sp.Number) \
                and isinstance(dt, sp.Number):
            j1, j2, j3, j4, j5 = sp.symbols('j1 j2 j3 j4 j5')
            return \
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            sp.Sum(
                                sp.Sum(
                                    C00000(j5, j4, j3, j2, j1, dt) *
                                    (ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] * ksi[j4, i4] * ksi[j5, i5] -
                                     Ind(i1, i2) * Ind(j1, j2) * ksi[j3, i3] * ksi[j4, i4] * ksi[j5, i5] -
                                     Ind(i1, i3) * Ind(j1, j3) * ksi[j2, i2] * ksi[j3, i3] * ksi[j4, i4] -
                                     Ind(i1, i4) * Ind(j1, j4) * ksi[j2, i2] * ksi[j3, i3] * ksi[j5, i5] -
                                     Ind(i1, i5) * Ind(j1, j5) * ksi[j2, i2] * ksi[j3, i3] * ksi[j4, i4] -
                                     Ind(i2, i3) * Ind(j2, j3) * ksi[j1, i1] * ksi[j4, i4] * ksi[j5, i5] -
                                     Ind(i2, i4) * Ind(j2, j4) * ksi[j1, i1] * ksi[j3, i3] * ksi[j5, i5] -
                                     Ind(i2, i5) * Ind(j2, j5) * ksi[j1, i1] * ksi[j3, i3] * ksi[j4, i4] -
                                     Ind(i3, i4) * Ind(j3, j4) * ksi[j1, i1] * ksi[j2, i2] * ksi[j5, i5] -
                                     Ind(i3, i5) * Ind(j3, j5) * ksi[j1, i1] * ksi[j2, i2] * ksi[j4, i4] -
                                     Ind(i4, i5) * Ind(j4, j5) * ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] +
                                     Ind(i1, i2) * Ind(j1, j2) * Ind(i3, i4) * Ind(j3, j4) * ksi[j5, i5] +
                                     Ind(i1, i2) * Ind(j1, j2) * Ind(i3, i5) * Ind(j3, j5) * ksi[j4, i4] +
                                     Ind(i1, i2) * Ind(j1, j2) * Ind(i4, i5) * Ind(j4, j5) * ksi[j3, i3] +
                                     Ind(i1, i3) * Ind(j1, j3) * Ind(i2, i4) * Ind(j2, j4) * ksi[j5, i5] +
                                     Ind(i1, i3) * Ind(j1, j3) * Ind(i2, i5) * Ind(j2, j5) * ksi[j4, i4] +
                                     Ind(i1, i3) * Ind(j1, j3) * Ind(i4, i5) * Ind(j4, j5) * ksi[j2, i2] +
                                     Ind(i1, i4) * Ind(j1, j4) * Ind(i2, i3) * Ind(j2, j3) * ksi[j5, i5] +
                                     Ind(i1, i4) * Ind(j1, j4) * Ind(i2, i5) * Ind(j2, j5) * ksi[j3, i3] +
                                     Ind(i1, i4) * Ind(j1, j4) * Ind(i3, i5) * Ind(j3, j5) * ksi[j2, i2] +
                                     Ind(i1, i5) * Ind(j1, j5) * Ind(i2, i3) * Ind(j2, j3) * ksi[j4, i4] +
                                     Ind(i1, i5) * Ind(j1, j5) * Ind(i2, i4) * Ind(j2, j4) * ksi[j3, i3] +
                                     Ind(i1, i5) * Ind(j1, j5) * Ind(i3, i4) * Ind(j3, j4) * ksi[j2, i2] +
                                     Ind(i2, i3) * Ind(j2, j3) * Ind(i4, i5) * Ind(j4, j5) * ksi[j1, i1] +
                                     Ind(i2, i4) * Ind(j2, j4) * Ind(i3, i5) * Ind(j3, j5) * ksi[j1, i1] +
                                     Ind(i2, i5) * Ind(j2, j5) * Ind(i3, i4) * Ind(j3, j4) * ksi[j1, i1]),
                                    (j5, 0, q)),
                                (j4, 0, q)),
                            (j3, 0, q)),
                        (j2, 0, q)),
                    (j1, 0, q))
        else:
            return super(I00000, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        I00000
        """
        return I00000(*self.args, **hints)
