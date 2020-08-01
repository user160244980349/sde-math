from numpy import transpose, hstack, ndarray
from numpy.random import randn

from mathematics.sde.linear.matrix import diagonal_to_column


# from scipy.linalg import expm


class Integral:
    def __init__(self, n: int):
        self.n, self.t0, self.tk, self.dt, self.integration_step = \
            n, 0, 0, 0, 0
        self.mat_a, self.mat_ad, self.mat_bd, self.mat_h, self.mat_fd, self.distortion = \
            None, None, None, None, None, None
        self.mat_x0, self.mat_mx0, self.mat_dx0, self.mat_xt, self.mat_mx, self.mat_dx = \
            None, None, None, ndarray((n, 0)), ndarray((n, 0)), ndarray((n, 0))
        self.vec_yt, self.vec_my, self.vec_dy, self.vec_t = \
            [], [], [], []
        # self.vec_ry = []

    def integrate(self):
        higher_limit = self.integration_step + int((self.tk - self.t0) / self.dt + 1)
        lower_limit = self.integration_step

        self.mat_xt = hstack((self.mat_xt, ndarray((self.n, higher_limit - lower_limit))))
        self.mat_mx = hstack((self.mat_mx, ndarray((self.n, higher_limit - lower_limit))))
        self.mat_dx = hstack((self.mat_dx, ndarray((self.n, higher_limit - lower_limit))))

        for self.integration_step in range(lower_limit, higher_limit):
            t = self.t0 + self.integration_step * self.dt
            ft = randn(self.n, 1)
            mat_ut = self.distortion.t(t)

            # solution of sde
            xt = self.mat_ad.dot(self.mat_x0) + self.mat_bd.dot(mat_ut) + self.mat_fd.dot(ft)
            # exit process of stochastic system
            self.mat_xt[:, self.integration_step] = xt[:, 0]
            # self.vec_yt.append(self.mat_h.dot(xt)[0][0])

            # expectation of solution of sde
            mx = self.mat_ad.dot(self.mat_mx0) + self.mat_bd.dot(mat_ut)
            # expectation of exit process
            self.mat_mx[:, self.integration_step] = mx[:, 0]
            # self.vec_my.append(self.mat_h.dot(mx)[0][0])

            # dispersion of solution of sde
            dx = self.mat_ad.dot(self.mat_dx0).dot(transpose(self.mat_ad)) + self.mat_fd.dot(transpose(self.mat_fd))
            # dispersion of exit process
            self.mat_dx[:, self.integration_step] = diagonal_to_column(dx)[:, 0]
            # self.vec_dy.append(self.mat_h.dot(dx).dot(transpose(self.mat_h))[0][0])

            # covariance matrix of solution of sde
            # rx = expm(self.mat_a * (self.tk - t)).dot(dx)
            # covariance matrix of exit process
            # self.vec_ry.append(self.mat_h.dot(rx).dot(transpose(self.mat_h))[0][0])

            # time flow
            self.vec_t.append(t)

            self.mat_x0, self.mat_mx0, self.mat_dx0 = xt, mx, dx
