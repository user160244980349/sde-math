import sympy as sp

from mathematics.sde.nonlinear.functions.ito.i0 import I0


class Euler(sp.Function):
    """
    Euler method
    """
    nargs = 6

    def __new__(cls, *args, **kwargs):
        """
        Creates new Euler object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i, yp, m_a, m_b, dt, ksi = sp.sympify(args)
        n, m = m_b.shape[0], m_b.shape[1]
        a = sp.MatrixSymbol("a", n, 1)
        b = sp.MatrixSymbol("b", n, m)
        i1 = sp.symbols("i1")

        formula = \
            yp[i, 0] + a[i, 0] * dt + \
            sp.Sum(
                b[i, i1] * I0(i1, dt, ksi),
                (i1, 0, m - 1))

        if m_a.is_Matrix and m_b.is_Matrix:
            return formula.subs([(a, m_a), (b, m_b)])
        else:
            return formula

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        sympy.Expr
        """
        return Euler(*self.args, **hints)
