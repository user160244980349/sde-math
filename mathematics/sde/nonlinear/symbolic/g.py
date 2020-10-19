import sympy as sp

from mathematics.sde.nonlinear.symbolic.operator import Operator


class G(Operator):
    """
    Performs G operation on function
    """
    nargs = 3

    def __new__(cls, *args, **kwargs):
        """
        Creates new G object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        c, f, dxs = sp.sympify(args)
        if (isinstance(f, sp.Number) or f.has(*dxs)) and not f.has(Operator):
            return sum([c[i, 0] * sp.diff(f, dxs[i]) for i in range(len(dxs))])
        else:
            return super(G, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        G
        """
        return G(*self.args, **hints)
