import sympy as sp

import mathematics.sde.nonlinear.c as c
import tools.database as db


class Cd(sp.Function):
    """
    Function to perform G operation with function
    """

    def __new__(cls, *args, **kwargs):
        """
        Creating method context with sizes of it`s components and symbols

        Parameters
        ----------
            n - a column size
            m - b matrix width
            q - independent random variables dimension size
            dxs - tuple of variables to perform differentiation

        Returns
        -------
            Calculated value or symbolic expression
        """
        obj = super(Cd, cls).__new__(cls, *args, **kwargs)
        return obj

    def doit(self):
        """
        Applies G operator on function

        Parameters
        ----------
            c - b matrix column to apply G operator
            f - function to apply operator
            dxs - arguments to apply Grad

        Returns
        -------
            Scalar result of G operator
        """
        args = self.args

        if all([isinstance(arg, sp.Number) for arg in args]):
            index = ':'.join([str(i) for i in args])
            respond = db.execute("SELECT `value` FROM `C`"
                                 "WHERE REGEXP(`index`, '^%s$')" % index)
            if len(respond) == 0:
                new_c = c.getc(args)
                print("ADD NEW C_%s = %s" % (index, new_c))
                db.execute("INSERT INTO `C` (`index`, `value`) VALUES {}"
                           .format("('%s', '%s')" % (index, new_c)))
                return sp.Rational(new_c)
            else:
                return sp.Rational(respond[0][0])
        else:
            return Cd(*args)
