from sympy import S
from numpy import ndarray


class BoundExceedError(Exception):
    pass


def input_matrix(n, m, s):
    mat = ndarray((n, m))

    for i in range(n):
        row = input().strip().split(s)

        if len(row) != m:
            raise BoundExceedError()

        for j in range(m):
            mat[i][j] = int(row[j])

    return mat


def input_formula():
    f_str = input()
    f = S(f_str)
    return f
