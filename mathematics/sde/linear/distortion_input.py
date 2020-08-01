from tools.input import input_vector
from mathematics.sde.linear.distortion import Zero, Const, Polynomial, Harmonic


def zero():
    return Zero()


def const():
    return Const(float(input('const distortion = ?\n')))


def polynomial():
    print('U = U(1) + U(2) * t + ... + U(p+1) * t^p - k x 1\n')
    p = int(input('degree of distortion polynomial p = ?'))
    print('U = ? - 1 x p + 1\n')
    vec_u = input_vector(p + 1, ' ').astype(float)
    return Polynomial(vec_u)


def harmonic():
    print('U = D * sin(w * t + fi) - k x 1\nU = [D, w, fi]')
    vec_u = input_vector(3, ' ').astype(float)
    return Harmonic(vec_u)
