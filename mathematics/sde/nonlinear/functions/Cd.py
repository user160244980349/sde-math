from sympy import Rational, Function

import tools.database as db
from mathematics.sde.nonlinear.c import getc


class Cd(Function):
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
        j1, j2, j3 = args
        obj.j1, obj.j2, obj.j3 = j1, j2, j3
        return obj

    @property
    def argv(self):
        return self.args

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
        args = self.argv
        cond = True
        for arg in args:
            cond *= arg.is_Number

        if cond:
            index = ':'.join([str(i) for i in args])
            respond = db.execute("SELECT `value` FROM `C`"
                                 "WHERE REGEXP(`index`, '^%s$')" % index)
            # print("GETTING C_%s" % index)

            if len(respond) == 0:
                new_c = getc(args)
                print("ADD NEW C_%s = %s" % (index, new_c))
                db.execute("INSERT INTO `C` (`index`, `value`) VALUES {}"
                           .format("('%s', '%s')" % (index, new_c)))
                return Rational(new_c)
            else:
                return Rational(respond[0][0])
        else:
            return Cd(*args)
