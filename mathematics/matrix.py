from numpy import shape, zeros


class NotASquareMatrix(Exception):
    pass


def vec_to_eye(vector):
    n = len(vector)
    matrix = zeros((n, n))

    for i in range(len(matrix)):
        matrix[i][i] = vector[i]

    return matrix


def diagonal_to_column(matrix):
    height = shape(matrix)[0]
    if height != shape(matrix)[1]:
        raise NotASquareMatrix()

    column = zeros((height, 1))
    for i in range(height):
        column[i][0] = matrix[i][i]

    return column
