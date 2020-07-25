from numpy import transpose, zeros, ndarray, sqrt
from numpy.linalg import eig

from mathematics.matrix import extending_assignment, vec_to_eye
from mathematics.sde.linear.dindet import dindet


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
    mat_vec = ndarray((1, 1))

    i2 = 0

    for i in range(n):
        n2 = n - i

        for j in range(n2):
            mat_vec = extending_assignment(mat_vec, j + i2, 0, mat_g[j][j + i])

        i2 = i2 + n - i

    return mat_vec


def algorithm_11_4(n: int, mat_dv: ndarray):
    mat_d1 = ndarray((1, 1))

    i2 = 0

    for i in range(n):
        n2 = n - i

        for j in range(n2):
            mat_d1 = extending_assignment(mat_d1, j, j + i, mat_dv[j + i2][0])
            mat_d1 = extending_assignment(mat_d1, j + i, j, mat_dv[j + i2][0])

        i2 = i2 + n - i

    return mat_d1


def algorithm_11_5(n: int, mat_a: ndarray):
    mat_one1 = zeros((n, n))
    mat_ac = ndarray((1, 1))

    r = 0

    for i in range(n):
        n2 = n - i

        for j in range(n2):
            i2 = j + i
            mat_one1[j][i2] = 1
            mat_one1[i2][j] = 1
            mat_one_a = mat_one1.dot(transpose(mat_a)) + mat_a.dot(mat_one1)
            o = 0

            for k in range(n):
                n3 = n - k

                for m in range(n3):
                    mat_ac = extending_assignment(mat_ac, m + o, r, mat_one_a[m][m + k])

                o = o + n - k

            mat_one1 = zeros((n, n))
            r = r + 1

    return mat_ac
