from sympy import S, transpose, derive_by_array, trace


def l(f, mat_a, mat_b):
    return f.diff(S('t')) + transpose(gradient(f, (S('x')))) * mat_a \
           + 1 / 2 * trace(transpose(mat_b) * hessian(f, (S('x'))) * mat_b)


def g(f, mat_b):
    return transpose(gradient(f, (S('x')))) * mat_b


def gradient(f, v: tuple):
    return derive_by_array(f, v)


def hessian(f, v: tuple):
    return derive_by_array(derive_by_array(f, v), v)
