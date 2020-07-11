import unittest

from sympy import Symbol, simplify

from mathematics.symbolic.legendre_polynomial import polynomial


class LegendrePolynomial(unittest.TestCase):
    def test_polynomials(self):

        x = Symbol('x')

        polynomials = [1,
                       x,
                       simplify((3 * x**2 - 1) / 2),
                       simplify((5 * x**3 - 3 * x) / 2),
                       simplify((35 * x**4 - 30 * x**2 + 3) / 8),
                       simplify((63 * x**5 - 70 * x**3 + 15 * x) / 8),
                       simplify((231 * x**6 - 315 * x**4 + 105 * x**2 - 5) / 16),
                       simplify((429 * x**7 - 693 * x**5 + 315 * x**3 - 35 * x) / 16),
                       simplify((6435 * x**8 - 12012 * x**6 + 6930 * x**4 - 1260 * x**2 + 35) / 128),
                       simplify((12155 * x**9 - 25740 * x**7 + 18018 * x**5 - 4620 * x**3 + 315 * x) / 128),
                       simplify((46189 * x**10 - 109395 * x**8 + 90090 * x**6 - 30030 * x**4 + 3465 * x**2 - 63) / 256)]

        for i in range(1, 11):
            with self.subTest(i=i):
                self.assertEqual(simplify(polynomial(i, x)), polynomials[i])


if __name__ == '__main__':
    unittest.main()
