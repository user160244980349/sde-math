import math as m

import numpy as np


class Zero:
    """
    Provides zero distortion
    """
    _ut = 0

    def t(self, t: float):
        """
        Provides zero distortion at moment t

        Parameters
        ----------
        t : float
            moment of time
        Returns
        -------
        float
            value of distortion
        """
        return Zero._ut


class Const:
    """
    Provides const distortion
    """
    def __init__(self, u: float):
        self._ut = u

    def t(self, t):
        """
        Provides const distortion at moment t

        Parameters
        ----------
        t : float
            moment of time
        Returns
        -------
        float
            value of distortion
        """
        return self._ut


class Polynomial:
    """
    Provides polynomial distortion
    """
    def __init__(self, u: np.array):
        self._u = u
        self._p = len(u)

    def t(self, t):
        """
        Provides polynomial distortion at moment t

        Parameters
        ----------
        t : float
            moment of time
        Returns
        -------
        float
            value of distortion
        """
        ut = 0
        for i in range(self._p):
            ut = ut + self._u[i] * t ** i

        return ut


class Harmonic:
    """
    Provides harmonic distortion
    """
    def __init__(self, u: np.array):
        self._u = u

    def t(self, t):
        """
        Provides harmonic distortion at moment t

        Parameters
        ----------
        t : float
            moment of time
        Returns
        -------
        float
            value of distortion
        """
        return self._u[0] * m.sin(self._u[1] * t + self._u[2])


class Distortion:
    """
    Container for various distortions
    """
    def __init__(self, n: int, mat_u: np.ndarray):
        self._size = n
        self._mat_u = mat_u
        self._mat_ut = np.array([[0.0]] * n)

    def t(self, t: float):
        """
        Provides various distortions at moment t

        Parameters
        ----------
        t : float
            moment of time
        Returns
        -------
        numpy.ndarray
            column of distortions values
        """
        for i in range(self._size):
            self._mat_ut[i, 0] = self._mat_u[i, 0].inp(t)
        return self._mat_ut
