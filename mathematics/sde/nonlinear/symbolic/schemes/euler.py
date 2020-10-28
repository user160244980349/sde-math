from sympy import Function, sympify, Add

from mathematics.sde.nonlinear.symbolic.ito.i0 import I0


class Euler(Function):
    """
    Euler method
    """
    nargs = 6

    def __new__(cls, *args, **kwargs):
        """
        Creates new Euler object with given args
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
        Returns
        =======
        sympy.Expr
            formula to simplify and substitute
        """
        i, yp, a, b, dt, ksi = sympify(args)
        n, m = b.shape[0], b.shape[1]

        return Add(

            yp[i, 0], a[i, 0] * dt,

            *[b[i, i1] * I0(i1, dt, ksi)
              for i1 in range(m)]

        )

    def doit(self, **hints):
        """
        Tries to expand or calculate function
        Returns
        =======
        sympy.Expr
        """
        return Euler(*self.args, **hints)
