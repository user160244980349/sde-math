from numpy import array

from mathematics.sde.linear.distortion import Zero, Const, Polynomial, Harmonic


class BoundExceedError(Exception):
    pass


def input_matrix(n, m, s):
    mat = []

    for i in range(n):
        row = input().strip().split(s)

        if len(row) != m:
            raise BoundExceedError()

        mat.append(row)

    return array(mat)


def input_vector(n, s):

    row = input().strip().split(s)

    if len(row) != n:
        raise BoundExceedError()

    return array(row)


def zero():
    return Zero()


def const():
    return Const(float(input('const distortion = ?\n')))


def polynomial():
    print('U = U(1) + U(2) * t + ... + U(p+1) * t^p - k x 1\n')
    p = int(input('degree of distortion polynomial p = ?'))
    print('U = ? - 1 x p + 1')
    vec_u = input_vector(p + 1, ' ').astype(float)
    return Polynomial(vec_u)


def harmonic():
    print('U = D * sin(w * t + fi) - k x 1\nU = [D, w, fi]\n')
    vec_u = input_vector(3, ' ').astype(float)
    return Harmonic(vec_u)
