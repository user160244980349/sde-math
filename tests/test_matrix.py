import unittest

import numpy as np

from mathematics.sde.linear.matrix import vec_to_eye


class TestMatrix(unittest.TestCase):
    def test_vec_to_eye(self):
        vec = np.array([1, 2, 3])
        mx = vec_to_eye(vec)
        e_mx = np.array([
            [1, 0, 0],
            [0, 2, 0],
            [0, 0, 3]
        ])

        self.assertEqual(np.testing.assert_array_equal(mx, e_mx), None)


if __name__ == "__main__":
    unittest.main()
