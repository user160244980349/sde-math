from sympy import sympify, Number, Function


class Ind(Function):
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
        i1, i2 = sympify(args)

        if not (isinstance(i1, Number) and
                isinstance(i2, Number)):
            return super(Ind, cls).__new__(cls, *args, **kwargs)

        if i1 == i2:
            return 1
        else:
            return 0

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        Ind
        """
        return Ind(*self.args, **hints)
