from sympy import Function, sympify, Add

from mathematics.sde.nonlinear.symbolic.aj import Aj
from mathematics.sde.nonlinear.symbolic.g import G
from mathematics.sde.nonlinear.symbolic.l import L
from mathematics.sde.nonlinear.symbolic.lj import Lj
from mathematics.sde.nonlinear.symbolic.stratonovich.j0 import J0
from mathematics.sde.nonlinear.symbolic.stratonovich.j00 import J00
from mathematics.sde.nonlinear.symbolic.stratonovich.j000 import J000
from mathematics.sde.nonlinear.symbolic.stratonovich.j1 import J1


class StrongTaylorStratonovich1p5(Function):
    """
    Strong Taylor 1.5 method
    """
    nargs = 8

    def __new__(cls, *args, **kwargs):
        """
        Creates new StrongTaylorStratonovich1p5 object with given args

        Parameters
        ----------
        i : int
            component of stochastic process
        yp : numpy.ndarray
            initial conditions
        m_a : numpy.ndarray
            algebraic, given in the variables x and t
        m_b : numpy.ndarray
            algebraic, given in the variables x and t
        dt : float
            integration step
        ksi : numpy.ndarray
            matrix of Gaussian variables
        dxs : tuple
            variables to differentiate
        q : tuple
            amounts of q for integrals approximations

        Returns
        -------
        sympy.Expr
            formula to simplify and substitute
        """
        i, yp, a, b, dt, ksi, dxs, q = sympify(args)
        n, m = b.shape[0], b.shape[1]

        aj = Aj(i, a, b, dxs)

        return Add(

            yp[i, 0], aj[i, 0] * dt,

            *[b[i, i1] * J0(i1, dt, ksi)
              for i1 in range(m)],

            *[G(b[:, i1], b[i, i2], dxs) *
              J00(i1, i2, q[0], dt, ksi)
              for i2 in range(m)
              for i1 in range(m)],

            *[G(b[:, i1], aj[i, 0], dxs) *
              (dt * J0(i1, dt, ksi) + J1(i1, dt, ksi)) -
              Lj(a, b[i, i1], dxs) *
              J1(i1, dt, ksi)
              for i1 in range(m)],

            *[G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs) *
              J000(i1, i2, i3, q[1], dt, ksi)
              for i3 in range(m)
              for i2 in range(m)
              for i1 in range(m)],

                      dt ** 2 / 2 * L(a, b, a[i, 0], dxs)

        )

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        sympy.Expr
        """
        return StrongTaylorStratonovich1p5(*self.args, **hints)
