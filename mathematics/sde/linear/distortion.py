from math import sin

from numpy import array


class Zero:
    _ut = 0

    def t(self, t):
        return Zero._ut


class Const:
    def __init__(self, u):
        self._ut = u

    def t(self, t):
        return self._ut


class Polynomial:
    def __init__(self, u):
        self._u = u
        self._p = len(u)

    def t(self, t):
        ut = 0
        for i in range(self._p):
            ut = ut + self._u[i] * t ** i

        return ut


class Harmonic:
    def __init__(self, u):
        self._u = u

    def t(self, t):
        return self._u[0] * sin(self._u[1] * t + self._u[2])


class Distortion:
    def __init__(self, n, mat_u):
        self._size = n
        self._mat_u = mat_u
        self._mat_ut = array([[0.0]] * n)

    def t(self, t):
        for i in range(self._size):
            self._mat_ut[i, 0] = self._mat_u[i, 0].t(t)
        return self._mat_ut
