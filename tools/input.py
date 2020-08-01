from numpy import array


class BoundExceedError(Exception):
    pass


def input_matrix(n, m, s):
    mat = []

    for i in range(n):
        row = input().strip().split(s)

        if len(row) != m:
            raise BoundExceedError()

        mat.append(row)

    return array(mat)


def input_vector(n, s):
    row = input().strip().split(s)

    if len(row) != n:
        raise BoundExceedError()

    return array(row)
