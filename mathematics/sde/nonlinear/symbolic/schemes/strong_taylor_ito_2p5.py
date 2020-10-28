from sympy import Function, sympify, Add

from mathematics.sde.nonlinear.symbolic.g import G
from mathematics.sde.nonlinear.symbolic.ito.i0 import I0
from mathematics.sde.nonlinear.symbolic.ito.i00 import I00
from mathematics.sde.nonlinear.symbolic.ito.i000 import I000
from mathematics.sde.nonlinear.symbolic.ito.i0000 import I0000
from mathematics.sde.nonlinear.symbolic.ito.i00000 import I00000
from mathematics.sde.nonlinear.symbolic.ito.i001 import I001
from mathematics.sde.nonlinear.symbolic.ito.i01 import I01
from mathematics.sde.nonlinear.symbolic.ito.i010 import I010
from mathematics.sde.nonlinear.symbolic.ito.i1 import I1
from mathematics.sde.nonlinear.symbolic.ito.i10 import I10
from mathematics.sde.nonlinear.symbolic.ito.i100 import I100
from mathematics.sde.nonlinear.symbolic.ito.i2 import I2
from mathematics.sde.nonlinear.symbolic.l import L


class StrongTaylorIto2p5(Function):
    """
    Strong Taylor 2.5 method
    """
    nargs = 8

    def __new__(cls, *args, **kwargs):
        """
        Creates new StrongTaylorIto2p5 object with given args
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
              for i1 in range(m)],

            *[G(b[:, i1], L(a, b, a[i, 0], dxs), dxs) *
              (I2(i1, dt, ksi) / 2 + dt * I1(i1, dt, ksi) + dt ** 2 / 2 * I0(i1, dt, ksi)) +
              L(a, b, L(a, b, b[i, i1], dxs), dxs) * I2(i1, dt, ksi) / 2 -
              L(a, b, G(b[:, i1], a[i, 0], dxs), dxs) * (I2(i1, dt, ksi) + dt * I1(i1, dt, ksi))
              for i1 in range(m)],

            *[G(b[:, i1], L(a, b, G(b[:, i2], b[i, i3], dxs), dxs), dxs) *
              (I100(i1, i2, i3, q[6], dt, ksi) - I010(i1, i2, i3, q[5], dt, ksi)) +
              G(b[:, i1], G(b[:, i2], L(a, b, b[i, i3], dxs), dxs), dxs) *
              (I010(i1, i2, i3, q[5], dt, ksi) - I001(i1, i2, i3, q[4], dt, ksi)) +
              G(b[:, i1], G(b[:, i2], G(b[:, i3], a[i, 0], dxs), dxs), dxs) *
              (dt * I000(i1, i2, i3, q[1], dt, ksi) + I001(i1, i2, i3, q[4], dt, ksi)) -
              L(a, b, G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs), dxs) *
              I100(i1, i2, i3, q[6], dt, ksi)
              for i3 in range(m)
              for i2 in range(m)
              for i1 in range(m)],

            *[G(b[:, i1], G(b[:, i2], G(b[:, i3], G(b[:, i4], b[i, i5], dxs), dxs), dxs), dxs) *
              I00000(i1, i2, i3, i4, i5, q[7], dt, ksi)
              for i5 in range(m)
              for i4 in range(m)
              for i3 in range(m)
              for i2 in range(m)
              for i1 in range(m)],

                      dt ** 3 / 6 * L(a, b, L(a, b, a[i, 0], dxs), dxs)

        )

    def doit(self, **hints):
        """
        Tries to expand or calculate function
        Returns
        =======
        sympy.Expr
        """
        return StrongTaylorIto2p5(*self.args, **hints)
