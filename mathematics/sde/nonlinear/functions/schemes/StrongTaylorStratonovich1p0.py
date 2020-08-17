import sympy as sp

from mathematics.sde.nonlinear.functions.Aj import Aj
from mathematics.sde.nonlinear.functions.G import G
from mathematics.sde.nonlinear.functions.stratonovich.J0 import J0
from mathematics.sde.nonlinear.functions.stratonovich.J00 import J00


class StrongTaylorStratonovich1p0(sp.Function):
    """
    Strong Taylor Stratonovich 1.0 method
    """
    nargs = 8

    def __new__(cls, *args, **kwargs):
        """
        Creates new StrongTaylorStratonovich1p0 object with given args

        Parameters
        ----------
        args
            bunch of necessary arguments
        Returns
        -------
        sympy.Expr
            formula to simplify and substitutions
        """
        i, yp, a, b, q, dt, ksi, dxs = sp.sympify(args)
        m = b.shape[1]
        i1, i2 = sp.symbols("i1 i2")
        aj = Aj(i, a, b, dxs)
        return \
            yp[i, 0] + aj * dt + \
            sp.Sum(
                b[i, i1] * J0(i1, dt, ksi),
                (i1, 0, m - 1)) + \
            sp.Sum(
                sp.Sum(
                    G(b[:, i1], b[i, i2], dxs) *
                    J00(i1, i2, q, dt, ksi),
                    (i2, 0, m - 1)),
                (i1, 0, m - 1))
