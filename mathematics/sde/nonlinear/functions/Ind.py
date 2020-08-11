import sympy as sp


class Ind(sp.Function):
    """
    Stochastic Ito integral
    """
    nargs = 2

    def __new__(cls, *args, **kwargs):
        """
        Creates new Ind object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i1, i2 = sp.sympify(args)
        if isinstance(i1, sp.Number) and isinstance(i2, sp.Number):
            if i1 == i2:
                return sp.S.One
            else:
                return sp.S.Zero
        else:
            return super(Ind, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        Ind
        """
        return Ind(*self.args, **hints)
