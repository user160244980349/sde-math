import logging
import unittest
from multiprocessing import Pool, cpu_count
from pprint import pprint
from sys import setrecursionlimit
from time import time

import numpy as np
from sympy import Add, symbols
from sympy import Matrix

import config as c
import tools.database as db
from mathematics.sde.nonlinear.drivers.strong_taylor_stratonovich_3p0_mp import strong_taylor_stratonovich_3p0_mp
from mathematics.sde.nonlinear.symbolic.coefficients.c import C
from mathematics.sde.nonlinear.symbolic.coefficients.c000000 import C000000
from mathematics.sde.nonlinear.symbolic.g import G
from mathematics.sde.nonlinear.symbolic.schemes.strong_taylor_stratonovich_3p0_mp import ranges


class DoDiff:
    def __init__(self, b):
        self.b = b

    def __call__(self, x):
        b = self.b
        return Add(*[G(b[:, 1], b[0, 0], symbols("x1 x2")) for _ in range(x)])


class DoApprox:
    def __init__(self, b):
        self.b = b

    def __call__(self, x):
        b = self.b
        dt = 0.01
        ksi = np.random(n, m)

        return Add(*[
            C000000(j6, j5, j4, j3, j2, j1, dt) *
            ksi[j1, i1] * ksi[j2, i2] * ksi[j3, i3] *
            ksi[j4, i4] * ksi[j5, i5] * ksi[j6, i6]
            for j6 in range(q + 1)
            for j5 in range(q + 1)
            for j4 in range(q + 1)
            for j3 in range(q + 1)
            for j2 in range(q + 1)
            for j1 in range(q + 1)])


class TestMP(unittest.TestCase):

    @unittest.skip("Success")
    def test_ranges(self):
        pprint(ranges(50, 100))

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_strat_mp(self):
        logging.basicConfig(level=logging.INFO)
        setrecursionlimit(c.recursion_limit)

        # init()

        db.connect("../resources/database.db")

        y0 = np.array([
            [1],
            [1.5]
        ])

        m_a = Matrix([
            "-5 * x1",
            "-5 * x2"
        ])

        m_b = Matrix([
            ["0.5 * sin(x1)", "x2"],
            ["x2", "0.5 * cos(x1)"]
        ])

        C.preload(56, 56, 56, 56, 56)

        taylor_higher_orders = (y0, m_a, m_b, 1, (0, 1, 20))

        # Euler
        np.random.seed(703)
        y, t = strong_taylor_stratonovich_3p0_mp(*taylor_higher_orders)

        db.disconnect()

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_mp(self):
        start_time = time()

        b = Matrix([
            ["0.5 * sin(x1) - 0.5 * cos(x2)", "0.75 * sin(x1) - 0.75 * cos(x2)"],
            ["-0.5 * sin(x1) + 0.5 * cos(x2)", "-0.75 * sin(x1) + 0.75 * cos(x2)"]
        ])

        input = [i for i in range(500)]

        with Pool(cpu_count()) as pool:
            r1 = pool.map(DoDiff(b), input)
            r2 = pool.map(DoApprox(b), input)
            pool.close()
            pool.join()

        # print(r)
        print(f"mp: {time() - start_time}")

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_sp(self):
        start_time = time()

        b = Matrix([
            ["0.5 * sin(x1) - 0.5 * cos(x2)", "0.75 * sin(x1) - 0.75 * cos(x2)"],
            ["-0.5 * sin(x1) + 0.5 * cos(x2)", "-0.75 * sin(x1) + 0.75 * cos(x2)"]
        ])

        r = [doit(b) for _ in range(500)]

        # print(r)
        print(f"sp: {time() - start_time}")

        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
