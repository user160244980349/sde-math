import numpy as np


class BoundExceedError(Exception):
    pass


def input_matrix(n, m, s):
    """
    Input of matrix
    Parameters
    ==========
    n : int
        0 dimension volume of matrix
    m : int
        1 dimension volume of matrix
    s : str
        split character
    Returns
    =======
    numpy.ndarray
    """
    mat = []

    for i in range(n):
        row = input().strip().split(s)

        if len(row) != m:
            raise BoundExceedError()

        mat.append(row)

    return np.array(mat)


def input_vector(n, s):
    """
    Input of vector
    Parameters
    ==========
    n : int
        volume of vector
    s : str
        split character
    Returns
    =======
    numpy.ndarray
    """
    row = input().strip().split(s)

    if len(row) != n:
        raise BoundExceedError()

    return np.array(row)
