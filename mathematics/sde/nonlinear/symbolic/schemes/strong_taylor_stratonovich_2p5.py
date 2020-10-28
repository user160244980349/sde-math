from sympy import Function, sympify, Add

from mathematics.sde.nonlinear.symbolic.aj import Aj
from mathematics.sde.nonlinear.symbolic.g import G
from mathematics.sde.nonlinear.symbolic.l import L
from mathematics.sde.nonlinear.symbolic.lj import Lj
from mathematics.sde.nonlinear.symbolic.stratonovich.j0 import J0
from mathematics.sde.nonlinear.symbolic.stratonovich.j00 import J00
from mathematics.sde.nonlinear.symbolic.stratonovich.j000 import J000
from mathematics.sde.nonlinear.symbolic.stratonovich.j0000 import J0000
from mathematics.sde.nonlinear.symbolic.stratonovich.j00000 import J00000
from mathematics.sde.nonlinear.symbolic.stratonovich.j001 import J001
from mathematics.sde.nonlinear.symbolic.stratonovich.j01 import J01
from mathematics.sde.nonlinear.symbolic.stratonovich.j010 import J010
from mathematics.sde.nonlinear.symbolic.stratonovich.j1 import J1
from mathematics.sde.nonlinear.symbolic.stratonovich.j10 import J10
from mathematics.sde.nonlinear.symbolic.stratonovich.j100 import J100
from mathematics.sde.nonlinear.symbolic.stratonovich.j2 import J2


class StrongTaylorStratonovich2p5(Function):
    """
    Strong Taylor 2.5 method
    """
    nargs = 8

    def __new__(cls, *args, **kwargs):
        """
        Creates new StrongTaylorStratonovich2p5 object with given args
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

                      dt ** 2 / 2 * Lj(a, aj[i, 0], dxs),

            *[G(b[:, i1], Lj(a, b[i, i2], dxs), dxs) *
              (J10(i1, i2, q[2], dt, ksi) - J01(i1, i2, q[2], dt, ksi)) -
              Lj(a, G(b[:, i1], b[i, i2], dxs), dxs) * J10(i1, i2, q[2], dt, ksi) +
              G(b[:, i1], G(b[:, i2], aj[i, 0], dxs), dxs) *
              (J01(i1, i2, q[2], dt, ksi) + dt * J00(i1, i2, q[0], dt, ksi))
              for i2 in range(m)
              for i1 in range(m)],

            *[G(b[:, i1], G(b[:, i2], G(b[:, i3], b[i, i4], dxs), dxs), dxs) *
              J0000(i1, i2, i3, i4, q[3], dt, ksi)
              for i4 in range(m)
              for i3 in range(m)
              for i2 in range(m)
              for i1 in range(m)],

            *[G(b[:, i1], Lj(a, aj[i, 0], dxs), dxs) *
              (J2(i1, dt, ksi) / 2 + dt * J1(i1, dt, ksi) + dt ** 2 / 2 * J0(i1, dt, ksi)) +
              Lj(a, Lj(a, b[i, i1], dxs), dxs) * J2(i1, dt, ksi) / 2 -
              Lj(a, G(b[:, i1], aj[i, 0], dxs), dxs) * (J2(i1, dt, ksi) + dt * J1(i1, dt, ksi))
              for i1 in range(m)],

            *[G(b[:, i1], Lj(a, G(b[:, i2], b[i, i3], dxs), dxs), dxs) *
              (J100(i1, i2, i3, q[6], dt, ksi) - J010(i1, i2, i3, q[5], dt, ksi)) +
              G(b[:, i1], G(b[:, i2], Lj(a, b[i, i3], dxs), dxs), dxs) *
              (J010(i1, i2, i3, q[5], dt, ksi) - J001(i1, i2, i3, q[4], dt, ksi)) +
              G(b[:, i1], G(b[:, i2], G(b[:, i3], aj[i, 0], dxs), dxs), dxs) *
              (dt * J000(i1, i2, i3, q[1], dt, ksi) + J001(i1, i2, i3, q[4], dt, ksi)) -
              Lj(a, G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs), dxs) *
              J100(i1, i2, i3, q[6], dt, ksi)
              for i3 in range(m)
              for i2 in range(m)
              for i1 in range(m)],

            *[G(b[:, i1], G(b[:, i2], G(b[:, i3], G(b[:, i4], b[i, i5], dxs), dxs), dxs), dxs) *
              J00000(i1, i2, i3, i4, i5, q[7], dt, ksi)
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
        return StrongTaylorStratonovich2p5(*self.args, **hints)
