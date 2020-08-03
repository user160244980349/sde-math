import unittest

from sympy import S, Function, Matrix, MatrixSymbol, Symbol, symbols, pprint

from mathematics.sde.nonlinear.functions.G import G
from mathematics.sde.nonlinear.functions.Grad import Grad
from mathematics.sde.nonlinear.functions.Ind import Ind
from mathematics.sde.nonlinear.functions.Io import Io
from mathematics.sde.nonlinear.functions.Ioo import Ioo
from mathematics.sde.nonlinear.functions.L import L, L2


class MyTestCase(unittest.TestCase):
    @unittest.skip('Success')
    def test_Grad(self):
        x1, x2, x3, x4, t = symbols('x1 x2 x3 x4, t')
        # a = x1 ** 2 * x2 ** 2 * t ** 3
        a = S(-5) * x1

        dx = tuple([S('x1'), S('x2')])

        print()
        res = Grad(a, dx)
        pprint(res)

        res = Grad(Function('a'), dx)
        pprint(res)

        self.assertEqual(True, True)

    @unittest.skip('Failure')
    def test_L2(self):
        x1, x2, x3, x4, t = symbols('x1 x2 x3 x4, t')
        exp = Matrix([x1 ** 2 * x2 ** 2 * t ** 3,
                      x1 ** 2 * x2 ** 2 * t ** 3,
                      x1 ** 2 * x2 ** 2 * t ** 3])

        a = [['x1**2 * x2**2 * t'],
             ['x2 * x1**2 * 5 * t**3']]

        b = [['sin(x1)', 'cos(x2)', 'cos(2 * x1)'],
             ['x2**2', 't * x1**2', 't * x2**3']]

        L2.context(Matrix(a), Matrix(b))

        print()
        res = L2(exp)
        pprint(res)

        self.assertEqual(True, True)

    @unittest.skip('Failure')
    def test_L(self):
        x1, x2, x3, x4, t = symbols('x1 x2 x3 x4, t')
        exp = x1 ** 2 * x2 ** 2 * t ** 3

        a = [['x1**2 * x2**2 * t'],
             ['x2 * x1**2 * 5 * t**3']]

        b = [['sin(x1)', 'cos(x2)', 'cos(2 * x1)'],
             ['x2**2', 't * x1**2', 't * x2**3']]

        L.context(Matrix(a), Matrix(b))
        res = L(exp)

        print()
        pprint(res)

        self.assertEqual(True, True)

    # @unittest.skip('Success')
    def test_G(self):
        x1, x2, x3, x4, t = symbols('x1 x2 x3 x4, t')

        exp = x1 ** 2 + 5 * x2 ** 2
        sym_exp = Symbol('z')

        b = Matrix([['sin(x1)', 'cos(x1)'],
                    ['sin(x2)', 'cos(x2)']])

        diff_args = tuple([S('x1'), S('x2')])

        print()
        pprint(G(b[:, 0], exp, diff_args))

        sym_b = MatrixSymbol('b', 2, 2)
        pprint(G(sym_b[:, 0], sym_exp, diff_args))

        self.assertEqual(True, True)

    @unittest.skip('Success')
    def test_Ind(self):
        i1, i2 = symbols('i1 i2')

        print()
        exp = Ind(i1, i2)
        pprint(exp)

        print()
        exp = Ind(1, 2)
        pprint(exp)

        self.assertEqual(True, True)

    @unittest.skip('Success')
    def test_Io(self):
        i = symbols('i')
        ksi = MatrixSymbol('ksi', 100, 100)
        dt = Symbol('dt')

        print()
        exp = Io(i, dt, ksi)
        pprint(exp)

        print()
        exp = Io(1, dt, ksi)
        pprint(exp)

        self.assertEqual(True, True)

    @unittest.skip('Success')
    def test_Ioo(self):
        i1, i2, q = symbols('i1 i2 q')
        ksi = MatrixSymbol('ksi', 100, 100)
        dt = Symbol('dt')

        print()
        exp = Ioo(i1, i2, q, dt, ksi)
        pprint(exp)

        print()
        exp = Ioo(1, 2, 10, dt, ksi)
        pprint(exp)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
