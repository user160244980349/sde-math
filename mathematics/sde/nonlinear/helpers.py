from sympy import Matrix


def filter_args(symbols: tuple, deprecated: list):
    return [s for s in symbols if s not in deprecated]


def unwrap_1x1_matrix(matrix: Matrix):
    return matrix[0, 0]
