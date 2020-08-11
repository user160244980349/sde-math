import sympy as sp


class I0(sp.Function):
    """
    Stochastic Ito integral
    """
    nargs = 3

    def __new__(cls, *args, **kwargs):
        """
        Creates new I0 object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i1, dt, ksi = sp.sympify(args)
        if isinstance(i1, sp.Number):
            return ksi[0, i1] * sp.sqrt(dt)
        else:
            return super(I0, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        I0
        """
        return I0(*self.args, **hints)
