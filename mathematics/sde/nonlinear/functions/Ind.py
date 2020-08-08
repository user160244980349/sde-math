import sympy as sp


class Ind(sp.Function):
    """
    Stochastic Ito integral
    """
    nargs = 2

    def __new__(cls, *args, **kwargs):
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
        Function evaluation method
        If i1 and i2 are numbers then evaluation performs
        Parameters
        ----------
            i1 - index 1
            i2 - index 2

        Returns
        -------
            Zero or One depending on i1 and i2
        """
        return Ind(*self.args, **hints)
