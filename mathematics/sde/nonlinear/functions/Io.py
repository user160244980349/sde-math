import sympy as sp


class Io(sp.Function):
    """
    Stochastic Ito integral
    """
    nargs = 3

    def __new__(cls, *args, **kwargs):
        i1, dt, ksi = sp.sympify(args)
        if isinstance(i1, sp.Number):
            return ksi[0, i1] * sp.sqrt(dt)
        else:
            return super(Io, cls).__new__(cls, *args, **kwargs)

    def doit(self, **hints):
        """
        Function evaluation method
        If i1 is number then evaluation performs

        Parameters
        ----------
            i1 - index
            dt - delta time
            ksi - matrix of independent random variables

        Returns
        -------
            Calculated value or symbolic expression
        """
        return Io(*self.args, **hints)
