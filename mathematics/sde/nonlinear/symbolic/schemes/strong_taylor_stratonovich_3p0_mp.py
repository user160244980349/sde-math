from multiprocessing import Pool, cpu_count

from sympy import Function, sympify, Add, S

from mathematics.sde.nonlinear.symbolic.aj import Aj
from mathematics.sde.nonlinear.symbolic.g import G
from mathematics.sde.nonlinear.symbolic.stratonovich.j0 import J0
from mathematics.sde.nonlinear.symbolic.stratonovich.j00 import J00


class _Routine:

    def __init__(self, i, b, dt, ksi):
        self.i, self.b = i, b
        self.dt, self.ksi = dt, ksi

    def __call__(self, x):
        return S.one


class _Routine1(_Routine):
    def __init__(self, i, b, dt, ksi):
        super().__init__(i, b, dt, ksi)

    def __call__(self, range_of_indices):
        i, b, dt, ksi = self.i, self.b, self.dt, self.ksi
        return Add(
            *[b[i, i1] * J0(i1, dt, ksi)
              for i1 in range(range_of_indices)])


class _Routine2(_Routine):
    def __init__(self, i, b, q, dt, ksi, dxs):
        super().__init__(i, b, dt, ksi)
        self.q = q
        self.dxs = dxs

    def __call__(self, range_of_indices):
        i, b, q, dt, ksi, dxs = \
            self.i, self.b, self.q, self.dt, self.ksi, self.dxs
        return Add(
            *[G(b[:, i1], b[i, i2], dxs) *
              J00(i1, i2, q, dt, ksi)
              for i2 in range(range_of_indices[0])
              for i1 in range(range_of_indices[1])])


class _Routine3(_Routine):
    def __init__(self, i, b, q, dt, ksi):
        super().__init__(i, b, q, dt, ksi)

    def __call__(self, range_of_indices):
        # *[G(b[:, i1], aj[i, 0], dxs) *
        #   (dt * J0(i1, dt, ksi) + J1(i1, dt, ksi)) -
        #   Lj(a, b[i, i1], dxs) *
        #   J1(i1, dt, ksi)
        #   for i1 in range(m)],
        return S.one


class _Routine4(_Routine):
    def __init__(self, i, b, q, dt, ksi):
        super().__init__(i, b, q, dt, ksi)

    def __call__(self, range_of_indices):
        # *[G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs) *
        #   J000(i1, i2, i3, q[1], dt, ksi)
        #   for i3 in range(m)
        #   for i2 in range(m)
        #   for i1 in range(m)],
        return S.one


class _Routine5(_Routine):
    def __init__(self, i, b, q, dt, ksi):
        super().__init__(i, b, q, dt, ksi)

    def __call__(self, range_of_indices):
        # *[G(b[:, i1], Lj(a, b[i, i2], dxs), dxs) *
        #   (J10(i1, i2, q[2], dt, ksi) - J01(i1, i2, q[2], dt, ksi)) -
        #   Lj(a, G(b[:, i1], b[i, i2], dxs), dxs) * J10(i1, i2, q[2], dt, ksi) +
        #   G(b[:, i1], G(b[:, i2], aj[i, 0], dxs), dxs) *
        #   (J01(i1, i2, q[2], dt, ksi) + dt * J00(i1, i2, q[0], dt, ksi))
        #   for i2 in range(m)
        #   for i1 in range(m)],
        return S.one


class _Routine6(_Routine):
    def __init__(self, i, b, q, dt, ksi):
        super().__init__(i, b, q, dt, ksi)

    def __call__(self, range_of_indices):
        # *[G(b[:, i1], G(b[:, i2], G(b[:, i3], b[i, i4], dxs), dxs), dxs) *
        #   J0000(i1, i2, i3, i4, q[3], dt, ksi)
        #   for i4 in range(m)
        #   for i3 in range(m)
        #   for i2 in range(m)
        #   for i1 in range(m)],
        return S.one


class _Routine7(_Routine):
    def __init__(self, i, b, q, dt, ksi):
        super().__init__(i, b, q, dt, ksi)

    def __call__(self, range_of_indices):
        # *[G(b[:, i1], Lj(a, aj[i, 0], dxs), dxs) *
        #   (J2(i1, dt, ksi) / 2 + dt * J1(i1, dt, ksi) + dt ** 2 / 2 * J0(i1, dt, ksi)) +
        #   Lj(a, Lj(a, b[i, i1], dxs), dxs) * J2(i1, dt, ksi) / 2 -
        #   Lj(a, G(b[:, i1], aj[i, 0], dxs), dxs) * (J2(i1, dt, ksi) + dt * J1(i1, dt, ksi))
        #   for i1 in range(m)],
        return S.one


