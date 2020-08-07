from sympy import S, Function, Sum, sqrt, symbols, pprint

from mathematics.sde.nonlinear.functions.Ind import Ind
from mathematics.sde.nonlinear.functions.C import C
from mathematics.sde.nonlinear.functions.Cd import Cd


class Iooo(Function):
    """
    Iterated stochastic Ito integral
    """
    nargs = 6

    @classmethod
    def eval(cls, i1, i2, i3, q1, dt, ksi):
        """
        Function evaluation method
        If i1, i2, q are numbers then evaluation performs
        Parameters
        ----------
            i1 - index
            dt - delta time
            ksi - matrix of independent random variables

        Returns
        -------
            Calculated value or symbolic expression
        """
        if i1.is_Number and i2.is_Number and i3.is_Number and q1.is_Number:
            j1, j2, j3 = symbols('j1 j2 j3')
            return \
                Sum(
                    Sum(
                        Sum(C(j1, j2, j3, dt).doit() *
                            (ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] -
                             Ind(i1, i2) * Ind(j1, j2) * ksi[j3, i3] -
                             Ind(i1, i3) * Ind(j1, j3) * ksi[j2, i2] -
                             Ind(i2, i3) * Ind(j2, j3) * ksi[j1, i1]),
                            (j3, 0, q1 - 1)).doit(),
                        (j2, 0, q1 - 1)).doit(),
                    (j1, 0, q1 - 1)).doit()
