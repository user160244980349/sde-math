import sympy as sp


class Unwrap(sp.Function):
    """
    Simple function to unwrap matrix
    """
    nargs = 1

    def __new__(cls, *args, **kwargs):
        """
        Creates new Unwrap object with given args

        Parameters
        ----------
        args
            contains 1 argument - matrix 1x1 to unwrap
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        m = sp.sympify(args[0])
        if isinstance(m, sp.MatrixExpr):
            return m[0, 0]
        else:
            return super(Unwrap, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        Unwrap
        """
        return Unwrap(*self.args, **hints)
