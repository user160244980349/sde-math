from sympy import diff, zeros, S


def convert(a, n):
    one_1 = zeros(n, n)
    r = 1
    for j in range(1, n):
        nb = n - j + 1
        for k in range(1, nb):
            i = k + j - 1
            one_1[k, i] = 1
            one_1[i, k] = 1
            one_a = one_1 * diff(a, S('x')) + a * one_1
            oo1 = 0
