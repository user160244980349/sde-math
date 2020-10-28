import unittest

import numpy as np
from sympy import Symbol, pprint, diff, sympify

from tools.input import input_matrix


@unittest.skip("Input is necessary")
class TestInput(unittest.TestCase):
    def test_formula_matrix(self):
        print()
        mat = input_matrix(2, 2, ";")

        x = Symbol("x")
        print()
        pprint(diff(mat, x))

    def test_input_formula(self):
        print("\nf(x, y) = x**2 + 2*x + y**2 + y + 2")
        f = sympify(input())
        print("f(x, y) = ")
        pprint(f)

        x, y = Symbol("x"), Symbol("y")
        print("f'xy(x, y) =")
        f1 = diff(diff(f, x), y)
        pprint(f1)
        print("f'yx(x, y) =")
        f2 = diff(diff(f, y), x)
        pprint(f2)

        self.assertEqual(f, x ** 2 + 2 * x + y ** 2 + y + 2)
        self.assertEqual(f1, f2)

    def test_input_matrix(self):
        print("\nA[4, 3] =")
        mat_a1 = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]
        ])
        print(mat_a1)

        print("A[4, 3] =")
        mat_a2 = input_matrix(4, 3, " ")

        self.assertEqual(np.testing.assert_array_equal(mat_a1, mat_a2.astype(int)), None)


if __name__ == "__main__":
    unittest.main()
