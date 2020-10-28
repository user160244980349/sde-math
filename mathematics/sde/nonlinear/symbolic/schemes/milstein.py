from sympy import Function, sympify, Add

from mathematics.sde.nonlinear.symbolic.g import G
from mathematics.sde.nonlinear.symbolic.ito.i0 import I0
from mathematics.sde.nonlinear.symbolic.ito.i00 import I00


class Milstein(Function):
    """
    Milstein method
    """
    nargs = 8

    def __new__(cls, *args, **kwargs):
        """
        Creates new Milstein object with given args
        Parameters
        ==========
        i : int
            component of stochastic process
        yp : numpy.ndarray
            initial conditions
        a : numpy.ndarray
            algebraic, given in the variables x and t
        b : numpy.ndarray
            algebraic, given in the variables x and t
        dt : float
            integration step
        ksi : numpy.ndarray
            matrix of Gaussian variables
        q : tuple
            amounts of q for integrals approximations
        Returns
        =======
        sympy.Expr
            formula to simplify and substitute
        """
        i, yp, a, b, dt, ksi, dxs, q = sympify(args)
        n, m = b.shape[0], b.shape[1]

        return Add(

            yp[i, 0], a[i, 0] * dt,

            *[b[i, i1] * I0(i1, dt, ksi)
              for i1 in range(m)],

            *[G(b[:, i1], b[i, i2], dxs) *
              I00(i1, i2, q[0], dt, ksi)
              for i2 in range(m)
              for i1 in range(m)]

        )

    def doit(self, **hints):
        """
        Tries to expand or calculate function
        Returns
        =======
        sympy.Expr
        """
        return Milstein(*self.args, **hints)
