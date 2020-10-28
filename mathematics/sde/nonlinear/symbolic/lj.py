from sympy import sympify, Number, diff, Add

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
        a, f, dxs = sympify(args)

        if not (isinstance(f, Number) or f.has(*dxs)) and \
                not f.has(Operator):
            return super(Lj, cls).__new__(cls, *args, **kwargs)

        n = a.shape[0]
        from sympy.abc import t
        return Add(diff(f, t), *[a[i, 0] * diff(f, dxs[i])
                                 for i in range(n)])

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        Lj
        """
        return Lj(*self.args, **hints)
