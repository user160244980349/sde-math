from numpy import ndarray, shape, vstack, hstack, zeros


class BoundExceedError(Exception):
    pass


def input_ndarray(n, m, s):
    mat = ndarray((n, m))

    for i in range(n):
        row = input().strip().split(s)

        if len(row) != m:
            raise BoundExceedError()
        
        for j in range(m):
            mat[i, j] = int(row[j])

    return mat


def extending_set(matrix, i, j, value):

    if shape(matrix)[0] <= i:
        matrix = vstack((matrix, zeros((i - shape(matrix)[0] + 1, shape(matrix)[1]))))

    if shape(matrix)[1] <= j:
        matrix = hstack((matrix, zeros((shape(matrix)[0], j - shape(matrix)[1] + 1))))

    matrix[i][j] = value

    return matrix


def vec_to_eye(vector):
    
    n = len(vector)
    matrix = zeros((n, n))
    
    for i in range(len(matrix)):
        matrix[i][i] = vector[i]
    
    return matrix


def print_with_precision(matrix):

    for i in range(len(matrix)):
        print(' '.join("%2.4f" % e for e in matrix[i]))

    return matrix
