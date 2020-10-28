from sympy import Function, Number, sympify, Sum, Add

from mathematics.sde.nonlinear.symbolic.coefficients.c01 import C01
from mathematics.sde.nonlinear.symbolic.ind import Ind


class I01(Function):
    """
    Iterated Ito stochastic integral
    """
    nargs = 5

    def __new__(cls, *args, **kwargs):
        """
        Creates new I01 object with given args
        Parameters
        ==========
        i1 : int
            integral index
        i2 : int
            integral index
        q : int
            amount of terms in approximation of integral
        dt : float
            delta time
        ksi : numpy.ndarray
            matrix of Gaussian variables
        Returns
        =======
        sympy.Expr
            formula to simplify and substitute
        """
        i1, i2, q, dt, ksi = sympify(args)

        if not (isinstance(i1, Number) and
                isinstance(i2, Number) and
                isinstance(q, Number)):
            return super(I01, cls).__new__(cls, *args, **kwargs)

        return Add(*[
            C01(j2, j1, dt) *
            (ksi[j1, i1] * ksi[j2, i2] -
             Ind(i1, i2) * Ind(j1, j2))
            for j2 in range(q + 1)
            for j1 in range(q + 1)])

    def doit(self, **hints):
        """
        Tries to expand or calculate function
        Returns
        =======
        I01
        """
        return I01(*self.args, **hints)


# class I01_old(Function):
#     """
#     Iterated stochastic Ito integral
#     """
#     nargs = 5
#
#     def __new__(cls, *args, **kwargs):
#         """
#         Creates new I01 object with given args
#
#         Parameters
#         ----------
#         args
#             bunch of necessary arguments
#         Returns
#         -------
#         sympy.Expr
#             formula to simplify and substitutions
#         """
#         i1, i2, q, dt, ksi = sympify(args)
#         if isinstance(i1, Number) and \
#                 isinstance(i2, Number) and \
#                 isinstance(q, Number):
#             from sympy.abc import i
#             return \
#                 -dt / 2 * I00(i1, i2, q, dt, ksi) - \
#                 dt ** 2 / 4 * (ksi[0, i1] * ksi[1, i2] / sqrt(3) +
#                                Sum(
#                                    ((i + 1) * ksi[i, i1] * ksi[i + 2, i2] -
#                                     (i + 1) * ksi[i + 2, i1] * ksi[i, i2]) /
#                                    sqrt((2 * i + 1) * (2 * i + 5)) / (2 * i + 3) -
#                                    ksi[i, i1] * ksi[i, i2] / (2 * i - 1) / (2 * i + 3),
#                                    (i, 0, q)))
#         else:
#             return super(I01_old, cls).__new__(cls, *args, **kwargs)
#
#     def doit(self, **hints):
#         """
#         Tries to expand or calculate function
#
#         Returns
#         -------
#         I01
#         """
#         return I01_old(*self.args, **hints)
