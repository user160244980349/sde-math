from sympy import Rational, Function

import tools.database as db
from mathematics.sde.nonlinear.c import getc


class C(Function):
    """
    Function to perform G operation with function
    """

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

            if len(respond) == 0:
                new_c = getc(args)
                print("ADD NEW C_%s = %s" % (index, new_c))
                db.execute("INSERT INTO `C` (`index`, `value`) VALUES {}"
                           .format("('%s', '%s')" % (index, new_c)))
                return Rational(new_c)
            else:
                return Rational(respond[0][0])
