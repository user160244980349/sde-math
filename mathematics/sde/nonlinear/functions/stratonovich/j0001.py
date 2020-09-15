import sympy as sp

from mathematics.sde.nonlinear.functions.coefficients.c0001 import C0001


class J0001(sp.Function):
    """
    Iterated stochastic Ito integral
    """
    nargs = 7

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
        i1, i2, i3, i4, q, dt, ksi = sp.sympify(args)
        if isinstance(i1, sp.Number) and isinstance(i2, sp.Number) \
                and isinstance(i3, sp.Number) and isinstance(i4, sp.Number) \
                and isinstance(q, sp.Number):
            j1, j2, j3, j4 = sp.symbols("j1 j2 j3 j4")
            return \
                sp.Sum(
                    sp.Sum(
                        sp.Sum(
                            sp.Sum(
                                C0001(j4, j3, j2, j1, dt) *
                                ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] * ksi[j4, i4],
                                (j4, 0, q)),
                            (j3, 0, q)),
                        (j2, 0, q)),
                    (j1, 0, q))
        else:
            return super(J0001, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        J0001
        """
        return J0001(*self.args, **hints)
