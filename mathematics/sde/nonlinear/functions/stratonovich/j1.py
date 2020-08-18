import sympy as sp


class J1(sp.Function):
    """
    Stochastic Stratonovich integral
    """
    nargs = 3

    def __new__(cls, *args, **kwargs):
        """
        Creates new J1 object with given args

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
            return -dt ** sp.Rational(3, 2) / 2 * \
                   (ksi[0, i1] + ksi[1, i1] / sp.sqrt(3))
        else:
            return super(J1, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        J1
        """
        return J1(*self.args, **hints)
