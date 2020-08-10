import sympy as sp

import mathematics.sde.nonlinear.c as cs
import tools.database as db


class C(sp.Function):
    """
    Function to perform G operation with function
    """
    preloaded = dict()

    def __new__(cls, indices: tuple, weights: tuple, **kwargs):
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
        if all([isinstance(sp.sympify(arg), sp.Number) for arg in indices]):
            index = "%s_%s" % (':'.join([str(i) for i in indices]),
                               ':'.join([str(i) for i in weights]))
            try:
                return sp.Rational(cls.preloaded[index])
            except KeyError:
                print("MISSING PRELOADED VERSION OF C_%s" % index)
                respond = db.execute("SELECT `value` FROM `C`"
                                     "WHERE REGEXP(`index`, '^%s$')" % index)
                if len(respond) == 0:
                    new_c = cs.getc(indices, weights)
                    print("ADDING NEW C_%s = %s" % (index, new_c))
                    db.execute("INSERT INTO `C` (`index`, `value`) VALUES {}"
                               .format("('%s', '%s')" % (index, new_c)))
                    return sp.Rational(new_c)
                else:
                    return sp.Rational(respond[0][0])
        else:
            return super(C, cls).__new__(cls, indices, weights, **kwargs)

    @classmethod
    def search_regex(cls):
        pass

    @classmethod
    def preload(cls, *args):
        query = []
        for q in range(len(args)):
            numbers = [int(char) for char in str(args[q] + 1)]
            pattern = []

            for i in range(1, len(numbers)):
                pattern.append('[0-9]' * i)

            for i in range(len(numbers)):
                p = []
                for j in range(len(numbers)):
                    if j < i:
                        p.append(str(numbers[j]))
                    elif i == j:
                        p.append('[0-%d]' % (numbers[j] - 1))
                    elif j > i:
                        p.append('[0-9]')
                pattern.append(''.join(p))

            regex = '|'.join(pattern)
            regex = '^%s_' % ':'.join([regex for _ in range(q + 2)])
            query.append('SELECT `index`, `value` FROM `C`'
                         'WHERE REGEXP(`index`, "%s")' % regex)

        cls.preloaded.update(db.execute('\nUNION\n'.join(query)))

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
