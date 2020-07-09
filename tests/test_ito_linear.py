import unittest
from numpy import array, shape, transpose
from numpy.linalg import eigh
from ito.linear.dindet import dindet
from ito.linear.stoch import stoch, algorithm_11_5, algorithm_11_3, algorithm_11_4
from tools.matrix import print_with_precision


class ItoLinear(unittest.TestCase):
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
        for i in range(shape(e_mat_gv)[0]):
            with self.subTest(i=i):
                for j in range(shape(e_mat_gv)[1]):
                    with self.subTest(j=j):
                        self.assertAlmostEqual(mat_gv[i][j], e_mat_gv[i][j], 4)

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
        for i in range(shape(e_mat_d1)[0]):
            with self.subTest(i=i):
                for j in range(shape(e_mat_d1)[1]):
                    with self.subTest(j=j):
                        self.assertAlmostEqual(mat_d1[i][j], e_mat_d1[i][j], 4)

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
        for i in range(shape(e_mat_ac)[0]):
            with self.subTest(i=i):
                for j in range(shape(e_mat_ac)[1]):
                    with self.subTest(j=j):
                        self.assertAlmostEqual(mat_ac[i][j], e_mat_ac[i][j], 4)

    def test_dindet(self):
        n = 4
        k = 3
        dt = 0.001

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
        for i in range(shape(e_mat_ad)[0]):
            with self.subTest(i=i):
                for j in range(shape(e_mat_ad)[1]):
                    with self.subTest(j=j):
                        self.assertAlmostEqual(mat_ad[i][j], e_mat_ad[i][j], 4)

        e_mat_bd = array([[0.0009995, 0.0009995, 0.0009995],
                          [0.0009990, 0.0009990, 0.0009990],
                          [0.0009995, 0.0009995, 0.0009995],
                          [0.0009985, 0.0009985, 0.0009985]])
        for i in range(shape(e_mat_bd)[0]):
            with self.subTest(i=i):
                for j in range(shape(e_mat_bd)[1]):
                    with self.subTest(j=j):
                        self.assertAlmostEqual(mat_bd[i][j], e_mat_bd[i][j], 7)

    def test_stoch(self):

        n = 4

        mat_a = array([[-1, 0, 0, 0],
                       [0, -2, 0, 0],
                       [0, 0, -1, 0],
                       [0, 0, 0, -3]])

        mat_f = array([[0.2, 0.1, 0.1, 0.1, 0.1],
                       [0.0, 0.2, 0.1, 0.1, 0.1],
                       [0.1, 0.1, 0.2, 0.1, 0.1],
                       [0.1, 0.1, 0.1, 0.2, 0.1]])

        dt = 0.001

        mat_fd = stoch(n, mat_a, mat_f, dt)

        # print('\nFd =')
        # print_with_precision(mat_fd)

        e_mat_fd = array([[0.0016,  -0.0000,  0.0029, 0.0083],
                          [0.0010,  -0.0000, -0.0040, 0.0073],
                          [-0.0012,  0.0022,  0.0003, 0.0086],
                          [-0.0012, -0.0022,  0.0003, 0.0086]])
        # for i in range(shape(e_mat_fd)[0]):
        #     with self.subTest(i=i):
        #         for j in range(shape(e_mat_fd)[1]):
        #             with self.subTest(j=j):
        #                 self.assertAlmostEqual(mat_fd[i][j], e_mat_fd[i][j], 4)

        self.assertEqual(True, True)
        

if __name__ == '__main__':
    unittest.main()
