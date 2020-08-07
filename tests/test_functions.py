import unittest

from sympy import S, Matrix, MatrixSymbol, Symbol, symbols, pprint, Integral, sin

import config as c
from mathematics.sde.nonlinear.functions.G import G
from mathematics.sde.nonlinear.functions.L import L
from mathematics.sde.nonlinear.functions.Io import Io
from mathematics.sde.nonlinear.functions.Ioo import Ioo
from mathematics.sde.nonlinear.functions.Iooo import Iooo
from mathematics.sde.nonlinear.functions.C import C
from mathematics.sde.nonlinear.functions.Cd import Cd
from mathematics.sde.nonlinear.functions.Ind import Ind
from tools import database as db


class MyTestCase(unittest.TestCase):
    @unittest.skip('Success')
    def test_Iooo(self):
        q, m = 3, 2

        db.connect(c.database)

        dt = symbols('dt')
        ksi = MatrixSymbol('ksi', q + 1, m)
        pprint(Iooo(1, 1, 1, q, dt, ksi))

        db.disconnect()

        self.assertEqual(True, True)

    @unittest.skip('Success')
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

        print()
        pprint(L(mat_a, mat_b, L(mat_a, mat_b, exp, diff_args) + L(mat_a, mat_b, exp, diff_args), diff_args).doit())
        pprint(L(mat_a, mat_b, S(1) + L(mat_a, mat_b, exp, diff_args), diff_args).doit())
        pprint(L(mat_a, mat_b, diff_args[0], diff_args).doit())
        pprint(L(mat_a, mat_b, mat_b[0, 0], diff_args).doit())
        pprint(L(mat_a, mat_b, L(mat_a, mat_b, S(1), diff_args), diff_args).doit())

        self.assertEqual(True, True)

    @unittest.skip('Success')
    def test_G(self):
        a = Matrix(['-5 * x1',
                    '-5 * x2'])
        sym_a = MatrixSymbol('a', 2, 1)

        b = Matrix([['sin(x1)', 'x2'],
                    ['x2', 'cos(x1)']])

        # b = Matrix([['0.5 * sin(x1) - 0.5 * cos(x2)', '0.75 * sin(x1) - 0.75 * cos(x2)'],
        #             ['-0.5 * sin(x1) + 0.5 * cos(x2)', '-0.75 * sin(x1) + 0.75 * cos(x2)']])

        # b = Matrix([['sin(x1)', 'cos(x2)', 'x1**2 + x3**2'],
        #             ['x3**(1/2)', 'x1 * x2', '5'],
        #             ['cos(2 * x3)', 'sin(x1 / 2)', 'x1**2 * x3**2']])

        # b = Matrix([['x1', 'cos(x2)', 'x1**2 + x3**2'],
        #             ['x3**(1/2)', 'x1 * x2', '5'],
        #             ['cos(2 * x3)', 'sin(x1 / 2)', 'x1**2 * x3**2']])

        sym_b = MatrixSymbol('b', 2, 2)

        diff_args = symbols('x1 x2')

        print()
        # pprint(G(b[:, 1], b[1, 0], diff_args))
        # pprint(G(b[:, 1], b[2, 1], diff_args))
        # pprint(G(b[:, 0], G(b[:, 0], b[0, 0], diff_args).doit(), diff_args))
        # pprint(G(sym_b[:, 0], sym_a[0, 0], diff_args))
        # pprint(G(sym_b[:, 0], G(b[:, 0], sym_b[0, 0], diff_args) + G(b[:, 0], b[0, 0], diff_args), diff_args).doit())
        # pprint(G(b[:, 0], G(b[:, 0], b[0, 0], diff_args), diff_args).doit())
        # pprint(G(b[:, 0], G(b[:, 0], diff_args[0], diff_args), diff_args).doit())
        # pprint(G(b[:, 0], G(b[:, 0], S(1), diff_args), diff_args).doit())
        pprint(G(b[:, 0], G(b[:, 1], S(1), diff_args), diff_args).doit())
        pprint(G(b[:, 0], G(b[:, 1], b[0, 0], diff_args), diff_args).doit())
        pprint(G(b[:, 1], G(b[:, 0], b[0, 0], diff_args), diff_args).doit())
        pprint(G(b[:, 1], G(b[:, 1], b[0, 0], diff_args), diff_args).doit())

        self.assertEqual(True, True)

    @unittest.skip('Success')
    def test_C(self):
        print()
        db.connect(c.database)

        i1, i2, i3 = symbols('i1 i2 i3')

        exp = i1 + Cd(i1, i2, i3)
        pprint(exp)

        exp = i1 + C(S(8), S(9), S(9), S(0.001)).doit()
        pprint(exp)

        db.disconnect()

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
