import logging

from sympy import sympify, Function

import tools.database as db
from mathematics.sde.nonlinear.c import get_c


class C(Function):
    """
    Gives coefficient with requested indices and weights
    """
    _preloaded = dict()

    def __new__(cls, indices: tuple, weights: tuple, to_float=True, **kwargs):
        """
        Creates C coefficient object with needed indices and weights
        Parameters
        ==========
        indices: tuple
            requested indices
        weights: tuple
            requested weights
        Returns
        =======
        symbolic.Rational or C
            calculated value or symbolic expression
        """
        if not len(indices) == len(weights):
            return super(C, cls).__new__(cls, indices, weights, **kwargs)

        index = f"{':'.join([str(i) for i in indices])}_{':'.join([str(i) for i in weights])}"
        try:
            return cls._value(index, to_float)

        except KeyError:
            respond = cls._download_one(index)
            if len(respond) != 0:
                cls._preloaded[respond[0]] = respond[1]
                return cls._value(index, to_float)
            else:
                new_c = cls._calculate(index, indices, weights)
                cls._upload_one(new_c)
                cls._preloaded[new_c[0]] = new_c[1]
                return cls._value(index, to_float)

    @classmethod
    def _calculate(cls, index, indices, weights):
        new_c = get_c(indices, weights)
        return index, (new_c, sympify(new_c).evalf())

    @classmethod
    def _upload_one(cls, c):
        logging.info(f"C: ADDING NEW C_{c[0]} = {c[1][0]}")
        db.execute(f"INSERT INTO `C` (`index`, `value`, `value_f`) VALUES ('{c[0]}', '{c[1][0]}', {c[1][1]})")

    @classmethod
    def _unpack(cls, rows):
        return [(rows[i][0], (rows[i][1], rows[i][2])) for i in range(len(rows))]

    @classmethod
    def _value(cls, index, to_float):
        c = cls._preloaded[index]
        if to_float:
            return c[1]
        else:
            return sympify(c[0])

    @classmethod
    def _download_one(cls, index):
        logging.info(f"C: MISSING PRELOADED VERSION OF C_{index}")
        respond = db.execute(
            f"SELECT `index`, `value`, `value_f` FROM `C`"
            f"WHERE REGEXP(`index`, '^{index}$')"
        )
        return cls._unpack(respond)

    @classmethod
    def preload(cls, *args):
        """
        Updates dictionary of preloaded coefficients_legacy
        Note: weights are not accepted, such coefficients_legacy are loaded
        with all available weights
        Parameters
        ==========
        args
            Indices for coefficients_legacy to download them from database
        """
        logging.info(f"C: PRELOADING COEFFICIENTS {args}")

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

            regex = f"^{':'.join(['|'.join(pattern) for _ in range(q + 2)])}_.*$"
            query.append(
                f"SELECT `index`, `value`, `value_f` FROM `C`"
                f"WHERE REGEXP(`index`, '{regex}')"
            )

        result = db.execute("\nUNION\n".join(query))
        cls._preloaded.update(cls._unpack(result))

    def doit(self, **hints):
        """
        Tries to expand or calculate function
        Returns
        =======
        C
        """
        return C(*self.args, **hints)
