import sympy as sp

import tools.database as db
from mathematics.sde.nonlinear.c import get_c


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
        if all([isinstance(sp.sympify(arg), sp.Number) for arg in indices]) and \
                all([isinstance(sp.sympify(arg), sp.Number) for arg in weights]) and \
                len(indices) == len(weights):
            index = f"{':'.join([str(i) for i in indices])}_{':'.join([str(i) for i in weights])}"
            try:
                return sp.Rational(cls._preloaded[index])
            except KeyError:
                print(f"MISSING PRELOADED VERSION OF C_{index}")
                respond = db.execute(
                    f"SELECT `value` FROM `C`"
                    f"WHERE REGEXP(`index`, '^{index}$')"
                )
                if len(respond) == 0:
                    new_c = get_c(indices, weights)
                    print(f"ADDING NEW C_{index} = {new_c}")
                    db.execute(f"INSERT INTO `C` (`index`, `value`) VALUES ('{index}', '{new_c}')")
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
                pattern.append("[0-9]" * i)

            for i in range(len(numbers)):
                p = []
                for j in range(len(numbers)):
                    if j < i:
                        p.append(str(numbers[j]))
                    elif i == j:
                        p.append(f"[0-{numbers[j] - 1}]")
                    elif j > i:
                        p.append("[0-9]")
                pattern.append("".join(p))

            regex = f"^{':'.join(['|'.join(pattern) for _ in range(q + 3)])}_.*$"
            query.append(
                f"SELECT `index`, `value` FROM `C`"
                f"WHERE REGEXP(`index`, '{regex}')"
            )

        cls._preloaded.update(db.execute("\nUNION\n".join(query)))

    def doit(self, **hints):
        """
        Tries to expand or calculate function
        
        Returns
        -------
        C
        """
        return C(*self.args, **hints)
