import unittest

from numpy import array
from numpy.testing import assert_array_equal

from mathematics.sde.linear.matrix import vec_to_eye


class TestMatrix(unittest.TestCase):
    def test_vec_to_eye(self):
        vec = array([1, 2, 3])
        mat = vec_to_eye(vec)
        e_mat = array([[1, 0, 0],
                       [0, 2, 0],
                       [0, 0, 3]])

        self.assertEqual(assert_array_equal(mat, e_mat), None)


if __name__ == '__main__':
    unittest.main()
