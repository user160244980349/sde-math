from sympy import Add, sympify, Number, diff

from mathematics.sde.nonlinear.symbolic.operator import Operator


class L(Operator):
    """
    Performs L operation on function
    """
    nargs = 4

    def __new__(cls, *args, **kwargs):
        """
        Creates new L object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        a, b, f, dxs = sympify(args)

        if not ((isinstance(f, Number) or f.has(*dxs)) and
                not f.has(Operator) and a.is_Matrix):
            return super(L, cls).__new__(cls, *args, **kwargs)

        n = b.shape[0]
        m = b.shape[1]
        from sympy.abc import t

        return Add(
            diff(f, t),
            *[a[i, 0] * diff(f, dxs[i]) for i in range(n)],
            *[0.5 * b[i, j] * b[k, j] * diff(f, dxs[i], dxs[k])
              for j in range(m)
              for i in range(n)
              for k in range(n)]
        )

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        L
        """
        return L(*self.args, **hints)
