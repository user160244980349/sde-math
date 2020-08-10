import unittest

import sympy as sp

import config as c
import mathematics.sde.nonlinear.functions as f
from tools import database as db


class MyTestCase(unittest.TestCase):
    @unittest.skip('Success')
    def test_preload(self):

        db.connect(c.database)
        f.C.preload(3, 2)
        db.disconnect()

        self.assertEqual(True, True)

    @unittest.skip('Success')
    def test_Iooo(self):
        q, m = 3, 2

        db.connect(c.database)

        dt = sp.symbols('dt')
        ksi = sp.MatrixSymbol('ksi', q + 1, m)
        sp.pprint(f.Iooo(1, 1, 1, q, dt, ksi))

        db.disconnect()

        self.assertEqual(True, True)

    @unittest.skip('Success')
    def test_L(self):
        x1, x2, x3, x4, t = sp.symbols('x1 x2 x3 x4, t')
        exp = x1 ** 2 * x2 ** 2 * t ** 3

        a = [['x1**2 * x2**2 * t'],
             ['x2 * x1**2 * 5 * t**3']]

        b = [['sin(x1)', 'cos(x2)', 'cos(2 * x1)'],
             ['x2**2', 't * x1**2', 't * x2**3']]

        mat_a = sp.Matrix(a)
        mat_b = sp.Matrix(b)

        diff_args = sp.symbols('x1 x2')

        print()
        sp.pprint(f.L(mat_a, mat_b, f.L(mat_a, mat_b, exp, diff_args) +
                      f.L(mat_a, mat_b, exp, diff_args), diff_args).doit())
        sp.pprint(f.L(mat_a, mat_b, sp.S.One + f.L(mat_a, mat_b, exp, diff_args), diff_args).doit())
        sp.pprint(f.L(mat_a, mat_b, diff_args[0], diff_args).doit())
        sp.pprint(f.L(mat_a, mat_b, mat_b[0, 0], diff_args).doit())
        sp.pprint(f.L(mat_a, mat_b, f.L(mat_a, mat_b, sp.S.One, diff_args), diff_args).doit())

        self.assertEqual(True, True)

    @unittest.skip('Success')
    def test_G(self):
        a = sp.Matrix(['-5 * x1',
                       '-5 * x2'])
        sym_a = sp.MatrixSymbol('a', 2, 1)

        b = sp.Matrix([['sin(x1)', 'x2'],
                       ['x2', 'cos(x1)']])

        # b = Matrix([['0.5 * sin(x1) - 0.5 * cos(x2)', '0.75 * sin(x1) - 0.75 * cos(x2)'],
        #             ['-0.5 * sin(x1) + 0.5 * cos(x2)', '-0.75 * sin(x1) + 0.75 * cos(x2)']])

        # b = Matrix([['sin(x1)', 'cos(x2)', 'x1**2 + x3**2'],
        #             ['x3**(1/2)', 'x1 * x2', '5'],
        #             ['cos(2 * x3)', 'sin(x1 / 2)', 'x1**2 * x3**2']])

        # b = Matrix([['x1', 'cos(x2)', 'x1**2 + x3**2'],
        #             ['x3**(1/2)', 'x1 * x2', '5'],
        #             ['cos(2 * x3)', 'sin(x1 / 2)', 'x1**2 * x3**2']])

        sym_b = sp.MatrixSymbol('b', 2, 2)

        diff_args = sp.symbols('x1 x2')

        print()
        # sp.pprint(G(b[:, 1], b[1, 0], diff_args))
        # sp.pprint(G(b[:, 1], b[2, 1], diff_args))
        # sp.pprint(G(b[:, 0], G(b[:, 0], b[0, 0], diff_args).doit(), diff_args))
        # sp.pprint(G(sym_b[:, 0], sym_a[0, 0], diff_args))
        # sp.pprint(G(sym_b[:, 0], G(b[:, 0], sym_b[0, 0], diff_args) + 
        # G(b[:, 0], b[0, 0], diff_args), diff_args).doit())
        # sp.pprint(G(b[:, 0], G(b[:, 0], b[0, 0], diff_args), diff_args).doit())
        # sp.pprint(G(b[:, 0], G(b[:, 0], diff_args[0], diff_args), diff_args).doit())
        # sp.pprint(G(b[:, 0], G(b[:, 0], S(1), diff_args), diff_args).doit())
        # sp.pprint(f.G(b[:, 0], f.G(b[:, 1], sp.S.One, diff_args), diff_args).doit())
        # sp.pprint(f.G(b[:, 0], f.G(b[:, 1], b[0, 0], diff_args), diff_args).doit())
        # sp.pprint(f.G(b[:, 1], f.G(b[:, 0], b[0, 0], diff_args), diff_args).doit())
        # sp.pprint(f.G(b[:, 1], f.G(b[:, 1], b[0, 0], diff_args), diff_args).doit())
        sp.pprint(f.G(b[:, 1], sp.S.One + f.G(b[:, 1], b[0, 0], diff_args), diff_args).doit())

        self.assertEqual(True, True)

    @unittest.skip('Success')
    def test_C(self):
        print()
        db.connect(c.database)

        i1, i2, i3 = sp.symbols('i1 i2 i3')

        exp = i1 + f.C(i1, i2, i3)
        sp.pprint(exp)

        exp = i1 + f.C(sp.S(8), sp.S(9), sp.S(9), sp.S(0.001)).doit()
        sp.pprint(exp)

        db.disconnect()

        self.assertEqual(True, True)

    @unittest.skip('Success')
    def test_Ind(self):
        i1, i2 = sp.symbols('i1 i2')

        print()
        exp = f.Ind(i1, i2)
        sp.pprint(exp)

        print()
        exp = f.Ind(1, 2)
        sp.pprint(exp)

        self.assertEqual(True, True)

    @unittest.skip('Success')
    def test_Io(self):
        i = sp.symbols('i')
        ksi = sp.MatrixSymbol('ksi', 100, 100)
        dt = sp.Symbol('dt')

        print()
        exp = f.Io(i, dt, ksi).doit()
        sp.pprint(exp)

        print()
        exp = f.Io(1, dt, ksi).doit()
        sp.pprint(exp)

        print()
        try:
            exp = f.Io(i).doit()
            sp.pprint(exp)
        except Exception as e:
            print(e)

        print()
        f.Io.dt = sp.Symbol('dt')
        f.Io.ksi = sp.MatrixSymbol('ksi', 2, 2)
        exp = f.Io(i).doit()
        sp.pprint(exp)

        self.assertEqual(True, True)

    @unittest.skip('Success')
    def test_Ioo(self):
        i1, i2, q = sp.symbols('i1 i2 q')
        ksi = sp.MatrixSymbol('ksi', 100, 100)
        dt = sp.Symbol('dt')

        print()
        exp = f.Ioo(i1, i2, q, dt, ksi)
        sp.pprint(exp)

        print()
        exp = f.Ioo(1, 2, 10, dt, ksi)
        sp.pprint(exp)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
