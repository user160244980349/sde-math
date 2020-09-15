import sympy as sp

from mathematics.sde.nonlinear.functions.coefficients.c20 import C20
from mathematics.sde.nonlinear.functions.ind import Ind


class I20(sp.Function):
    """
    Stochastic Ito integral
    """
    nargs = 5

    def __new__(cls, *args, **kwargs):
        """
        Creates new I1 object with given args

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
        if isinstance(i1, sp.Number):
            j1, j2 = sp.symbols("j1 j2")
            return \
                sp.Sum(
                    sp.Sum(
                        C20(j2, j1, dt) *
                        (ksi[j1, i1] * ksi[j2, i2] - Ind(i1, i2) * Ind(j1, j2)),
                        (j1, 0, q)),
                    (j2, 0, q))
        else:
            return super(I20, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        I20
        """
        return I20(*self.args, **hints)
