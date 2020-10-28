from sympy import Function, sympify, Number, Add

from mathematics.sde.nonlinear.symbolic.coefficients.c02 import C02


class J02(Function):
    """
    Iterated Stratonovich stochastic integral
    """
    nargs = 5

    def __new__(cls, *args, **kwargs):
        """
        Creates new J02 object with given args

        Parameters
        −−−−−−−−−−
        i1 : int
            integral index
        i2 : int
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
        i1, i2, q, dt, ksi = sympify(args)

        if not (isinstance(i1, Number) and
                isinstance(i2, Number)):
            return super(J02, cls).__new__(cls, *args, **kwargs)

        return Add(*[
            C02(j2, j1, dt) *
            ksi[j1, i1] * ksi[j2, i2]
            for j2 in range(q + 1)
            for j1 in range(q + 1)])

    def doit(self, **hints):
        """
        Tries to expand or calculate function

        Returns
        -------
        I20
        """
        return J02(*self.args, **hints)
