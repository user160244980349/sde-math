import unittest

from time import time

import numpy as np
import plotly.graph_objects as go
from numpy import transpose

from mathematics.sde.linear.distortions import ComplexDistortion
from mathematics.sde.linear.distortions_input import const, polynomial, harmonic, zero
from mathematics.sde.linear.integration import Integral
from mathematics.sde.linear.stoch import stoch
from tools.input import input_matrix

from mathematics.sde.linear.dindet import dindet
from mathematics.sde.linear.matrix import vec_to_eye
from mathematics.sde.linear.stoch import algorithm_11_2, algorithm_11_3, algorithm_11_5, algorithm_11_4


class TestSdeLinear(unittest.TestCase):

    def test_program(self):
        """
        Performs modeling of linear stochastic systems
        """
        print("""
        NUMERICAL SOLUTION OF LINEAR
        STATIONARY SYSTEM OF STOCHASTIC
        DIFFERENTIAL EQUATIONS

        dx = AX dt + BU dt + F df, X(0) = X0
        Y = HX

        X - size n x 1, Y - size 1 x 1, U - size k x 1
        f - size m x 1, A - size n x n, B - size n x k
        F - size n x m, H - size 1 x n    

        n, k, m >= 1
        """)

        # input sizes
        n = int(input("n = ? (n >= 1)\n"))
        while n < 1:
            n = int(input("input new n = ? (n >= 1)\n"))

        k = int(input("k = ? (k >= 1)\n"))
        while k < 1:
            k = int(input("input new k = ? (k >= 1)\n"))

        m = int(input("m = ? (m >= 1)\n"))
        while m < 1:
            m = int(input("input new m = ? (m >= 1)\n"))

        # input matrices
        print("A = ? - n x n")
        mat_a = input_matrix(n, n, " ").astype(float)

        print("B = ? - n x k")
        mat_b = input_matrix(n, k, " ").astype(float)

        print("F = ? - n x m")
        mat_f = input_matrix(n, m, " ").astype(float)

        print("H = ? - 1 x n")
        mat_h = input_matrix(1, n, " ").astype(float)

        print("x0 = ? - n x 1")
        mat_x0 = input_matrix(n, 1, " ").astype(float)
        print(transpose(mat_x0))

        # integration range
        dt = float(input("dt = ? (dt > 0)\n"))
        t0 = float(input("t0 = ?\n"))
        tk = float(input("tk = ? (tk > t0 + dt)\n"))

        while dt <= 0 or t0 > tk - dt:
            dt = float(input("input new dt = ? (dt > 0)\n"))
            t0 = float(input("input new t0 = ?\n"))
            tk = float(input("input new tk = ? (tk > t0 + dt)\n"))

        integral = Integral(4)

        integral.k, integral.m, integral.dt, integral.t0, integral.tk = \
            k, m, dt, t0, tk

        integral.m_a = mat_a

        integral.mat_b = mat_b

        integral.mat_f = mat_f

        integral.m_h = mat_h

        integral.m_x0 = mat_x0

        integral.m_mx0 = mat_x0

        integral.m_dx0 = np.zeros((integral.n, integral.n))

        print("""
        CALCULATION OF MATRICES OF DYNAMICAL 
        PART OF SOLUTION - Ad AND DETERMINISTIC 
        PART OF SOLUTION - Bd (ALGORITHM 11.2)
        """)

        integral.m_ad, integral.m_bd = dindet(integral.n, integral.k, integral.m_a, integral.mat_b, integral.dt)

        print("Ab =")
        print(integral.m_ad)
        print("Bb =")
        print(integral.m_bd)

        print("""
        CALCULATION OF MATRIX OF STOCHASTIC
        PART OF SOLUTION - Fd (ALGORITHM 11.6)	
        """)

        integral.m_fd = stoch(integral.n, integral.m_a, integral.mat_f, integral.dt)

        print("Fd = ")
        print(integral.m_fd)

        mat_u = np.array([[object]] * integral.k)
        for i in range(integral.k):
            keysym = input("\nkey = ? [c,p,h,o]\n")
            if keysym == "c":
                mat_u[i][0] = const()

            elif keysym == "p":
                mat_u[i][0] = polynomial()

            elif keysym == "h":
                mat_u[i][0] = harmonic()

            elif keysym == "o":
                mat_u[i][0] = zero()

        integral.distortion = ComplexDistortion(integral.k, mat_u)

        print("\nwhich trajectories do you want to be shown?")
        trajectories = np.array(input().strip().split(" ")).astype(int)
        print("\ncalculating...")

        while True:
            start_time = time()
            integral.integrate()
            print(f"integration took {(time() - start_time):.3f} seconds")

            # create traces
            fig1 = go.Figure()
            fig2 = go.Figure()
            for i in trajectories:
                fig1.add_trace(
                    go.Scatter(
                        x=integral.v_t, y=integral.m_xt[i],
                        mode="lines",
                        name=f"component {i}"
                    )
                )
                fig1.add_trace(
                    go.Scatter(
                        x=integral.v_t, y=integral.m_mx[i],
                        mode="lines",
                        name=f"expectation of component {i}"
                    )
                )
                fig2.add_trace(
                    go.Scatter(
                        x=integral.v_t, y=integral.m_dx[i],
                        mode="lines",
                        name=f"dispersion of component {i}"
                    )
                )
            fig1.show()
            fig2.show()

            integral.tk = integral.tk * 2

            if input("\nnext?\n") != "y":
                break

    def test_algorithm_11_2(self):
        n, dt = 4, 0.001

        a = np.array([
            [-1, 0, 0, 0],
            [0, -2, 0, 0],
            [0, 0, -1, 0],
            [0, 0, 0, -3]
        ])

        f = np.array([
            [0.2, 0.1, 0.1, 0.1, 0.1],
            [0.0, 0.2, 0.1, 0.1, 0.1],
            [0.1, 0.1, 0.2, 0.1, 0.1],
            [0.1, 0.1, 0.1, 0.2, 0.1]
        ])

        v_l2, m_s1, m_d1 = algorithm_11_2(n, a, f, dt)
        m_l = vec_to_eye(np.sqrt(v_l2))
        m_d2 = m_s1.dot(m_l).dot(np.transpose(m_s1.dot(m_l)))

        self.assertIsNone(np.testing.assert_array_almost_equal(m_d1, m_d2, 4))

    def test_algorithm_11_3(self):
        n = 4

        m_g = np.array([
            [0.0800, 0.0500, 0.0700, 0.0700],
            [0.0500, 0.0700, 0.0600, 0.0600],
            [0.0700, 0.0600, 0.0800, 0.0700],
            [0.0700, 0.0600, 0.0700, 0.0800]
        ])

        m_gv = algorithm_11_3(n, m_g)

        e_m_gv = np.array([
            [0.0800],
            [0.0700],
            [0.0800],
            [0.0800],
            [0.0500],
            [0.0600],
            [0.0700],
            [0.0700],
            [0.0600],
            [0.0700]
        ])

        self.assertIsNone(np.testing.assert_array_almost_equal(e_m_gv, m_gv, 4))

    def test_algorithm_11_4(self):
        n = 4

        m_dv = np.array([
            [0.7992],
            [0.6986],
            [0.7992],
            [0.7976],
            [0.4993],
            [0.5991],
            [0.6986],
            [0.6993],
            [0.5985],
            [0.6986]
        ])

        m_d1 = algorithm_11_4(n, m_dv)

        e_m_d1 = np.array([
            [0.7992, 0.4993, 0.6993, 0.6986],
            [0.4993, 0.6986, 0.5991, 0.5985],
            [0.6993, 0.5991, 0.7992, 0.6986],
            [0.6986, 0.5985, 0.6986, 0.7976]
        ])

        self.assertIsNone(np.testing.assert_array_almost_equal(e_m_d1, m_d1, 4))

    def test_algorithm_11_5(self):
        n = 4

        m_a = np.array([
            [-1, 0, 0, 0],
            [0, -2, 0, 0],
            [0, 0, -1, 0],
            [0, 0, 0, -3]
        ])

        m_ac = algorithm_11_5(n, m_a)

        e_m_ac = np.array([
            [-2., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., -4., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., -2., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., -6., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., -3., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., -3., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., -4., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., -2., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., -5., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 0., -4.]
        ])

        self.assertIsNone(np.testing.assert_array_almost_equal(e_m_ac, m_ac, 4))

    def test_dindet(self):
        n, k, dt = 4, 3, 0.001

        m_a = np.array([
            [-1, 0, 0, 0],
            [0, -2, 0, 0],
            [0, 0, -1, 0],
            [0, 0, 0, -3]
        ])

        m_b = np.array([
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ])

        m_ad, m_bd = dindet(n, k, m_a, m_b, dt)

        e_m_ad = np.array([
            [0.9990, 0, 0, 0],
            [0, 0.9980, 0, 0],
            [0, 0, 0.9990, 0],
            [0, 0, 0, 0.9970]
        ])

        self.assertIsNone(np.testing.assert_array_almost_equal(e_m_ad, m_ad, 4))

        e_m_bd = np.array([
            [0.0009995, 0.0009995, 0.0009995],
            [0.0009990, 0.0009990, 0.0009990],
            [0.0009995, 0.0009995, 0.0009995],
            [0.0009985, 0.0009985, 0.0009985]
        ])

        self.assertIsNone(np.testing.assert_array_almost_equal(e_m_bd, m_bd, 4))


if __name__ == "__main__":
    unittest.main()
