import sympy as sp

from mathematics.sde.nonlinear.functions.operator import Operator


class L(Operator):
    """
    Performs L operation on function
    """
    nargs = 4

    def __new__(cls, *args, **kwargs):
        """
        Creates new L object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        a, b, f, dxs = sp.sympify(args)
        if (isinstance(f, sp.Number) or f.has(*dxs)) and not f.has(Operator) and a.is_Matrix:
            n = b.shape[0]
            m = b.shape[1]
            from sympy.abc import t
            return \
                sp.diff(f, t) + \
                sum([a[i, 0] * sp.diff(f, dxs[i]) for i in range(n)]) + \
                sum([sp.Rational(1, 2) * b[i, j] * b[k, j] * sp.diff(f, dxs[i], dxs[k])
                     for j in range(m)
                     for i in range(n)
                     for k in range(n)])
        else:
            return super(L, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        L
        """
        return L(*self.args, **hints)