class _Routine8(_Routine):
    def __init__(self, i, b, q, dt, ksi):
        super().__init__(i, b, q, dt, ksi)

    def __call__(self, range_of_indices):
        # *[
        # G(b[:, i1], Lj(a, G(b[:, i2], b[i, i3], dxs), dxs), dxs) *
        # (J100(i1, i2, i3, q[6], dt, ksi) - J010(i1, i2, i3, q[5], dt, ksi)) +
        # G(b[:, i1], G(b[:, i2], Lj(a, b[i, i3], dxs), dxs), dxs) *
        # (J010(i1, i2, i3, q[5], dt, ksi) - J001(i1, i2, i3, q[4], dt, ksi)) +
        # G(b[:, i1], G(b[:, i2], G(b[:, i3], aj[i, 0], dxs), dxs), dxs) *
        # (dt * J000(i1, i2, i3, q[1], dt, ksi) + J001(i1, i2, i3, q[4], dt, ksi)) -
        # Lj(a, G(b[:, i1], G(b[:, i2], b[i, i3], dxs), dxs), dxs) *
        # J100(i1, i2, i3, q[6], dt, ksi)
        # for i3 in range(m)
        # for i2 in range(m)
        # for i1 in range(m)],
        return S.one


class _Routine9(_Routine):
    def __init__(self, i, b, q, dt, ksi):
        super().__init__(i, b, q, dt, ksi)

    def __call__(self, range_of_indices):
        # *[G(b[:, i1], G(b[:, i2], G(b[:, i3], G(b[:, i4], b[i, i5], dxs), dxs), dxs), dxs) *
        #   J00000(i1, i2, i3, i4, i5, q[7], dt, ksi)
        #   for i5 in range(m)
        #   for i4 in range(m)
        #   for i3 in range(m)
        #   for i2 in range(m)
        #   for i1 in range(m)],
        return S.one


class _Routine10(_Routine):
    def __init__(self, i, b, q, dt, ksi):
        super().__init__(i, b, q, dt, ksi)

    def __call__(self, range_of_indices):
        # *[G(b[:, i1], G(b[:, i2], Lj(a, aj[i, 0], dxs), dxs), dxs) *
        #   (J02(i1, i2, q[6], dt, ksi) / 2 + dt * J01(i1, i2, q[2], dt, ksi) +
        #    dt ** 2 / 2 * J00(i1, i2, q[2], dt, ksi)) +
        #   Lj(a, Lj(a, G(b[:, i1], b[i, i2], dxs), dxs), dxs) / 2 *
        #   J20(i1, i2, q[10], dt, ksi) +
        #   G(b[:, i1], Lj(a, G(b[:, i2], aj[i, 0], dxs), dxs), dxs) *
        #   (J11(i1, i2, q[9], dt, ksi) - J02(i1, i2, q[8], dt, ksi) +
        #    dt * (J10(i1, i2, q[2], dt, ksi) - J01(i1, i2, q[2], dt, ksi))) +
        #   Lj(a, G(b[:, i1], Lj(a, b[i, i2], dxs), dxs), dxs) *
        #   (J11(i1, i2, q[9], dt, ksi) - J20(i1, i2, q[10], dt, ksi)) +
        #   G(b[:, i1], Lj(a, Lj(a, b[i, i2], dxs), dxs), dxs) *
        #   (J02(i1, i2, q[8], dt, ksi) / 2 + J20(i1, i2, q[10], dt, ksi) / 2 - J11(i1, i2, q[9], dt, ksi)) -
        #   Lj(a, G(b[:, i1], G(b[:, i2], aj[i, 0], dxs), dxs), dxs) *
        #   (dt * J10(i1, i2, q[2], dt, ksi) + J11(i1, i2, q[9], dt, ksi))
        #   for i2 in range(m)
        #   for i1 in range(m)],
        return S.one


