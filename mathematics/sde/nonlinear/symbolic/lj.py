import sympy as sp

from mathematics.sde.nonlinear.symbolic.operator import Operator


class Lj(Operator):
    """
    L for stratonovich stochastic integral
    """
    nargs = 3

    def __new__(cls, *args, **kwargs):
        """
        Creates new Lj object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        a, f, dxs = sp.sympify(args)
        from sympy.abc import t
        if (isinstance(f, sp.Number) or f.has(*dxs)) and not f.has(Operator):
            n = a.shape[0]
            return sp.diff(f, t) + sum([a[i, 0] * sp.diff(f, dxs[i]) for i in range(n)])
        else:
            return super(Lj, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        Lj
        """
        return Lj(*self.args, **hints)
