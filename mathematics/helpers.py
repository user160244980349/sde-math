from sympy import Symbol, Matrix


def filter_args(symbols: tuple):
    t = Symbol('t')
    return tuple([s for s in symbols if s != t])


def unwrap_1x1_matrix(matrix: Matrix):
    return matrix[0, 0]
