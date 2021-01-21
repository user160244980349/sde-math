import numpy as np
from numpy import transpose

from mathematics.sde.linear.matrix import diagonal_to_column


class Integral:
    """
    Provides numerical integration
    """

    def __init__(self, n: int):
        self.n, self.t0, self.tk, self.dt, self.t = \
            n, 0, 0, 0, 0
        self.m_a, self.m_ad, self.m_bd, self.m_h, self.m_fd, self.distortion = \
            None, None, None, None, None, None
        self.m_x0, self.m_mx0, self.m_dx0, self.m_xt, self.m_mx, self.m_dx = \
            None, None, None, np.ndarray((n, 0)), np.ndarray((n, 0)), np.ndarray((n, 0))
        self.v_yt, self.v_my, self.v_dy, self.v_t = \
            [], [], [], []
        self.v_ry = []

    def integrate(self):
        """
        Performs numerical integration
        """
        higher_limit = self.t + int((self.tk - self.t0) / self.dt + 1)
        lower_limit = self.t

        self.m_xt = np.hstack((self.m_xt, np.ndarray((self.n, higher_limit - lower_limit))))
        self.m_mx = np.hstack((self.m_mx, np.ndarray((self.n, higher_limit - lower_limit))))
        self.m_dx = np.hstack((self.m_dx, np.ndarray((self.n, higher_limit - lower_limit))))

        for self.t in range(lower_limit, higher_limit):
            t = self.t0 + self.t * self.dt
            ft = np.random.randn(self.n, 1)
            mat_ut = self.distortion.t(t)

            # solution of sde
            xt = self.m_ad.dot(self.m_x0) + self.m_bd.dot(mat_ut) + self.m_fd.dot(ft)
            # exit process of stochastic system
            self.m_xt[:, self.t] = xt[:, 0]
            self.v_yt.append(self.m_h.dot(xt)[0][0])

            # expectation of solution of sde
            mx = self.m_ad.dot(self.m_mx0) + self.m_bd.dot(mat_ut)
            # expectation of exit process
            self.m_mx[:, self.t] = mx[:, 0]
            self.v_my.append(self.m_h.dot(mx)[0][0])

            # dispersion of solution of sde
            dx = self.m_ad.dot(self.m_dx0).dot(np.transpose(self.m_ad)) + self.m_fd.dot(np.transpose(self.m_fd))
            # dispersion of exit process
            self.m_dx[:, self.t] = diagonal_to_column(dx)[:, 0]
            self.v_dy.append(self.m_h.dot(dx).dot(transpose(self.m_h))[0][0])

            # covariance matrix of solution of sde
            # rx = expm(self.m_a * (self.tk - t)).dot(dx)
            # covariance matrix of exit process
            # self.v_ry.append(self.m_h.dot(rx).dot(transpose(self.m_h))[0][0])

            # time flow
            self.v_t.append(t)

            self.m_x0, self.m_mx0, self.m_dx0 = xt, mx, dx
