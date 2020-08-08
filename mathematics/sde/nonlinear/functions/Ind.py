import sympy as sp


class Ind(sp.Function):
    """
    Stochastic Ito integral
    """
    nargs = 2

    @classmethod
    def eval(cls, i1, i2):
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
        if i1.is_Number and i2.is_Number:
            if i1 == i2:
                return sp.S.One
            else:
                return sp.S.Zero
