import sympy as sp

from mathematics.sde.nonlinear.symbolic.coefficients.c000000 import C000000
from mathematics.sde.nonlinear.symbolic.ind import Ind


class I000000(sp.Function):
    """
    Iterated stochastic Ito integral
    """
    nargs = 9

    def __new__(cls, *args, **kwargs):
        """
        Creates new I000000 object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i1, i2, i3, i4, i5, i6, q, dt, ksi = sp.sympify(args)
        if isinstance(i1, sp.Number) and \
                isinstance(i2, sp.Number) and \
                isinstance(i3, sp.Number) and \
                isinstance(i4, sp.Number) and \
                isinstance(i5, sp.Number) and \
                isinstance(i6, sp.Number) and \
                isinstance(q, sp.Number) and \
                isinstance(dt, sp.Number):
            j1, j2, j3, j4, j5, j6 = sp.symbols("j1 j2 j3 j4 j5 j6")
            return \
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            sp.Sum(
                                sp.Sum(
                                    sp.Sum(
                                        C000000(j6, j5, j4, j3, j2, j1, dt) *
                                        (ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] *
                                         ksi[j4, i4] * ksi[j5, i5] * ksi[j6, i6] -
                                         Ind(j1, j6) * Ind(i1, i6) * ksi[j2, i2] * ksi[j3, i3] * ksi[j4, i4] * ksi[
                                             j5, i5] -
                                         Ind(j2, j6) * Ind(i2, i6) * ksi[j1, i1] * ksi[j3, i3] * ksi[j4, i4] * ksi[
                                             j5, i5] -
                                         Ind(j3, j6) * Ind(i3, i6) * ksi[j1, i1] * ksi[j2, i2] * ksi[j4, i4] * ksi[
                                             j5, i5] -
                                         Ind(j4, j6) * Ind(i4, i6) * ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] * ksi[
                                             j5, i5] -
                                         Ind(j5, j6) * Ind(i5, i6) * ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] * ksi[
                                             j4, i4] -
                                         Ind(j1, j2) * Ind(i1, i2) * ksi[j3, i3] * ksi[j4, i4] * ksi[j5, i5] * ksi[
                                             j6, i6] -
                                         Ind(j1, j3) * Ind(i1, i3) * ksi[j2, i2] * ksi[j4, i4] * ksi[j5, i5] * ksi[
                                             j6, i6] -
                                         Ind(j1, j4) * Ind(i1, i4) * ksi[j2, i2] * ksi[j3, i3] * ksi[j5, i5] * ksi[
                                             j6, i6] -
                                         Ind(j1, j5) * Ind(i1, i5) * ksi[j2, i2] * ksi[j4, i4] * ksi[j3, i3] * ksi[
                                             j6, i6] -
                                         Ind(j2, j3) * Ind(i2, i3) * ksi[j1, i1] * ksi[j4, i4] * ksi[j5, i5] * ksi[
                                             j6, i6] -
                                         Ind(j2, j4) * Ind(i2, i4) * ksi[j1, i1] * ksi[j3, i3] * ksi[j5, i5] * ksi[
                                             j6, i6] -
                                         Ind(j2, j5) * Ind(i2, i5) * ksi[j1, i1] * ksi[j3, i3] * ksi[j4, i4] * ksi[
                                             j6, i6] -
                                         Ind(j3, j4) * Ind(i3, i4) * ksi[j1, i1] * ksi[j2, i2] * ksi[j5, i5] * ksi[
                                             j6, i6] -
                                         Ind(j3, j5) * Ind(i3, i5) * ksi[j1, i1] * ksi[j2, i2] * ksi[j4, i4] * ksi[
                                             j6, i6] -
                                         Ind(j4, j5) * Ind(i4, i5) * ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] * ksi[
                                             j6, i6] +
                                         Ind(j1, j2) * Ind(i1, i2) * Ind(j3, j4) * Ind(i3, i4) * ksi[j5, i5] * ksi[
                                             j6, i6] +
                                         Ind(j1, j2) * Ind(i1, i2) * Ind(j3, j5) * Ind(i3, i5) * ksi[j4, i4] * ksi[
                                             j6, i6] +
                                         Ind(j1, j2) * Ind(i1, i2) * Ind(j4, j5) * Ind(i4, i5) * ksi[j3, i3] * ksi[
                                             j6, i6] +
                                         Ind(j1, j3) * Ind(i1, i3) * Ind(j2, j4) * Ind(i2, i4) * ksi[j5, i5] * ksi[
                                             j6, i6] +
                                         Ind(j1, j3) * Ind(i1, i3) * Ind(j2, j5) * Ind(i2, i5) * ksi[j4, i4] * ksi[
                                             j6, i6] +
                                         Ind(j1, j3) * Ind(i1, i3) * Ind(j4, j5) * Ind(i4, i5) * ksi[j2, i2] * ksi[
                                             j6, i6] +
                                         Ind(j1, j4) * Ind(i1, i4) * Ind(j2, j3) * Ind(i2, i3) * ksi[j5, i5] * ksi[
                                             j6, i6] +
                                         Ind(j1, j4) * Ind(i1, i4) * Ind(j2, j5) * Ind(i2, i5) * ksi[j3, i3] * ksi[
                                             j6, i6] +
                                         Ind(j1, j4) * Ind(i1, i4) * Ind(j3, j5) * Ind(i3, i5) * ksi[j2, i2] * ksi[
                                             j6, i6] +
                                         Ind(j1, j5) * Ind(i1, i5) * Ind(j2, j3) * Ind(i2, i3) * ksi[j4, i4] * ksi[
                                             j6, i6] +
                                         Ind(j1, j5) * Ind(i1, i5) * Ind(j2, j4) * Ind(i2, i4) * ksi[j3, i3] * ksi[
                                             j6, i6] +
                                         Ind(j1, j5) * Ind(i1, i5) * Ind(j3, j4) * Ind(i3, i4) * ksi[j2, i2] * ksi[
                                             j6, i6] +
                                         Ind(j2, j3) * Ind(i2, i3) * Ind(j4, j5) * Ind(i4, i5) * ksi[j1, i1] * ksi[
                                             j6, i6] +
                                         Ind(j2, j4) * Ind(i2, i4) * Ind(j3, j5) * Ind(i3, i5) * ksi[j1, i1] * ksi[
                                             j6, i6] +
                                         Ind(j2, j5) * Ind(i2, i5) * Ind(j3, j4) * Ind(i3, i4) * ksi[j1, i1] * ksi[
                                             j6, i6] +
                                         Ind(j6, j1) * Ind(i6, i1) * Ind(j3, j4) * Ind(i3, i4) * ksi[j2, i2] * ksi[
                                             j5, i5] +
                                         Ind(j6, j1) * Ind(i6, i1) * Ind(j3, j5) * Ind(i3, i5) * ksi[j2, i2] * ksi[
                                             j4, i4] +
                                         Ind(j6, j1) * Ind(i6, i1) * Ind(j2, j5) * Ind(i2, i5) * ksi[j3, i3] * ksi[
                                             j4, i4] +
                                         Ind(j6, j1) * Ind(i6, i1) * Ind(j2, j4) * Ind(i2, i4) * ksi[j3, i3] * ksi[
                                             j5, i5] +
                                         Ind(j6, j1) * Ind(i6, i1) * Ind(j4, j5) * Ind(i4, i5) * ksi[j2, i2] * ksi[
                                             j3, i3] +
                                         Ind(j6, j1) * Ind(i6, i1) * Ind(j2, j3) * Ind(i2, i3) * ksi[j4, i4] * ksi[
                                             j5, i5] +
                                         Ind(j6, j2) * Ind(i6, i2) * Ind(j3, j5) * Ind(i3, i5) * ksi[j1, i1] * ksi[
                                             j4, i4] +
                                         Ind(j6, j2) * Ind(i6, i2) * Ind(j4, j5) * Ind(i4, i5) * ksi[j1, i1] * ksi[
                                             j3, i3] +
                                         Ind(j6, j2) * Ind(i6, i2) * Ind(j3, j4) * Ind(i3, i4) * ksi[j1, i1] * ksi[
                                             j5, i5] +
                                         Ind(j6, j2) * Ind(i6, i2) * Ind(j1, j5) * Ind(i1, i5) * ksi[j3, i3] * ksi[
                                             j4, i4] +
                                         Ind(j6, j2) * Ind(i6, i2) * Ind(j1, j4) * Ind(i1, i4) * ksi[j3, i3] * ksi[
                                             j5, i5] +
                                         Ind(j6, j2) * Ind(i6, i2) * Ind(j1, j3) * Ind(i1, i3) * ksi[j4, i4] * ksi[
                                             j5, i5] +
                                         Ind(j6, j3) * Ind(i6, i3) * Ind(j2, j5) * Ind(i2, i5) * ksi[j1, i1] * ksi[
                                             j4, i4] +
                                         Ind(j6, j3) * Ind(i6, i3) * Ind(j4, j5) * Ind(i4, i5) * ksi[j1, i1] * ksi[
                                             j2, i2] +
                                         Ind(j6, j3) * Ind(i6, i3) * Ind(j2, j4) * Ind(i2, i4) * ksi[j1, i1] * ksi[
                                             j5, i5] +
                                         Ind(j6, j3) * Ind(i6, i3) * Ind(j1, j5) * Ind(i1, i5) * ksi[j2, i2] * ksi[
                                             j4, i4] +
                                         Ind(j6, j3) * Ind(i6, i3) * Ind(j1, j4) * Ind(i1, i4) * ksi[j2, i2] * ksi[
                                             j5, i5] +
                                         Ind(j6, j3) * Ind(i6, i3) * Ind(j1, j2) * Ind(i1, i2) * ksi[j4, i4] * ksi[
                                             j5, i5] +
                                         Ind(j6, j4) * Ind(i6, i4) * Ind(j3, j5) * Ind(i3, i5) * ksi[j1, i1] * ksi[
                                             j2, i2] +
                                         Ind(j6, j4) * Ind(i6, i4) * Ind(j2, j5) * Ind(i2, i5) * ksi[j1, i1] * ksi[
                                             j3, i3] +
                                         Ind(j6, j4) * Ind(i6, i4) * Ind(j2, j3) * Ind(i2, i3) * ksi[j1, i1] * ksi[
                                             j5, i5] +
                                         Ind(j6, j4) * Ind(i6, i4) * Ind(j1, j5) * Ind(i1, i5) * ksi[j2, i2] * ksi[
                                             j3, i3] +
                                         Ind(j6, j4) * Ind(i6, i4) * Ind(j1, j3) * Ind(i1, i3) * ksi[j2, i2] * ksi[
                                             j5, i5] +
                                         Ind(j6, j4) * Ind(i6, i4) * Ind(j1, j2) * Ind(i1, i2) * ksi[j3, i3] * ksi[
                                             j5, i5] +
                                         Ind(j6, j5) * Ind(i6, i5) * Ind(j3, j4) * Ind(i3, i4) * ksi[j1, i1] * ksi[
                                             j2, i2] +
                                         Ind(j6, j5) * Ind(i6, i5) * Ind(j2, j4) * Ind(i2, i4) * ksi[j1, i1] * ksi[
                                             j3, i3] +
                                         Ind(j6, j5) * Ind(i6, i5) * Ind(j2, j3) * Ind(i2, i3) * ksi[j1, i4] * ksi[
                                             j1, i4] +
                                         Ind(j6, j5) * Ind(i6, i5) * Ind(j1, j4) * Ind(i1, i4) * ksi[j2, i2] * ksi[
                                             j3, i3] +
                                         Ind(j6, j5) * Ind(i6, i5) * Ind(j1, j3) * Ind(i1, i3) * ksi[j2, i2] * ksi[
                                             j4, i4] +
                                         Ind(j6, j5) * Ind(i6, i5) * Ind(j1, j2) * Ind(i1, i2) * ksi[j3, i3] * ksi[
                                             j4, i4] -
                                         Ind(j6, j1) * Ind(i6, i1) * Ind(j2, j5) * Ind(i2, i5) * Ind(j3, j4) * Ind(i3,
                                                                                                                   i4) -
                                         Ind(j6, j1) * Ind(i6, i1) * Ind(j2, j4) * Ind(i2, i4) * Ind(j3, j5) * Ind(i3,
                                                                                                                   i5) -
                                         Ind(j6, j1) * Ind(i6, i1) * Ind(j2, j3) * Ind(i2, i3) * Ind(j4, j5) * Ind(i4,
                                                                                                                   i5) -
                                         Ind(j6, j2) * Ind(i6, i2) * Ind(j1, j5) * Ind(i1, i5) * Ind(j3, j4) * Ind(i3,
                                                                                                                   i4) -
                                         Ind(j6, j2) * Ind(i6, i2) * Ind(j1, j4) * Ind(i1, i4) * Ind(j3, j5) * Ind(i3,
                                                                                                                   i5) -
                                         Ind(j6, j2) * Ind(i6, i2) * Ind(j1, j3) * Ind(i1, i3) * Ind(j4, j5) * Ind(i4,
                                                                                                                   i5) -
                                         Ind(j6, j3) * Ind(i6, i3) * Ind(j1, j5) * Ind(i1, i5) * Ind(j2, j4) * Ind(i2,
                                                                                                                   i4) -
                                         Ind(j6, j3) * Ind(i6, i3) * Ind(j1, j4) * Ind(i1, i4) * Ind(j2, j5) * Ind(i2,
                                                                                                                   i5) -
                                         Ind(j3, j6) * Ind(i3, i6) * Ind(j1, j2) * Ind(i1, i2) * Ind(j4, j5) * Ind(i4,
                                                                                                                   i5) -
                                         Ind(j6, j4) * Ind(i6, i4) * Ind(j1, j5) * Ind(i1, i5) * Ind(j2, j3) * Ind(i2,
                                                                                                                   i3) -
                                         Ind(j6, j4) * Ind(i6, i4) * Ind(j1, j3) * Ind(i1, i3) * Ind(j2, j5) * Ind(i2,
                                                                                                                   i5) -
                                         Ind(j6, j4) * Ind(i6, i4) * Ind(j1, j2) * Ind(i1, i2) * Ind(j3, j5) * Ind(i3,
                                                                                                                   i5) -
                                         Ind(j6, j5) * Ind(i6, i5) * Ind(j1, j4) * Ind(i1, i4) * Ind(j2, j3) * Ind(i2,
                                                                                                                   i3) -
                                         Ind(j6, j5) * Ind(i6, i5) * Ind(j1, j2) * Ind(i1, i2) * Ind(j3, j4) * Ind(i3,
                                                                                                                   i4) -
                                         Ind(j6, j5) * Ind(i6, i5) * Ind(j1, j3) * Ind(i1, i3) * Ind(j2, j4) * Ind(i2,
                                                                                                                   i4)),
                                        (j6, 0, q)),
                                    (j5, 0, q)),
                                (j4, 0, q)),
                            (j3, 0, q)),
                        (j2, 0, q)),
                    (j1, 0, q))
        else:
            return super(I000000, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        I000000
        """
        return I000000(*self.args, **hints)
