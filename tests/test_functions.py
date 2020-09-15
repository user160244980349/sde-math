import unittest

import sympy as sp

import config as c
import tools.database as db
from mathematics.sde.nonlinear.functions.aj import Aj
from mathematics.sde.nonlinear.functions.coefficients.c import C
from mathematics.sde.nonlinear.functions.g import G
from mathematics.sde.nonlinear.functions.ind import Ind
from mathematics.sde.nonlinear.functions.ito.i0 import I0
from mathematics.sde.nonlinear.functions.ito.i00 import I00
from mathematics.sde.nonlinear.functions.ito.i000 import I000
from mathematics.sde.nonlinear.functions.l import L
from mathematics.sde.nonlinear.functions.lj import Lj
from mathematics.sde.nonlinear.q import get_q


class MyTestCase(unittest.TestCase):
    # @unittest.skip("Success")
    def test_q(self):
        print()
        db.connect(c.database)

        dt = 0.01
        eps = 0.0000001

        print(get_q((0, 1, 2), dt, eps))

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_Lj(self):
        a = sp.Matrix([
            "x1**2 * x2**2 * t",
            "x2 * x1**2 * 5 * t**3"
        ])

        ad = Aj(a)

        b = sp.Matrix([
            ["sin(x1)", "cos(x2)", "cos(2 * x1)"],
            ["x2**2", "t * x1**2", "t * x2**3"]
        ])

        diff_args = sp.symbols("x1 x2")
        i = sp.Symbol("i")

        sym_b = sp.MatrixSymbol("b", 2, 2)

        print()
        sp.pprint(Lj(a, b, a[0, 0], diff_args))

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_Aj(self):
        a = sp.Matrix([
            ["x1**2 * x2**2 * t"],
            ["x2 * x1**2 * 5 * t**3"]
        ])

        b = sp.Matrix([
            ["sin(x1)", "cos(x2)", "cos(2 * x1)"],
            ["x2**2", "t * x1**2", "t * x2**3"]
        ])

        diff_args = sp.symbols("x1 x2")
        i = sp.Symbol("i")

        sym_b = sp.MatrixSymbol("b", 2, 2)

        print()
        sp.pprint(Aj(i, a, b, diff_args))

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_preload(self):
        print()
        db.connect(c.database)
        C.preload(3, 4)
        print(C._preloaded)
        db.disconnect()

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_I000(self):
        q, m = 3, 2

        db.connect(c.database)

        dt = sp.symbols("dt")
        ksi = sp.MatrixSymbol("ksi", q + 1, m)
        sp.pprint(I000(1, 1, 1, q, dt, ksi))

        db.disconnect()

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_L(self):
        x1, x2, x3, x4, t = sp.symbols("x1 x2 x3 x4 t")
        exp = x1 ** 2 * x2 ** 2 * t ** 3

        a = sp.Matrix([
            ["x1**2 * x2**2 * t"],
            ["x2 * x1**2 * 5 * t**3"]
        ])

        b = sp.Matrix([
            ["sin(x1)", "cos(x2)", "cos(2 * x1)"],
            ["x2**2", "t * x1**2", "t * x2**3"]
        ])

        diff_args = sp.symbols("x1 x2")

        print()
        sp.pprint(L(a, b, L(a, b, exp, diff_args) + L(a, b, exp, diff_args), diff_args))
        sp.pprint(L(a, b, sp.S.One + L(a, b, exp, diff_args), diff_args))
        sp.pprint(L(a, b, diff_args[0], diff_args))
        sp.pprint(L(a, b, b[0, 0], diff_args))
        sp.pprint(L(a, b, L(a, b, sp.S.One, diff_args), diff_args))

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_G(self):
        a = sp.Matrix([
            "-5 * x1",
            "-5 * x2"
        ])
        sym_a = sp.MatrixSymbol("a", 2, 1)

        b = sp.Matrix([
            ["0.5 * sin(x1) - 0.5 * cos(x2)", "0.75 * sin(x1) - 0.75 * cos(x2)"],
            ["-0.5 * sin(x1) + 0.5 * cos(x2)", "-0.75 * sin(x1) + 0.75 * cos(x2)"]
        ])
        sym_b = sp.MatrixSymbol("b", 2, 2)

        diff_args = sp.symbols("x1 x2")

        print()
        sp.pprint(G(b[:, 1], b[0, 0], diff_args))
        sp.pprint(G(b[:, 1], b[1, 0], diff_args))
        sp.pprint(G(b[:, 1], b[1, 1], diff_args))
        sp.pprint(G(b[:, 0], G(b[:, 0], b[0, 0], diff_args), diff_args))
        sp.pprint(G(sym_b[:, 0], sym_a[0, 0], diff_args))
        sp.pprint(G(sym_b[:, 0], G(b[:, 0], sym_b[0, 0], diff_args) + G(b[:, 0], b[0, 0], diff_args), diff_args))
        sp.pprint(G(b[:, 0], G(b[:, 0], b[0, 0], diff_args), diff_args))
        sp.pprint(G(b[:, 0], G(b[:, 0], diff_args[0], diff_args), diff_args))
        sp.pprint(G(b[:, 0], G(b[:, 0], sp.S.One, diff_args), diff_args))
        sp.pprint(G(b[:, 0], G(b[:, 1], sp.S.One, diff_args), diff_args))
        sp.pprint(G(b[:, 0], G(b[:, 1], b[0, 0], diff_args), diff_args))
        sp.pprint(G(b[:, 1], G(b[:, 0], b[0, 0], diff_args), diff_args))
        sp.pprint(G(b[:, 1], G(b[:, 1], b[0, 0], diff_args), diff_args))
        sp.pprint(G(b[:, 1], sp.S.One + G(b[:, 1], b[0, 0], diff_args), diff_args))

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_C(self):
        print()
        db.connect(c.database)

        i1, i2, i3 = sp.symbols("i1 i2 i3")

        exp = i1 + C((i1, i2, i3), (0, 0, 0))
        sp.pprint(exp)

        exp = i1 + C((8, 9, 9), (0, 0, 0))
        sp.pprint(exp)

        db.disconnect()

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_Ind(self):
        i1, i2 = sp.symbols("i1 i2")

        print()
        exp = Ind(i1, i2)
        sp.pprint(exp)

        exp = Ind(1, 2)
        sp.pprint(exp)

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_I0(self):
        i = sp.symbols("i")
        ksi = sp.MatrixSymbol("ksi", 100, 100)
        dt = sp.Symbol("dt")

        print()
        exp = I0(i, dt, ksi)
        sp.pprint(exp)

        exp = I0(1, dt, ksi)
        sp.pprint(exp)

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_I00(self):
        i1, i2, q = sp.symbols("i1 i2 q")
        ksi = sp.MatrixSymbol("ksi", 100, 100)
        dt = sp.Symbol("dt")

        exp = I00(i1, i2, q, dt, ksi)
        sp.pprint(exp)

        exp = I00(1, 2, 10, dt, ksi)
        sp.pprint(exp)

        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
