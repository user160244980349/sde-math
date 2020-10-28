from sympy import Function, sympify, Number, Add

from mathematics.sde.nonlinear.symbolic.coefficients.c0010 import C0010


class J0010(Function):
    """
    Iterated Stratonovich stochastic integral
    """
    nargs = 7

    def __new__(cls, *args, **kwargs):
        """
        Creates new J0010 object with given args
        Parameters
        ==========
        i1 : int
            integral index
        i2 : int
            integral index
        i3 : int
            integral index
        i3 : int
            integral index
        q : int
            amount of terms in approximation of integral
        dt : float
            delta time
        ksi : numpy.ndarray
            matrix of Gaussian variables
        Returns
        =======
        sympy.Expr
            formula to simplify and substitute
        """
        i1, i2, i3, i4, q, dt, ksi = sympify(args)

        if not (isinstance(i1, Number) and
                isinstance(i2, Number) and
                isinstance(i3, Number) and
                isinstance(i4, Number) and
                isinstance(q, Number)):
            return super(J0010, cls).__new__(cls, *args, **kwargs)

        return Add(*[
            C0010(j4, j3, j2, j1, dt) *
            ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] * ksi[j4, i4]
            for j4 in range(q + 1)
            for j3 in range(q + 1)
            for j2 in range(q + 1)
            for j1 in range(q + 1)])

    def doit(self, **hints):
        """
        Tries to expand or calculate function
        Returns
        =======
        J0010
        """
        return J0010(*self.args, **hints)
