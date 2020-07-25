import unittest
from sympy import Matrix, symbols, pprint

from mathematics.symbolic.operators import g, l, gradient, hessian


class TestOperators(unittest.TestCase):
    @unittest.skip('Is tested manually.')
    def test_gradient(self):

        x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
        exp = x1**3 + x2**3 + x3**3 + x4**3
        
        res = gradient(exp, exp.free_symbols)

        print()
        pprint(res)

        self.assertEqual(True, True)

    @unittest.skip('Is tested manually.')
    def test_hessian(self):

        x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
        exp = x1 ** 3 + x2 ** 3 + x3 ** 3 + x4 ** 3

        res = hessian(exp, exp.free_symbols)

        print()
        pprint(res)

        self.assertEqual(True, True)

    @unittest.skip('Is tested manually.')
    def test_l(self):

        x1, x2, x3, x4, t = symbols('x1 x2 x3 x4, t')
        exp = x1**2 * x2**2 * t**3

        a = [['x1**2 * x2**2 * t'],
             ['x2 * x1**2 * 5 * t**3']]

        b = [['sin(x1)', 'cos(x2)', 'cos(2 * x1)'],
             ['x2**2', 't * x1**2', 't * x2**3']]

        mat_a = Matrix(a)
        mat_b = Matrix(b)

        res = l(exp, mat_a, mat_b)

        print()
        pprint(res)
        
        self.assertEqual(True, True)

    @unittest.skip('Is tested manually.')
    def test_g(self):

        x1, x2, x3, x4, t = symbols('x1 x2 x3 x4, t')
        exp = x1**2 * x2**2 * t**3

        b = [['sin(x1)', 'cos(x2)', 'cos(2 * x1)'],
             ['x2**2', 't * x1**2', 't * x2**3']]

        mat_b = Matrix(b)

        res = g(exp, mat_b)

        print()
        pprint(res)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
