import unittest
from sympy import Matrix, symbols, pprint

from mathematics.symbolic.operators import g, l, gradient, hessian


class TestOperators(unittest.TestCase):
    def test_gradient(self):

        x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
        exp = x1**3 + x2**3 + x3**3 + x4**3
        
        res = gradient(exp, exp.free_symbols)

        print()
        pprint(res)

        self.assertEqual(True, True)

    def test_hessian(self):

        x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
        exp = x1 ** 3 + x2 ** 3 + x3 ** 3 + x4 ** 3

        res = hessian(exp, exp.free_symbols)

        print()
        pprint(res)

        self.assertEqual(True, True)

    def test_l(self):

        x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
        exp = x1 ** 3 + x2 ** 3 + x3 ** 3 + x4 ** 3

        a = [['x1'],
             ['x2'],
             ['x3'],
             ['x4']]

        b = [['x1', 'x3', 'x3'],
             ['x1', 'x3', 'x3'],
             ['x1', 'x3', 'x3'],
             ['x1', 'x3', 'x3']]

        mat_a = Matrix(a)
        mat_b = Matrix(b)

        res = l(exp, mat_a, mat_b)

        print()
        pprint(res)
        
        self.assertEqual(True, True)

    def test_g(self):

        x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
        exp = x1 ** 3 + x2 ** 3 + x3 ** 3 + x4 ** 3

        b = [['x1', 'x3', 'x3'],
             ['x1', 'x3', 'x3'],
             ['x1', 'x3', 'x3'],
             ['x1', 'x3', 'x3']]

        mat_b = Matrix(b)

        res = g(exp, mat_b)

        print()
        pprint(res)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
