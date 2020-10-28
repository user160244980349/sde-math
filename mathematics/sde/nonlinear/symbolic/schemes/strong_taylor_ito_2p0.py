from sympy import Function, sympify, Add

from mathematics.sde.nonlinear.symbolic.g import G
from mathematics.sde.nonlinear.symbolic.ito.i0 import I0
from mathematics.sde.nonlinear.symbolic.ito.i00 import I00
from mathematics.sde.nonlinear.symbolic.ito.i000 import I000
from mathematics.sde.nonlinear.symbolic.ito.i0000 import I0000
from mathematics.sde.nonlinear.symbolic.ito.i01 import I01
from mathematics.sde.nonlinear.symbolic.ito.i1 import I1
from mathematics.sde.nonlinear.symbolic.ito.i10 import I10
from mathematics.sde.nonlinear.symbolic.l import L


class StrongTaylorIto2p0(Function):
    """
    Strong Taylor 2.0 method
    """
    nargs = 8

    def __new__(cls, *args, **kwargs):
        """
        Creates new StrongTaylorIto2p0 object with given args
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
              for i1 in range(m)],

            *[G(b[:, i1], a[i, 0], dxs) *
              (dt * I0(i1, dt, ksi) + I1(i1, dt, ksi)) -
              L(a, b, b[i, i1], dxs) *
              I1(i1, dt, ksi)
              for i1 in range(m)],

            *[G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs) *
              I000(i1, i2, i3, q[1], dt, ksi)
              for i3 in range(m)
              for i2 in range(m)
              for i1 in range(m)],

                      dt ** 2 / 2 * L(a, b, a[i, 0], dxs),

            *[G(b[:, i1], L(a, b, b[i, i2], dxs), dxs) *
              (I10(i1, i2, q[2], dt, ksi) - I01(i1, i2, q[2], dt, ksi)) -
              L(a, b, G(b[:, i1], b[i, i2], dxs), dxs) * I10(i1, i2, q[2], dt, ksi) +
              G(b[:, i1], G(b[:, i2], a[i, 0], dxs), dxs) *
              (I01(i1, i2, q[2], dt, ksi) + dt * I00(i1, i2, q[0], dt, ksi))
              for i2 in range(m)
              for i1 in range(m)],

            *[G(b[:, i1], G(b[:, i2], G(b[:, i3], b[i, i4], dxs), dxs), dxs) *
              I0000(i1, i2, i3, i4, q[3], dt, ksi)
              for i4 in range(m)
              for i3 in range(m)
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
        return StrongTaylorIto2p0(*self.args, **hints)
