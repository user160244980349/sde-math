import sympy as sp

from .Io import Io


class Euler(sp.Function):
    """
    Milstein method with focus on columns
    """
    nargs = 6

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
        i, yp, a, b, dt, ksi = sp.sympify(args)
        m = b.shape[1]
        i1 = sp.symbols('i1')
        return \
            yp[i, 0] + a[i, 0] * dt + \
            sp.Sum(
                b[i, i1] * Io(i1, dt, ksi),
                (i1, 0, m - 1))
