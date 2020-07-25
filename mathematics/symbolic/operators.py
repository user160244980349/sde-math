from sympy import S, Expr, Matrix, transpose, derive_by_array, trace

from mathematics.helpers import filter_args, unwrap_1x1_matrix


def l(f: Expr, mat_a: Matrix, mat_b: Matrix):
    diff_args = filter_args(f.free_symbols)
    return f.diff(S('t')) + unwrap_1x1_matrix(transpose(gradient(f, diff_args)) * mat_a) \
           + S(1) / 2 * trace(transpose(mat_b) * hessian(f, diff_args) * mat_b)


def g(f: Expr, mat_b: Matrix):
    diff_args = filter_args(f.free_symbols)
    return transpose(gradient(f, diff_args)) * mat_b


def gradient(f: Expr, v: tuple):
    return Matrix(derive_by_array(f, v))


def hessian(f: Expr, v: tuple):
    return Matrix(derive_by_array(derive_by_array(f, v), v))
