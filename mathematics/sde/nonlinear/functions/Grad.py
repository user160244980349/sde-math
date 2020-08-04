from sympy import Function, Matrix, Derivative


class Grad(Function):
    """
    Function to perform gradient operation
    """
    nargs = 2

    @classmethod
    def eval(cls, f, dxs):
        """
        Function evaluation method
        If i1 and i2 are numbers then evaluation performs
        Parameters
        ----------
            f - function to apply on
            dxs - arguments to differentiate

        Returns
        -------
            Column of derivatives
        """
        if not f.is_symbol:
            return Matrix([Derivative(f, dxi) for dxi in dxs])
