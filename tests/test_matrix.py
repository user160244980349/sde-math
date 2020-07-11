import unittest

from numpy import array
from numpy.testing import assert_array_equal

from mathematics.matrix import vec_to_eye, extending_assignment


class Matrix(unittest.TestCase):
    def test_vec_to_eye(self):
        vec = array([1, 2, 3])
        mat = vec_to_eye(vec)
        e_mat = array([[1, 0, 0],
                       [0, 2, 0],
                       [0, 0, 3]])

        self.assertEqual(assert_array_equal(mat, e_mat), None)

    def test_extending_assignment(self):
        mat = array([[]])
        mat = extending_assignment(mat, 0, 0, 1)
        mat = extending_assignment(mat, 0, 5, 1)
        mat = extending_assignment(mat, 5, 0, 1)
        mat = extending_assignment(mat, 5, 5, 1)

        e_mat = array([[1, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 1]])

        self.assertEqual(assert_array_equal(mat, e_mat), None)


if __name__ == '__main__':
    unittest.main()
