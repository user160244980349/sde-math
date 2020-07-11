from numpy import shape, vstack, hstack, zeros


def extending_assignment(matrix, i, j, value):
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
