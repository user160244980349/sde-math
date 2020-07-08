from numpy import zeros


def matrix(n, m, s):
    mat = zeros((n, m))

    for i in range(n):
        row = input().strip().split(s)

        if len(row) != m:
            raise BoundExceedError()
        
        for j in range(m):
            mat[i, j] = int(row[j])

    return mat


class BoundExceedError(Exception):
    pass
