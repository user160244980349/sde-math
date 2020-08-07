import sympy as sp
from mathematics.sde.nonlinear.functions.CustomFunction import CustomFunction


class Io(CustomFunction):
    """
    Stochastic Ito integral
    """
    nargs = (1, 2, 3)

    dt = None
    ksi = None

    def __new__(cls, *args, **kwargs):
        i1 = args[0]
        
        dt = None
        ksi = None

        if len(args) == 2:
            dt = cls._parse_argument(cls.dt, args[1], sp.Number)
            ksi = cls._parse_argument(cls.ksi, args[1], sp.Matrix)

        if len(args) == 3:
            dt = cls._parse_argument(cls.dt, args[1], sp.Number)
            ksi = cls._parse_argument(cls.ksi, args[2], sp.Matrix)

        obj = super().__new__(cls, i1, dt, ksi)
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
        i1, dt, ksi = self.args
        if i1.is_Number:
            return ksi[0, i1] * sp.sqrt(dt)
        else:
            return Io(i1, dt, ksi)
