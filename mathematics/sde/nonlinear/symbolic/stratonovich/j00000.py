import sympy as sp

from mathematics.sde.nonlinear.symbolic.coefficients.c00000 import C00000


class J00000(sp.Function):
    """
    Iterated stochastic Stratonovich integral
    """
    nargs = 8

    def __new__(cls, *args, **kwargs):
        """
        Creates new J00000 object with given args

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
        if isinstance(i1, sp.Number) and \
                isinstance(i2, sp.Number) and \
                isinstance(i3, sp.Number) and \
                isinstance(i4, sp.Number) and \
                isinstance(i5, sp.Number) and \
                isinstance(q, sp.Number) and \
                isinstance(dt, sp.Number):
            j1, j2, j3, j4, j5 = sp.symbols("j1 j2 j3 j4 j5")
            return \
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            sp.Sum(
                                sp.Sum(
                                    C00000(j5, j4, j3, j2, j1, dt) *
                                    (ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] * ksi[j4, i4] * ksi[j5, i5]),
                                    (j5, 0, q)),
                                (j4, 0, q)),
                            (j3, 0, q)),
                        (j2, 0, q)),
                    (j1, 0, q))
        else:
            return super(J00000, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        J00000
        """
        return J00000(*self.args, **hints)
