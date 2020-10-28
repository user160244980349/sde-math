from sympy import Function, Number, sympify, Add

from mathematics.sde.nonlinear.symbolic.coefficients.c000000 import C000000


class J000000(Function):
    """
    Iterated Stratonovich stochastic integral
    """
    nargs = 9

    def __new__(cls, *args, **kwargs):
        """
        Creates new J000000 object with given args

        Parameters
        −−−−−−−−−−
        i1 : int
            integral index
        i2 : int
            integral index
        i3 : int
            integral index
        i4 : int
            integral index
        i5 : int
            integral index
        i6 : int
            integral index
        q : int
            amount of terms in approximation of integral
        dt : float
            delta time
        ksi : numpy.ndarray
            matrix of Gaussian variables
        Returns
        −−−−−−−
        sympy . Expr
            formula to simplify and substitute
        """
        i1, i2, i3, i4, i5, i6, q, dt, ksi = sympify(args)

        if not (isinstance(i1, Number) and
                isinstance(i2, Number) and
                isinstance(i3, Number) and
                isinstance(i4, Number) and
                isinstance(i5, Number) and
                isinstance(i6, Number) and
                isinstance(q, Number) and
                isinstance(dt, Number)):
            return super(J000000, cls).__new__(cls, *args, **kwargs)

        return Add(*[
            C000000(j6, j5, j4, j3, j2, j1, dt) *
            ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] *
            ksi[j4, i4] * ksi[j5, i5] * ksi[j6, i6]
            for j6 in range(q + 1)
            for j5 in range(q + 1)
            for j4 in range(q + 1)
            for j3 in range(q + 1)
            for j2 in range(q + 1)
            for j1 in range(q + 1)])

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        J000000
        """
        return J000000(*self.args, **hints)
