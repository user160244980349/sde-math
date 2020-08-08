import sympy as sp


class Unwrap(sp.Function):
    """
    Simple function to unwrap matrix
    """
    nargs = 1

    def __new__(cls, *args, **kwargs):
        m = sp.sympify(args[0])
        if isinstance(m, sp.MatrixExpr):
            return m[0, 0]
        else:
            return super(Unwrap, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Performs modeling with Milstein method with scalar substitutions in cycle
        Parameters
        ----------
            m - matrix to unwrap

        Returns
        -------
            Unwraped matrix
        """
        return Unwrap(*self.args, **hints)
