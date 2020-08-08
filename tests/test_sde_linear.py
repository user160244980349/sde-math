import unittest

import numpy as np

import mathematics.sde.linear as lin


class TestSdeLinear(unittest.TestCase):
    def test_algorithm_11_2(self):
        n, dt = 4, 0.001

        mat_a = np.array([[-1, 0, 0, 0],
                          [0, -2, 0, 0],
                          [0, 0, -1, 0],
                          [0, 0, 0, -3]])

        mat_f = np.array([[0.2, 0.1, 0.1, 0.1, 0.1],
                          [0.0, 0.2, 0.1, 0.1, 0.1],
                          [0.1, 0.1, 0.2, 0.1, 0.1],
                          [0.1, 0.1, 0.1, 0.2, 0.1]])

        vec_l2, mat_s1, mat_d1 = lin.algorithm_11_2(n, mat_a, mat_f, dt)
        mat_l = lin.vec_to_eye(np.sqrt(vec_l2))
        mat_d2 = mat_s1.dot(mat_l).dot(np.transpose(mat_s1.dot(mat_l)))

        self.assertIsNone(np.testing.assert_array_almost_equal(mat_d1, mat_d2, 4))

    def test_algorithm_11_3(self):
        n = 4

        mat_g = np.array([[0.0800, 0.0500, 0.0700, 0.0700],
                          [0.0500, 0.0700, 0.0600, 0.0600],
                          [0.0700, 0.0600, 0.0800, 0.0700],
                          [0.0700, 0.0600, 0.0700, 0.0800]])

        mat_gv = lin.algorithm_11_3(n, mat_g)

        e_mat_gv = np.array([[0.0800],
                             [0.0700],
                             [0.0800],
                             [0.0800],
                             [0.0500],
                             [0.0600],
                             [0.0700],
                             [0.0700],
                             [0.0600],
                             [0.0700]])

        self.assertIsNone(np.testing.assert_array_almost_equal(e_mat_gv, mat_gv, 4))

    def test_algorithm_11_4(self):
        n = 4

        mat_dv = np.array([[0.7992],
                           [0.6986],
                           [0.7992],
                           [0.7976],
                           [0.4993],
                           [0.5991],
                           [0.6986],
                           [0.6993],
                           [0.5985],
                           [0.6986]])

        mat_d1 = lin.algorithm_11_4(n, mat_dv)

        e_mat_d1 = np.array([[0.7992, 0.4993, 0.6993, 0.6986],
                             [0.4993, 0.6986, 0.5991, 0.5985],
                             [0.6993, 0.5991, 0.7992, 0.6986],
                             [0.6986, 0.5985, 0.6986, 0.7976]])

        self.assertIsNone(np.testing.assert_array_almost_equal(e_mat_d1, mat_d1, 4))

    def test_algorithm_11_5(self):
        n = 4

        mat_a = np.array([[-1, 0, 0, 0],
                          [0, -2, 0, 0],
                          [0, 0, -1, 0],
                          [0, 0, 0, -3]])

        mat_ac = lin.algorithm_11_5(n, mat_a)

        e_mat_ac = np.array([[-2., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                             [0., -4., 0., 0., 0., 0., 0., 0., 0., 0.],
                             [0., 0., -2., 0., 0., 0., 0., 0., 0., 0.],
                             [0., 0., 0., -6., 0., 0., 0., 0., 0., 0.],
                             [0., 0., 0., 0., -3., 0., 0., 0., 0., 0.],
                             [0., 0., 0., 0., 0., -3., 0., 0., 0., 0.],
                             [0., 0., 0., 0., 0., 0., -4., 0., 0., 0.],
                             [0., 0., 0., 0., 0., 0., 0., -2., 0., 0.],
                             [0., 0., 0., 0., 0., 0., 0., 0., -5., 0.],
                             [0., 0., 0., 0., 0., 0., 0., 0., 0., -4.]])

        self.assertIsNone(np.testing.assert_array_almost_equal(e_mat_ac, mat_ac, 4))

    def test_dindet(self):
        n, k, dt = 4, 3, 0.001

        mat_a = np.array([[-1, 0, 0, 0],
                          [0, -2, 0, 0],
                          [0, 0, -1, 0],
                          [0, 0, 0, -3]])

        mat_b = np.array([[1, 1, 1],
                          [1, 1, 1],
                          [1, 1, 1],
                          [1, 1, 1]])

        mat_ad, mat_bd = lin.dindet(n, k, mat_a, mat_b, dt)

        e_mat_ad = np.array([[0.9990, 0, 0, 0],
                             [0, 0.9980, 0, 0],
                             [0, 0, 0.9990, 0],
                             [0, 0, 0, 0.9970]])

        self.assertIsNone(np.testing.assert_array_almost_equal(e_mat_ad, mat_ad, 4))

        e_mat_bd = np.array([[0.0009995, 0.0009995, 0.0009995],
                             [0.0009990, 0.0009990, 0.0009990],
                             [0.0009995, 0.0009995, 0.0009995],
                             [0.0009985, 0.0009985, 0.0009985]])

        self.assertIsNone(np.testing.assert_array_almost_equal(e_mat_bd, mat_bd, 4))


if __name__ == '__main__':
    unittest.main()
