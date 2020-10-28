from sympy import sympify, Matrix, Add

from mathematics.sde.nonlinear.symbolic.g import G
from mathematics.sde.nonlinear.symbolic.operator import Operator


class Aj(Operator):
    """
    A for stratonovich stochastic integral
    """
    nargs = 4

    def __new__(cls, *args, **kwargs):
        """
        Creates new Aj object with given args
        Parameters
        ==========
        args
            bunch of necessary arguments
        Returns
        =======
        sympy.Expr
            formula for simplifications and substitutions
        """
        i, a, b, dxs = sympify(args)
        n = b.shape[0]
        m = b.shape[1]

        return Matrix([a[i, 0] -
                       (Add(*[0.5 * G(b[:, j], b[i, j], dxs)
                              for j in range(m)]))
                       for i in range(n)])
