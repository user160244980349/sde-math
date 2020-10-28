from sympy import Add, sympify, Number, diff

from mathematics.sde.nonlinear.symbolic.operator import Operator


class G(Operator):
    """
    Performs G operation on function
    """
    nargs = 3

    _dict = dict()

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
        c, f, dxs = sympify(args)

        if not ((isinstance(f, Number) or f.has(*dxs)) and
                not f.has(Operator)):
            return super(G, cls).__new__(cls, *args, **kwargs)

        return Add(*[c[i, 0] * diff(f, dxs[i])
                     for i in range(len(dxs))])

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        G
        """
        return G(*self.args, **hints)
