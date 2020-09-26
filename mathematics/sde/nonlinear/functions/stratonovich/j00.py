import sympy as sp


class J00(sp.Function):
    """
    Iterated stochastic Stratonovich integral
    """
    nargs = 5

    def __new__(cls, *args, **kwargs):
        """
        Creates new J00 object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i1, i2, q, dt, ksi = sp.sympify(args)
        if isinstance(i1, sp.Number) and isinstance(i2, sp.Number) \
                and isinstance(q, sp.Number):
            from sympy.abc import i
            return \
                dt / 2 * (ksi[0, i1] * ksi[0, i2] +
                          sp.Sum(
                              (ksi[i - 1, i1] * ksi[i, i2] -
                               ksi[i, i1] * ksi[i - 1, i2]) /
                              sp.sqrt((i + 1) ** 2 * 4 - 1),
                              (i, 1, q)))
        else:
            return super(J00, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        J00
        """
        return J00(*self.args, **hints)
