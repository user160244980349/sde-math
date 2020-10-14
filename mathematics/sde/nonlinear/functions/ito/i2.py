import sympy as sp


class I2(sp.Function):
    """
    Stochastic Ito integral
    """
    nargs = 3

    def __new__(cls, *args, **kwargs):
        """
        Creates new I2 object with given args

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
            return dt ** sp.Rational(5, 2) / 3 * \
                   (ksi[0, i1] + ksi[1, i1] * sp.sqrt(3) / 2 + ksi[2, i1] / sp.sqrt(5) / 2)
        else:
            return super(I2, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        I2
        """
        return I2(*self.args, **hints)
