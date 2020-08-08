import sympy as sp

from .Cd import Cd
from .CustomFunction import CustomFunction


class C(CustomFunction):
    """
    Function to perform G operation with function
    """
    nargs = (3, 4)

    j1 = None
    j2 = None
    j3 = None
    dt = None

    @classmethod
    def _get_defaults(cls):
        return [
            cls.j1,
            cls.j2,
            cls.j3,
            cls.dt
        ]

    def __new__(cls, *args, **kwargs):
        obj = super(C, cls).__new__(cls, *args, **kwargs)
        return obj

    @property
    def argv(self):
        return self.args

    def doit(self):
        """
        Applies G operator on function
        Parameters
        ----------
            c - b matrix column to apply G operator
            f - function to apply operator
            dxs - arguments to apply Grad

        Returns
        -------
            Scalar result of G operator
        """
        j1, j2, j3, dt = self.validated_args
        if isinstance(j1, sp.Number) and isinstance(j2, sp.Number) and \
                isinstance(j3, sp.Number) and isinstance(dt, sp.Number):
            return sp.sqrt((j1 * 2 + 1) * (j2 * 2 + 1) * (j3 * 2 + 1)) * \
                   dt ** (sp.Rational(3, 2)) * Cd(j1, j2, j3).doit() / 8
        else:
            return C(*self.args)
