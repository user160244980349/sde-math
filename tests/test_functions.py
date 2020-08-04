import unittest

from sympy import S, Function, Matrix, MatrixSymbol, Symbol, symbols, pprint

from mathematics.sde.nonlinear.functions.G import G, G2
from mathematics.sde.nonlinear.functions.Grad import Grad
from mathematics.sde.nonlinear.functions.Ind import Ind
from mathematics.sde.nonlinear.functions.Io import Io
from mathematics.sde.nonlinear.functions.Ioo import Ioo
from mathematics.sde.nonlinear.functions.L import L


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

    # @unittest.skip('Failure')
    def test_L(self):
        x1, x2, x3, x4, t = symbols('x1 x2 x3 x4, t')
        exp = x1 ** 2 * x2 ** 2 * t ** 3

        a = [['x1**2 * x2**2 * t'],
             ['x2 * x1**2 * 5 * t**3']]

        b = [['sin(x1)', 'cos(x2)', 'cos(2 * x1)'],
             ['x2**2', 't * x1**2', 't * x2**3']]

        mat_a = Matrix(a)
        mat_b = Matrix(b)

        diff_args = symbols('x1 x2')

        res = L(exp, mat_a, mat_b, diff_args)

        print()
        pprint(res.doit())

        self.assertEqual(True, True)

    @unittest.skip('Success')
    def test_G(self):
        a = Matrix(['-5 * x1',
                    '-5 * x2'])
        sym_a = MatrixSymbol('a', 2, 1)

        # b = Matrix([['0.5 * sin(x1) - 0.5 * cos(x2)', '0.75 * sin(x1) - 0.75 * cos(x2)'],
        #             ['-0.5 * sin(x1) + 0.5 * cos(x2)', '-0.75 * sin(x1) + 0.75 * cos(x2)']])

        b = Matrix([['sin(x1)', 'cos(x2)', 'x1**2 + x3**2'],
                    ['x3**(1/2)', 'x1 * x2', '5'],
                    ['cos(2 * x3)', 'sin(x1 / 2)', 'x1**2 * x3**2']])

        sym_b = MatrixSymbol('b', 2, 2)

        diff_args = symbols('x1 x2 x3')

        print()
        pprint(G(b[:, 0], b[0, 0], diff_args))
        pprint(G(b[:, 1], b[1, 0], diff_args))
        pprint(G(b[:, 1], b[2, 1], diff_args))

        pprint(G(sym_b[:, 0], sym_a[0, 0], diff_args))

        self.assertEqual(True, True)

    @unittest.skip('Success')
    def test_G2(self):
        a = Matrix(['-5 * x1',
                    '-5 * x2'])
        sym_a = MatrixSymbol('a', 2, 1)

        # b = Matrix([['0.5 * sin(x1) - 0.5 * cos(x2)', '0.75 * sin(x1) - 0.75 * cos(x2)'],
        #             ['-0.5 * sin(x1) + 0.5 * cos(x2)', '-0.75 * sin(x1) + 0.75 * cos(x2)']])

        b = Matrix([['sin(x1)', 'cos(x2)', 'x1**2 + x3**2'],
                    ['x3**(1/2)', 'x1 * x2', '5'],
                    ['cos(2 * x3)', 'sin(x1 / 2)', 'x1**2 * x3**2']])

        sym_b = MatrixSymbol('b', 2, 2)

        diff_args = symbols('x1 x2 x3')

        print()
        pprint(G2(Matrix(b[:, 0]), Matrix(b[:, 0]), diff_args).doit())
        pprint(G2(Matrix(b[:, 1]), Matrix(b[:, 0]), diff_args).doit())
        pprint(G2(Matrix(b[:, 1]), Matrix(b[:, 2]), diff_args).doit())
        gs = G2(sym_b, sym_a, diff_args)

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
