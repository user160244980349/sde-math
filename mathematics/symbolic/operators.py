from sympy import S, Expr, Matrix, transpose, derive_by_array, trace, pprint

from mathematics.helpers import filter_args, unwrap_1x1_matrix


def l(f: Expr, mat_a: Matrix, mat_b: Matrix):
    diff_args = filter_args(f.free_symbols)
    return f.diff(S('t')) + unwrap_1x1_matrix(transpose(gradient(f, diff_args)) * mat_a) \
           + S(1) / 2 * trace(transpose(mat_b) * hessian(f, diff_args) * mat_b)


def two_dim_l(f: Matrix, mat_a: Matrix, mat_b: Matrix):
    mat_l = Matrix()
    for i in range(f.shape[0]):
        mat_l = mat_l.col_join(Matrix([[l(f[i, 0], mat_a, mat_b)]]))
    return mat_l


def g(f: Expr, mat_b: Matrix):
    diff_args = filter_args(f.free_symbols)
    return transpose(gradient(f, diff_args)) * mat_b


def two_dim_g(f: Matrix, mat_b: Matrix):
    mat_g = Matrix()
    for i in range(f.shape[0]):
        mat_g = mat_g.col_join(Matrix([[g(f[i, 0], mat_b)]]))
    return mat_g


def gradient(f: Expr, v: tuple):
    return Matrix(derive_by_array(f, v))


def hessian(f: Expr, v: tuple):
    return Matrix(derive_by_array(derive_by_array(f, v), v))
