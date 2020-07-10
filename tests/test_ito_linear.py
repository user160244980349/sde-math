import unittest
from numpy import array, transpose, sqrt
from numpy.testing import assert_array_almost_equal
from mathematics.ito.linear import dindet
from mathematics.ito.linear import algorithm_11_5, algorithm_11_3, algorithm_11_4, algorithm_11_2
from mathematics.matrix import vec_to_eye


class ItoLinear(unittest.TestCase):
    def test_algorithm_11_2(self):

        n, dt = 4, 0.001

        mat_a = array([[-1, 0, 0, 0],
                       [0, -2, 0, 0],
                       [0, 0, -1, 0],
                       [0, 0, 0, -3]])

        mat_f = array([[0.2, 0.1, 0.1, 0.1, 0.1],
                       [0.0, 0.2, 0.1, 0.1, 0.1],
                       [0.1, 0.1, 0.2, 0.1, 0.1],
                       [0.1, 0.1, 0.1, 0.2, 0.1]])

        vec_l2, mat_s1, mat_d1 = algorithm_11_2(n, mat_a, mat_f, dt)
        mat_l = vec_to_eye(sqrt(vec_l2))
        mat_d2 = mat_s1.dot(mat_l).dot(transpose(mat_s1.dot(mat_l)))

        self.assertIsNone(assert_array_almost_equal(mat_d1, mat_d2, 4))

    def test_algorithm_11_3(self):

        n = 4

        mat_g = array([[0.0800, 0.0500, 0.0700, 0.0700],
                       [0.0500, 0.0700, 0.0600, 0.0600],
                       [0.0700, 0.0600, 0.0800, 0.0700],
                       [0.0700, 0.0600, 0.0700, 0.0800]])

        mat_gv = algorithm_11_3(n, mat_g)

        e_mat_gv = array([[0.0800],
                          [0.0700],
                          [0.0800],
                          [0.0800],
                          [0.0500],
                          [0.0600],
                          [0.0700],
                          [0.0700],
                          [0.0600],
                          [0.0700]])

        self.assertIsNone(assert_array_almost_equal(e_mat_gv, mat_gv, 4))

    def test_algorithm_11_4(self):

        n = 4

        mat_dv = array([[0.7992],
                        [0.6986],
                        [0.7992],
                        [0.7976],
                        [0.4993],
                        [0.5991],
                        [0.6986],
                        [0.6993],
                        [0.5985],
                        [0.6986]])

        mat_d1 = algorithm_11_4(n, mat_dv)

        e_mat_d1 = array([[0.7992, 0.4993, 0.6993, 0.6986],
                          [0.4993, 0.6986, 0.5991, 0.5985],
                          [0.6993, 0.5991, 0.7992, 0.6986],
                          [0.6986, 0.5985, 0.6986, 0.7976]])

        self.assertIsNone(assert_array_almost_equal(e_mat_d1, mat_d1, 4))

    def test_algorithm_11_5(self):

        n = 4

        mat_a = array([[-1, 0, 0, 0],
                       [0, -2, 0, 0],
                       [0, 0, -1, 0],
                       [0, 0, 0, -3]])

        mat_ac = algorithm_11_5(n, mat_a)

        e_mat_ac = array([[-2., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                          [0., -4., 0., 0., 0., 0., 0., 0., 0., 0.],
                          [0., 0., -2., 0., 0., 0., 0., 0., 0., 0.],
                          [0., 0., 0., -6., 0., 0., 0., 0., 0., 0.],
                          [0., 0., 0., 0., -3., 0., 0., 0., 0., 0.],
                          [0., 0., 0., 0., 0., -3., 0., 0., 0., 0.],
                          [0., 0., 0., 0., 0., 0., -4., 0., 0., 0.],
                          [0., 0., 0., 0., 0., 0., 0., -2., 0., 0.],
                          [0., 0., 0., 0., 0., 0., 0., 0., -5., 0.],
                          [0., 0., 0., 0., 0., 0., 0., 0., 0., -4.]])

        self.assertIsNone(assert_array_almost_equal(e_mat_ac, mat_ac, 4))

    def test_dindet(self):
        n, k, dt = 4, 3, 0.001

        mat_a = array([[-1, 0, 0, 0],
                       [0, -2, 0, 0],
                       [0, 0, -1, 0],
                       [0, 0, 0, -3]])

        mat_b = array([[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1]])

        mat_ad, mat_bd = dindet(n, k, mat_a, mat_b, dt)

        e_mat_ad = array([[0.9990, 0, 0, 0],
                          [0, 0.9980, 0, 0],
                          [0, 0, 0.9990, 0],
                          [0, 0, 0, 0.9970]])

        self.assertIsNone(assert_array_almost_equal(e_mat_ad, mat_ad, 4))

        e_mat_bd = array([[0.0009995, 0.0009995, 0.0009995],
                          [0.0009990, 0.0009990, 0.0009990],
                          [0.0009995, 0.0009995, 0.0009995],
                          [0.0009985, 0.0009985, 0.0009985]])

        self.assertIsNone(assert_array_almost_equal(e_mat_bd, mat_bd, 4))


if __name__ == '__main__':
    unittest.main()
