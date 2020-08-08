import unittest

import sympy as sp

from mathematics.sde.nonlinear.legendre_polynomial import polynomial


class TestLegendrePolynomial(unittest.TestCase):
    def test_polynomials(self):
        x = sp.Symbol('x')

        polynomials = [1,
                       x,
                       sp.simplify((3 * x ** 2 - 1) / 2),
                       sp.simplify((5 * x ** 3 - 3 * x) / 2),
                       sp.simplify((35 * x ** 4 - 30 * x ** 2 + 3) / 8),
                       sp.simplify((63 * x ** 5 - 70 * x ** 3 + 15 * x) / 8),
                       sp.simplify((231 * x ** 6 - 315 * x ** 4 + 105 * x ** 2 -
                                    5) / 16),
                       sp.simplify((429 * x ** 7 - 693 * x ** 5 + 315 * x ** 3 -
                                    35 * x) / 16),
                       sp.simplify((6435 * x ** 8 - 12012 * x ** 6 + 6930 * x ** 4 -
                                    1260 * x ** 2 + 35) / 128),
                       sp.simplify((12155 * x ** 9 - 25740 * x ** 7 + 18018 * x ** 5 -
                                    4620 * x ** 3 + 315 * x) / 128),
                       sp.simplify((46189 * x ** 10 - 109395 * x ** 8 + 90090 * x ** 6 -
                                    30030 * x ** 4 + 3465 * x ** 2 - 63) / 256)]

        for i in range(1, 11):
            with self.subTest(i=i):
                self.assertEqual(sp.simplify(polynomial(i)), polynomials[i])


if __name__ == '__main__':
    unittest.main()
