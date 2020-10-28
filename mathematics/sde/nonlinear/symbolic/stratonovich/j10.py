from sympy import Function, sympify, Number, Add

from mathematics.sde.nonlinear.symbolic.coefficients.c10 import C10


class J10(Function):
    """
    Iterated Stratonovich stochastic integral
    """
    nargs = 5

    def __new__(cls, *args, **kwargs):
        """
        Creates new J10 object with given args

        Parameters
        −−−−−−−−−−
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
        −−−−−−−
        sympy . Expr
            formula to simplify and substitute
        """
        i1, i2, q, dt, ksi = sympify(args)

        if not (isinstance(i1, Number) and
                isinstance(i2, Number) and
                isinstance(q, Number)):
            return super(J10, cls).__new__(cls, *args, **kwargs)

        return Add(*[
            C10(j2, j1, dt) *
            ksi[j1, i1] * ksi[j2, i2]
            for j2 in range(q + 1)
            for j1 in range(q + 1)])

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        J10
        """
        return J10(*self.args, **hints)

# class J10_old(Function):
#     """
#     Iterated stochastic Ito integral
#     """
#     nargs = 5
#
#     def __new__(cls, *args, **kwargs):
#         """
#         Creates new J10 object with given args
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
#         if isinstance(i1, Number) and isinstance(i2, Number) \
#                 and isinstance(q, Number):
#             from sympy.abc import i
#             return \
#                 -dt / 2 * I00(i1, i2, q, dt, ksi) - \
#                 dt ** 2 / 4 * (ksi[0, i2] * ksi[1, i1] / sqrt(3) +
#                                Sum(
#                                    ((i + 1) * ksi[i + 2, i2] * ksi[i, i1] -
#                                     (i + 2) * ksi[i, i2] * ksi[i + 2, i1]) /
#                                    sqrt((2 * i + 1) * (2 * i + 5)) / (2 * i + 3) +
#                                    ksi[i, i1] * ksi[i, i2] / (2 * i - 1) / (2 * i + 3),
#                                    (i, 0, q)))
#         else:
#             return super(J10_old, cls).__new__(cls, *args, **kwargs)
#
#     def doit(self, **hints):
#         """
#         Tries to expand or calculate function
#
#         Returns
#         -------
#         J10
#         """
#         return J10_old(*self.args, **hints)
