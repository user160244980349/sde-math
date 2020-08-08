import sympy as sp

from .CustomFunction import CustomFunction


class Io(CustomFunction):
    """
    Stochastic Ito integral
    """
    nargs = (1, 3)

    i1 = None
    dt = None
    ksi = None

    @classmethod
    def _get_defaults(cls):
        return [
            cls.i1,
            cls.dt,
            cls.ksi
        ]

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args)
        return obj

    def doit(self):
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
        i1, dt, ksi = self.validated_args
        if isinstance(i1, sp.Number):
            return ksi[0, i1] * sp.sqrt(dt)
        else:
            return Io(*self.args)
