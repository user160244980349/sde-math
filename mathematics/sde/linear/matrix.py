import numpy as np


class NotASquareMatrix(Exception):
    pass


def vec_to_eye(vector):
    """
    Converts vector to eye matrix
    
    Parameters
    ----------
    vector : iterable

    Returns
    -------
    numpy.ndarray
    """
    n = len(vector)
    matrix = np.zeros((n, n))

    for i in range(len(matrix)):
        matrix[i][i] = vector[i]

    return matrix


def diagonal_to_column(matrix):
    """
    Converts diagonal  matrix to column vector
    
    Parameters
    ----------
    matrix : numpy.ndarray
    Returns
    -------
    column : numpy.ndarray
    """
    height = np.shape(matrix)[0]
    if height != np.shape(matrix)[1]:
        raise NotASquareMatrix()

    column = np.zeros((height, 1))
    for i in range(height):
        column[i][0] = matrix[i][i]

    return column
