import unittest

import numpy as np

import mathematics.sde.linear.stoch as lin


class TestSdeLinear(unittest.TestCase):
    def test_algorithm_11_2(self):
        n, dt = 4, 0.001

        a = np.array([[-1, 0, 0, 0],
                      [0, -2, 0, 0],
                      [0, 0, -1, 0],
                      [0, 0, 0, -3]])

        f = np.array([[0.2, 0.1, 0.1, 0.1, 0.1],
                      [0.0, 0.2, 0.1, 0.1, 0.1],
                      [0.1, 0.1, 0.2, 0.1, 0.1],
                      [0.1, 0.1, 0.1, 0.2, 0.1]])

        v_l2, m_s1, m_d1 = lin.algorithm_11_2(n, a, f, dt)
        m_l = lin.vec_to_eye(np.sqrt(v_l2))
        m_d2 = m_s1.dot(m_l).dot(np.transpose(m_s1.dot(m_l)))

        self.assertIsNone(np.testing.assert_array_almost_equal(m_d1, m_d2, 4))

    def test_algorithm_11_3(self):
        n = 4

        m_g = np.array([[0.0800, 0.0500, 0.0700, 0.0700],
                        [0.0500, 0.0700, 0.0600, 0.0600],
                        [0.0700, 0.0600, 0.0800, 0.0700],
                        [0.0700, 0.0600, 0.0700, 0.0800]])

        m_gv = lin.algorithm_11_3(n, m_g)

        e_m_gv = np.array([[0.0800],
                           [0.0700],
                           [0.0800],
                           [0.0800],
                           [0.0500],
                           [0.0600],
                           [0.0700],
                           [0.0700],
                           [0.0600],
                           [0.0700]])

        self.assertIsNone(np.testing.assert_array_almost_equal(e_m_gv, m_gv, 4))

    def test_algorithm_11_4(self):
        n = 4

        m_dv = np.array([[0.7992],
                         [0.6986],
                         [0.7992],
                         [0.7976],
                         [0.4993],
                         [0.5991],
                         [0.6986],
                         [0.6993],
                         [0.5985],
                         [0.6986]])

        m_d1 = lin.algorithm_11_4(n, m_dv)

        e_m_d1 = np.array([[0.7992, 0.4993, 0.6993, 0.6986],
                           [0.4993, 0.6986, 0.5991, 0.5985],
                           [0.6993, 0.5991, 0.7992, 0.6986],
                           [0.6986, 0.5985, 0.6986, 0.7976]])

        self.assertIsNone(np.testing.assert_array_almost_equal(e_m_d1, m_d1, 4))

    def test_algorithm_11_5(self):
        n = 4

        m_a = np.array([[-1, 0, 0, 0],
                        [0, -2, 0, 0],
                        [0, 0, -1, 0],
                        [0, 0, 0, -3]])

        m_ac = lin.algorithm_11_5(n, m_a)

        e_m_ac = np.array([[-2., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                           [0., -4., 0., 0., 0., 0., 0., 0., 0., 0.],
                           [0., 0., -2., 0., 0., 0., 0., 0., 0., 0.],
                           [0., 0., 0., -6., 0., 0., 0., 0., 0., 0.],
                           [0., 0., 0., 0., -3., 0., 0., 0., 0., 0.],
                           [0., 0., 0., 0., 0., -3., 0., 0., 0., 0.],
                           [0., 0., 0., 0., 0., 0., -4., 0., 0., 0.],
                           [0., 0., 0., 0., 0., 0., 0., -2., 0., 0.],
                           [0., 0., 0., 0., 0., 0., 0., 0., -5., 0.],
                           [0., 0., 0., 0., 0., 0., 0., 0., 0., -4.]])

        self.assertIsNone(np.testing.assert_array_almost_equal(e_m_ac, m_ac, 4))

    def test_dindet(self):
        n, k, dt = 4, 3, 0.001

        m_a = np.array([[-1, 0, 0, 0],
                        [0, -2, 0, 0],
                        [0, 0, -1, 0],
                        [0, 0, 0, -3]])

        m_b = np.array([[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]])

        m_ad, m_bd = lin.dindet(n, k, m_a, m_b, dt)

        e_m_ad = np.array([[0.9990, 0, 0, 0],
                           [0, 0.9980, 0, 0],
                           [0, 0, 0.9990, 0],
                           [0, 0, 0, 0.9970]])

        self.assertIsNone(np.testing.assert_array_almost_equal(e_m_ad, m_ad, 4))

        e_m_bd = np.array([[0.0009995, 0.0009995, 0.0009995],
                           [0.0009990, 0.0009990, 0.0009990],
                           [0.0009995, 0.0009995, 0.0009995],
                           [0.0009985, 0.0009985, 0.0009985]])

        self.assertIsNone(np.testing.assert_array_almost_equal(e_m_bd, m_bd, 4))


if __name__ == '__main__':
    unittest.main()
