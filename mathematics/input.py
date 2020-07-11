from numpy import array


class BoundExceedError(Exception):
    pass


def input_matrix(n, m, s):
    mat = []

    for i in range(n):
        row = input().strip().split(s)

        if len(row) != m:
            raise BoundExceedError()

        mat.append([])
        for j in range(m):
            mat[i].append(row[j])

    return array(mat)