class _Routine11(_Routine):
    def __init__(self, i, b, q, dt, ksi):
        super().__init__(i, b, q, dt, ksi)

    def __call__(self, range_of_indices):
        # *[G(b[:, i1], G(b[:, i2], G(b[:, i3], G(b[:, i4], aj[i, 0], dxs), dxs), dxs), dxs) *
        #   (dt * J0000(i1, i2, i3, i4, q[3], dt, ksi) + J0001(i1, i2, i3, i4, q[11], dt, ksi)) +
        #   G(b[:, i1], G(b[:, i2], Lj(a, G(b[:, i3], b[i, i4], dxs), dxs), dxs), dxs) *
        #   (J0100(i1, i2, i3, i4, q[13], dt, ksi) - J0010(i1, i2, i3, i4, q[12], dt, ksi)) -
        #   Lj(a, G(b[:, i1], G(b[:, i2], G(b[:, i3], b[i, i4], dxs), dxs), dxs), dxs) *
        #   J1000(i1, i2, i3, i4, q[14], dt, ksi) +
        #   G(b[:, i1], Lj(a, G(b[:, i2], G(b[:, i3], b[i, i4], dxs), dxs), dxs), dxs) *
        #   (J1000(i1, i2, i3, i4, q[14], dt, ksi) - J0100(i1, i2, i3, i4, q[13], dt, ksi)) +
        #   G(b[:, i1], G(b[:, i2], G(b[:, i3], Lj(a, b[i, i4], dxs), dxs), dxs), dxs) *
        #   (J0010(i1, i2, i3, i4, q[12], dt, ksi) - J0001(i1, i2, i3, i4, q[11], dt, ksi))
        #   for i4 in range(m)
        #   for i3 in range(m)
        #   for i2 in range(m)
        #   for i1 in range(m)],
        return S.one


class _Routine12(_Routine):
    def __init__(self, i, b, q, dt, ksi):
        super().__init__(i, b, q, dt, ksi)

    def __call__(self, range_of_indices):
        # *[G(b[:, i1], G(b[:, i2], G(b[:, i3], G(b[:, i4], G(b[:, i5], b[i, i6], dxs), dxs), dxs), dxs), dxs) *
        #   J000000(i1, i2, i3, i4, i5, i6, q[15], dt, ksi)
        #   for i6 in range(m)
        #   for i5 in range(m)
        #   for i4 in range(m)
        #   for i3 in range(m)
        #   for i2 in range(m)
        #   for i1 in range(m)]
        return S.one


def ranges(limit, size):
    chunks = []
    counter = 0
    chunk = (0, 0), (0, 0), (0, 0)

    for i1 in range(limit):
        for i2 in range(limit):
            for i3 in range(limit):
                counter += 1
                if counter > size:
                    counter = 0
                    chunk = (chunk[0][1], i1), (chunk[1][1], i2), (chunk[2][1], i3)
                    chunks.append(chunk)
                    continue

    return chunks


class StrongTaylorStratonovich3p0MP(Function):
    """
    Strong Taylor 3.0 method
    """
    nargs = 8

    def __new__(cls, *args, **kwargs):
        """
        Creates new StrongTaylorStratonovich3p0 object with given args
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

        print(ranges(1200, 10))

        exit()

        ranges1 = []
        ranges2 = []
        ranges3 = []
        ranges4 = []
        ranges5 = []
        ranges6 = []
        ranges7 = []
        ranges8 = []
        ranges9 = []
        ranges10 = []
        ranges11 = []
        ranges12 = []

        with Pool(cpu_count()) as pool:
            chunks = [
                yp[i, 0], aj[i, 0] * dt,
                *pool.map(_Routine1(i, b, dt, ksi), ranges1),
                *pool.map(_Routine2(i, b, q[0], dt, ksi, dxs), ranges2),
                # *pool.map(_Routine3(i, a, b, dt, ksi), ranges3),
                # *pool.map(_Routine4(i, a, b, dt, ksi), ranges4),
                # dt ** 2 / 2 * Lj(a, aj[i, 0], dxs),
                # *pool.map(_Routine5(i, a, b, dt, ksi), ranges5),
                # *pool.map(_Routine6(i, a, b, dt, ksi), ranges6),
                # *pool.map(_Routine7(i, a, b, dt, ksi), ranges7),
                # *pool.map(_Routine8(i, a, b, dt, ksi), ranges8),
                # *pool.map(_Routine9(i, a, b, dt, ksi), ranges9),
                # dt ** 3 / 6 * Lj(a, Lj(a, aj[i, 0], dxs), dxs),
                # *pool.map(_Routine10(i, a, b, dt, ksi), ranges10),
                # *pool.map(_Routine11(i, a, b, dt, ksi), ranges11),
                # *pool.map(_Routine12(i, a, b, dt, ksi), ranges12),
            ]
            print("WAITING")
            pool.close()
            pool.join()

        return chunks

    def doit(self, **hints):
        """
        Tries to expand or calculate function
        Returns
        =======
        sympy.Expr
        """
        return StrongTaylorStratonovich3p0MP(*self.args, **hints)
