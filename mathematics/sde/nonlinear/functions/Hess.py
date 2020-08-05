from sympy import Function, Matrix, Derivative


class Hess(Function):
    """
    Function to perform hessian operation with function
    """

    @classmethod
    def eval(cls, f, dxs):
        """
        Applies hessian operator on function
        Parameters
        ----------
            f - function to apply on
            dxs - arguments to apply gradient

        Returns
        -------
            Matrix of function derivatives
        """
        if not f.is_symbol:
            return Matrix([[Derivative(f, dxi, dxj) for dxi in dxs] for dxj in dxs])
