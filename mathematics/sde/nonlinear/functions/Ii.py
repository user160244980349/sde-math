from sympy import Function, sqrt, Rational


class Ii(Function):
    """
    Stochastic Ito integral
    """
    nargs = 3

    @classmethod
    def eval(cls, i1, dt, ksi):
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
        if i1.is_Number:
            return -dt**(Rational(3, 2)) / 2 * (ksi[0, i1] + 1 / sqrt(3) * ksi[1, i1])