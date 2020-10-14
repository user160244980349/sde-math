import sympy as sp

from mathematics.sde.nonlinear.functions.coefficients.c10 import C10
from mathematics.sde.nonlinear.functions.stratonovich.j00 import J00


class J10(sp.Function):
    """
    Iterated stochastic Stratonovich integral
    """
    nargs = 5

    def __new__(cls, *args, **kwargs):
        """
        Creates new J10 object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i1, i2, q, dt, ksi = sp.sympify(args)
        if isinstance(i1, sp.Number) and \
                isinstance(i2, sp.Number) and \
                isinstance(q, sp.Number):
            j1, j2 = sp.symbols("j1 j2")
            from sympy.abc import i
            return sp.Sum(
                sp.Sum(
                    C10(j2, j1, dt) *
                    ksi[j1, i1] * ksi[j2, i2],
                    (j2, 0, q)),
                (j1, 0, q))
        else:
            return super(J10, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        J10
        """
        return J10(*self.args, **hints)


class J10_old(sp.Function):
    """
    Iterated stochastic Stratonovich integral
    """
    nargs = 5

    def __new__(cls, *args, **kwargs):
        """
        Creates new J10 object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i1, i2, q, dt, ksi = sp.sympify(args)
        if isinstance(i1, sp.Number) and isinstance(i2, sp.Number) \
                and isinstance(q, sp.Number):
            from sympy.abc import i
            return \
                -dt / 2 * J00(i1, i2, q, dt, ksi) - \
                dt ** 2 / 4 * (ksi[0, i2] * ksi[1, i1] / sp.sqrt(3) +
                               sp.Sum(
                                   ((i + 1) * ksi[i + 2, i2] * ksi[i, i1] -
                                    (i + 2) * ksi[i, i2] * ksi[i + 2, i1]) /
                                   sp.sqrt((2 * i + 1) * (2 * i + 5)) / (2 * i + 3) +
                                   ksi[i, i1] * ksi[i, i2] / (2 * i - 1) / (2 * i + 3),
                                   (i, 0, q)))
        else:
            return super(J10_old, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        J10
        """
        return J10_old(*self.args, **hints)
