from sympy import S, Matrix, transpose, derive_by_array, trace, pprint


def l(f, mat_a, mat_b):
    return f.diff(S('t')) + (transpose(gradient(f, f.free_symbols)) * mat_a)[0, 0] \
        + S(1) / 2 * trace(transpose(mat_b) * hessian(f, f.free_symbols) * mat_b)


def g(f, mat_b):
    return transpose(gradient(f, f.free_symbols)) * mat_b


def gradient(f, v: tuple):
    return Matrix(derive_by_array(f, v))


def hessian(f, v: tuple):
    return Matrix(derive_by_array(derive_by_array(f, v), v))
