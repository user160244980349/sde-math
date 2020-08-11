import sympy as sp

from ...c import getc
import tools.database as db


class C(sp.Function):
    """
    Gives coefficient with requested indices and weights
    """
    _preloaded = dict()

    def __new__(cls, indices: tuple, weights: tuple, **kwargs):
        """
        Creates C coefficient object with needed indices and weights

        Parameters
        ----------
        indices: tuple
            requested indices
        weights: tuple
            requested weights
        Returns
        -------
        sympy.Rational or C
            calculated value or symbolic expression
        """
        if all([isinstance(sp.sympify(arg), sp.Number) for arg in indices]):
            index = "%s_%s" % (':'.join([str(i) for i in indices]),
                               ':'.join([str(i) for i in weights]))
            try:
                return sp.Rational(cls._preloaded[index])
            except KeyError:
                print("MISSING PRELOADED VERSION OF C_%s" % index)
                respond = db.execute("SELECT `value` FROM `C`"
                                     "WHERE REGEXP(`index`, '^%s$')" % index)
                if len(respond) == 0:
                    new_c = getc(indices, weights)
                    print("ADDING NEW C_%s = %s" % (index, new_c))
                    db.execute("INSERT INTO `C` (`index`, `value`) VALUES {}"
                               .format("('%s', '%s')" % (index, new_c)))
                    return sp.sympify(new_c)
                else:
                    return sp.sympify(respond[0][0])
        else:
            return super(C, cls).__new__(cls, indices, weights, **kwargs)

    @classmethod
    def preload(cls, *args):
        """
        Updates dictionary of preloaded coefficients
        Note: weights are not accepted, such coefficients are loaded
        with all available weights

        Parameters
        ----------
        args
            Indices for coefficients to download them from database
        """
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
            regex = '^%s_.*$' % ':'.join([regex for _ in range(q + 3)])
            query.append('SELECT `index`, `value` FROM `C`'
                         'WHERE REGEXP(`index`, "%s")' % regex)
            
        cls._preloaded.update(db.execute('\nUNION\n'.join(query)))

    def doit(self, **hints):
        """
        Tries to expand or calculate function
        
        Returns
        -------
        C
        """
        return C(*self.args, **hints)
