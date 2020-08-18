import sympy as sp

from mathematics.sde.nonlinear.functions.stratonovich.j00 import J00


class J01(sp.Function):
    """
    Iterated stochastic Stratonovich integral
    """
    nargs = 5

    def __new__(cls, *args, **kwargs):
        """
        Creates new J01 object with given args

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
                dt ** 2 / 4 * (ksi[0, i1] * ksi[1, i2] / sp.sqrt(3) +
                               sp.Sum(
                                   ((i + 1) * ksi[i, i1] * ksi[i + 2, i2] -
                                    (i + 1) * ksi[i + 2, i1] * ksi[i, i2]) /
                                   sp.sqrt((2 * i + 1) * (2 * i + 5)) / (2 * i + 3) -
                                   ksi[i, i1] * ksi[i, i2] / (2 * i - 1) / (2 * i + 3),
                                   (i, 0, q)))
        else:
            return super(J01, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        J01
        """
        return J01(*self.args, **hints)
