import logging
import unittest

from sympy import Matrix, Symbol, symbols, MatrixSymbol, pprint

import config as c
import tools.database as db
from mathematics.sde.nonlinear.q import get_q
from mathematics.sde.nonlinear.symbolic.aj import Aj
from mathematics.sde.nonlinear.symbolic.coefficients.c import C
from mathematics.sde.nonlinear.symbolic.g import G
from mathematics.sde.nonlinear.symbolic.ind import Ind
from mathematics.sde.nonlinear.symbolic.ito.i0 import I0
from mathematics.sde.nonlinear.symbolic.ito.i00 import I00
from mathematics.sde.nonlinear.symbolic.ito.i000 import I000
from mathematics.sde.nonlinear.symbolic.l import L
from mathematics.sde.nonlinear.symbolic.lj import Lj

logging.basicConfig(level=logging.INFO)


class MyTestCase(unittest.TestCase):
    @unittest.skip("Success")
    def test_q(self):
        print()
        db.connect(c.database)

        # get_q(dt: float, k: float, r: float)
        # print(f"1.0 :{get_q(2 ** (-6), 1, 1.0)}")
        # print(f"1.5 :{get_q(0.05, 1, 1.5)}")
        print(f"2.0 :{get_q(0.1, 1, 2.0)}")
        # print(f"2.5 :{get_q(0.11736, 1, 2.5)}")
        # print(f"3.0 :{get_q(0.11736, 1, 3.0)}")

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_Lj(self):
        a = Matrix([
            "x1**2 * x2**2 * t",
            "x2 * x1**2 * 5 * t**3"
        ])

        ad = Aj(a)

        b = Matrix([
            ["sin(x1)", "cos(x2)", "cos(2 * x1)"],
            ["x2**2", "t * x1**2", "t * x2**3"]
        ])

        diff_args = symbols("x1 x2")
        i = Symbol("i")

        sym_b = MatrixSymbol("b", 2, 2)

        print()
        pprint(Lj(a, b, a[0, 0], diff_args))

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_Aj(self):
        a = Matrix([
            ["x1**2 * x2**2 * t"],
            ["x2 * x1**2 * 5 * t**3"]
        ])

        b = Matrix([
            ["sin(x1)", "cos(x2)", "cos(2 * x1)"],
            ["x2**2", "t * x1**2", "t * x2**3"]
        ])

        diff_args = symbols("x1 x2")
        i = Symbol("i")

        sym_b = MatrixSymbol("b", 2, 2)

        print()
        pprint(Aj(i, a, b, diff_args))

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

        dt = symbols("dt")
        ksi = MatrixSymbol("ksi", q + 1, m)
        pprint(I000(1, 1, 1, q, dt, ksi))

        db.disconnect()

        self.assertEqual(True, True)

    # @unittest.skip("Success")
    def test_L(self):
        # exp = x1 ** 2 * x2 ** 2 * t ** 3

        a = Matrix([
            ["cos(x1**2 + x2**2 + 2 * t**2)"],
            ["sin(x1**2 - x2**2 + 3 * t**2)"]
        ])

        b = Matrix([
            ["sin(x1**2 + x2**2 - t**2)", "x1**2 * x2**3 * t**2"],
            ["x1**3 * x2**2 * t**2", "cos(x1**2 + x2**2 + t**2)"]
        ])

        diff_args = symbols("x1 x2 t")

        print()
        # pprint(L(a, b, L(a, b, exp, diff_args) + L(a, b, exp, diff_args), diff_args))
        # pprint(L(a, b, S.One + L(a, b, exp, diff_args), diff_args))
        # pprint(L(a, b, diff_args[0], diff_args))
        # pprint(L(a, b, b[0, 0], diff_args))
        # pprint(L(a, b, L(a, b, S.One, diff_args), diff_args))

        # print("a:")
        # pprint(a)

        print("L(a1):")
        print(L(a, b, a[0, 0], diff_args))

        print("L(a2):")
        print(L(a, b, a[1, 0], diff_args))

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_G(self):
        # a = Matrix([
        #     "-5 * x1",
        #     "-5 * x2"
        # ])
        a = Matrix([
            ["cos(x1**2 + x2**2 + 2 * t**2)"],
            ["sin(x1**2 - x2**2 + 3 * t**2)"]
        ])
        # sym_a = MatrixSymbol("a", 2, 1)

        # b = Matrix([
        #     ["0.5 * sin(x1) - 0.5 * cos(x2)", "0.75 * sin(x1) - 0.75 * cos(x2)"],
        #     ["-0.5 * sin(x1) + 0.5 * cos(x2)", "-0.75 * sin(x1) + 0.75 * cos(x2)"]
        # ])
        b = Matrix([
            ["sin(x1**2 + x2**2 - t**2)", "x1**2 * x2**3 * t**2"],
            ["x1**3 * x2**2 * t**2", "cos(x1**2 + x2**2 + t**2)"]
        ])
        # sym_b = MatrixSymbol("b", 2, 2)

        diff_args = symbols("x1 x2")

        print()

        print("G1(B11):")
        print(G(b[:, 0], b[0, 0], diff_args))

        print("G1(B12):")
        print(G(b[:, 0], b[0, 1], diff_args))

        print("G1(B21):")
        print(G(b[:, 0], b[1, 0], diff_args))

        print("G1(B22):")
        print(G(b[:, 0], b[1, 1], diff_args))

        print("G2(B11):")
        print(G(b[:, 1], b[0, 0], diff_args))

        print("G2(B12):")
        print(G(b[:, 1], b[0, 1], diff_args))

        print("G2(B21):")
        print(G(b[:, 1], b[1, 0], diff_args))

        print("G2(B22):")
        print(G(b[:, 1], b[1, 1], diff_args))
        # pprint(G(b[:, 1], b[1, 0], diff_args))
        # pprint(G(b[:, 1], b[1, 1], diff_args))
        # pprint(G(b[:, 0], G(b[:, 0], b[0, 0], diff_args), diff_args))
        # pprint(G(sym_b[:, 0], sym_a[0, 0], diff_args))
        # pprint(G(sym_b[:, 0], G(b[:, 0], sym_b[0, 0], diff_args) + G(b[:, 0], b[0, 0], diff_args), diff_args))
        # pprint(G(b[:, 0], G(b[:, 0], b[0, 0], diff_args), diff_args))
        # pprint(G(b[:, 0], G(b[:, 0], diff_args[0], diff_args), diff_args))
        # pprint(G(b[:, 0], G(b[:, 0], S.One, diff_args), diff_args))
        # pprint(G(b[:, 0], G(b[:, 1], S.One, diff_args), diff_args))
        # pprint(G(b[:, 0], G(b[:, 1], b[0, 0], diff_args), diff_args))
        # pprint(G(b[:, 1], G(b[:, 0], b[0, 0], diff_args), diff_args))
        # pprint(G(b[:, 1], G(b[:, 1], b[0, 0], diff_args), diff_args))
        # pprint(G(b[:, 1], S.One + G(b[:, 1], b[0, 0], diff_args), diff_args))
        #
        # print("G(a1):")
        # pprint(L(a, b, b[0, 0], diff_args))
        # print("G(a2):")

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_C(self):
        print()
        db.connect(c.database)

        i1, i2, i3 = symbols("i1 i2 i3")

        exp = i1 + C((i1, i2, i3), (0, 0, 0))
        pprint(exp)

        exp = i1 + C((8, 9, 9), (0, 0, 0))
        pprint(exp)

        db.disconnect()

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_Ind(self):
        i1, i2 = symbols("i1 i2")

        print()
        exp = Ind(i1, i2)
        pprint(exp)

        exp = Ind(1, 2)
        pprint(exp)

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_I0(self):
        i = symbols("i")
        ksi = MatrixSymbol("ksi", 100, 100)
        dt = Symbol("dt")

        print()
        exp = I0(i, dt, ksi)
        pprint(exp)

        exp = I0(1, dt, ksi)
        pprint(exp)

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_I00(self):
        i1, i2, q = symbols("i1 i2 q")
        ksi = MatrixSymbol("ksi", 100, 100)
        dt = Symbol("dt")

        exp = I00(i1, i2, q, dt, ksi)
        pprint(exp)

        exp = I00(1, 2, 10, dt, ksi)
        pprint(exp)

        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
