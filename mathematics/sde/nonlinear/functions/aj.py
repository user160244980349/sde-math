import sympy as sp

from mathematics.sde.nonlinear.functions.g import G
from mathematics.sde.nonlinear.functions.operator import Operator


class Aj(Operator):
    """
    A for stratonovich stochastic integral
    """
    nargs = 4

    def __new__(cls, *args, **kwargs):
        """
        Creates new Aj object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula for simplifications and substitutions
        """
        i, a, b, dxs = sp.sympify(args)
        n = b.shape[0]
        m = b.shape[1]
        sym_a = sp.MatrixSymbol("a", n, 1)
        sym_b = sp.MatrixSymbol("b", n, m)
        return sp.Matrix([sym_a[i, 0] -
                          (sum([sp.Rational(1, 2) * G(sym_b[:, j], sym_b[i, j], dxs)
                                for j in range(m)]))
                          for i in range(n)]).subs([(sym_a, a), (sym_b, b)])
