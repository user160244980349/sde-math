import sympy as sp

import mathematics.sde.nonlinear.c as cs
import tools.database as db


class C(sp.Function):
    """
    Function to perform G operation with function
    """
    preloaded = dict()

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
        if all([isinstance(sp.sympify(arg), sp.Number) for arg in args]):
            index = ':'.join([str(i) for i in args])
            try:
                return sp.Rational(cls.preloaded[index])
            except KeyError:
                print("MISSING PRELOADED VERSION OF C_%s" % index)
                respond = db.execute("SELECT `value` FROM `C`"
                                     "WHERE REGEXP(`index`, '^%s$')" % index)
                if len(respond) == 0:
                    new_c = cs.getc(list(args))
                    print("ADDING NEW C_%s = %s" % (index, new_c))
                    db.execute("INSERT INTO `C` (`dimensions`, `index`, `value`) VALUES {}"
                               .format("(%d, '%s', '%s')" % (len(args), index, new_c)))
                    return sp.Rational(new_c)
                else:
                    return sp.Rational(respond[0][0])
        else:
            return super(C, cls).__new__(cls, *args, **kwargs)

    @classmethod
    def preload(cls, *args):
        i = 0
        query = ''
        while i < len(args) - 1:
            query = '%sSELECT * FROM\n' \
                    '(SELECT `index`, `value` FROM `C`\n' \
                    'WHERE `dimensions` = %d\n' \
                    'ORDER BY `index` ASC LIMIT %d)\n' \
                    'UNION\n' % (query, (i + 3), args[i] ** (i + 3))
            i += 1
        query = '%sSELECT * FROM\n' \
                '(SELECT `index`, `value` FROM `C`\n' \
                'WHERE `dimensions` = %d\n' \
                'ORDER BY `index` ASC LIMIT %d)\n' % (query, (i + 3), args[i] ** (i + 3))
        cls.preloaded.update(db.execute(query))

    def doit(self, **hints):
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
        return C(*self.args, **hints)
