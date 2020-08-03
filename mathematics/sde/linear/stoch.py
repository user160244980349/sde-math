from numpy import transpose, zeros, ndarray, sqrt
from numpy.linalg import eig

from mathematics.sde.linear.dindet import dindet
from mathematics.sde.linear.matrix import vec_to_eye

"""
Algorithms in this module are implementation
from the book named "xxx" in chapter nnn
"""


def stoch(n: int, mat_a: ndarray, mat_f: ndarray, dt: float):
    vec_l2, mat_s, mat_d1 = algorithm_11_2(n, mat_a, mat_f, dt)
    mat_l = vec_to_eye(sqrt(vec_l2))
    return mat_s.dot(mat_l)


def algorithm_11_2(n: int, mat_a: ndarray, mat_f: ndarray, dt: float):
    mat_ac = algorithm_11_5(n, mat_a)
    mat_g = mat_f.dot(transpose(mat_f))
    mat_gv = algorithm_11_3(n, mat_g)
    mat_dd, mat_dv = dindet(int(n * (n + 1) / 2), 1, mat_ac, mat_gv, dt)
    mat_d1 = algorithm_11_4(n, mat_dv)
    eigenvalues, eigenvectors = eig(mat_d1)
    return eigenvalues, eigenvectors, mat_d1


def algorithm_11_3(n: int, mat_g: ndarray):
    # calculating dimensions sizes
    # these are complicated thoughts
    # about indices just leave as they are
    i2 = 0
    v_size = 0
    for i in range(n):
        n2 = n - i
        for j in range(n2):
            if v_size < j + i2:
                v_size = j + i2
        i2 = i2 + n - i

    mat_vec = ndarray((v_size + 1, 1))

    # actual algorithm
    i2 = 0
    for i in range(n):
        n2 = n - i
        for j in range(n2):
            mat_vec[j + i2][0] = mat_g[j][j + i]
        i2 = i2 + n - i

    return mat_vec


def algorithm_11_4(n: int, mat_dv: ndarray):
    # calculating dimensions sizes
    # these are complicated thoughts
    # about indices just leave as they are
    i2 = 0
    size = 0
    for i in range(n):
        n2 = n - i
        for j in range(n2):
            if size < j + i:
                size = j + i
        i2 = i2 + n - i

    mat_d1 = ndarray((size + 1, size + 1))

    # actual algorithm
    i2 = 0
    for i in range(n):
        n2 = n - i
        for j in range(n2):
            mat_d1[j][j + i] = mat_dv[j + i2][0]
            mat_d1[j + i][j] = mat_dv[j + i2][0]
        i2 = i2 + n - i

    return mat_d1


def algorithm_11_5(n: int, mat_a: ndarray):
    # calculating dimensions sizes
    # these are complicated thoughts
    # about indices just leave as they are
    r = 0
    v_size = 0
    h_size = 0

    for i in range(n):
        n2 = n - i
        for j in range(n2):
            o = 0
            for k in range(n):
                n3 = n - k
                for m in range(n3):
                    if v_size < m + o:
                        v_size = m + o
                    if h_size < r:
                        h_size = r
                o = o + n - k
            r = r + 1

    mat_ones = zeros((n, n))
    mat_ac = ndarray((v_size + 1, h_size + 1))

    # actual algorithm
    r = 0
    for i in range(n):
        n2 = n - i
        for j in range(n2):
            i2 = j + i
            mat_ones[j][i2] = 1
            mat_ones[i2][j] = 1
            mat_one_a = mat_ones.dot(transpose(mat_a)) + mat_a.dot(mat_ones)
            o = 0
            for k in range(n):
                n3 = n - k
                for m in range(n3):
                    mat_ac[m + o][r] = mat_one_a[m][m + k]
                o = o + n - k
            mat_ones = zeros((n, n))
            r = r + 1

    return mat_ac
