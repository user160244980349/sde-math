import sympy as sp

from mathematics.sde.nonlinear.functions.coefficients.c000 import C000


class J000(sp.Function):
    """
    Iterated stochastic Stratonovich integral
    """
    nargs = 6

    def __new__(cls, *args, **kwargs):
        """
        Creates new J000 object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i1, i2, i3, q, dt, ksi = sp.sympify(args)
        if isinstance(i1, sp.Number) and isinstance(i2, sp.Number) \
                and isinstance(i3, sp.Number) and isinstance(q, sp.Number):
            j1, j2, j3 = sp.symbols("j1 j2 j3")
            return \
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            C000(j3, j2, j1, dt) *
                            ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3],
                            (j3, 0, q)),
                        (j2, 0, q)),
                    (j1, 0, q))
        else:
            return super(J000, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        000
        """
        return J000(*self.args, **hints)