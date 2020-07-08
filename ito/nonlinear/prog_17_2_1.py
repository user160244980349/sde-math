from math import sqrt
from numpy.random import normal


def prog_17_2_1():
    dt = 0.1
    eps = 0.00001
    ee = (dt ** 2) / 4
    s = 0
    i = 1

    while ee >= eps:
        s = s + 1 / (4 * i ** 2 - 1)
        ee = ((dt ** 2) / 2) * (1 / 2 - s)
        i = i + 1

    q = i
    u = [normal() for i in range(0, q + 1)]
    v = [normal() for i in range(0, q + 1)]

    s = u[0] * v[0]

    for i in range(1, q):
        s = s + d(i) * (v[i] * u[i + 1] - v[i + 1] * u[i])

    ui100 = s * dt * 0.5

    return ui100


def d(i):
    return 1 / sqrt(4 * i ** 2 - 1)
