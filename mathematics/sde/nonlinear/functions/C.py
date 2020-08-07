from sympy import Rational, Function, sqrt, pprint

import tools.database as db
from mathematics.sde.nonlinear.c import getc
from mathematics.sde.nonlinear.functions.Cd import Cd


class C(Function):
    """
    Function to perform G operation with function
    """
    nargs = 4

    def __new__(cls, *args, **kwargs):
        """
        Creating method context with sizes of it`s components and symbols
        Parameters
        ----------
            n - a column size
            m - b matrix width
            q - independent random variables dimension size
            dxs - tuple of variables to perform differentiation

        Returns
        -------
            Calculated value or symbolic expression
        """
        obj = super(C, cls).__new__(cls, *args, **kwargs)
        j1, j2, j3, dt = args
        obj.j1, obj.j2, obj.j3, obj.dt = j1, j2, j3, dt
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
        args = self.argv
        j1, j2, j3, dt = args
        if j1.is_Number and j2.is_Number and j3.is_Number and dt.is_Number:
            return sqrt((self.j1 * 2 + 1) * (self.j2 * 2 + 1) * (self.j3 * 2 + 1)) * \
                   dt ** (Rational(3, 2)) * Cd(self.j1, self.j2, self.j3).doit() / 8
        else:
            return C(j1, j2, j3, dt)