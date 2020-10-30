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
from init.init import init
from mathematics.sde.nonlinear.drivers.strong_taylor_stratonovich_3p0_mp import strong_taylor_stratonovich_3p0_mp
from mathematics.sde.nonlinear.symbolic.coefficients.c import C
from mathematics.sde.nonlinear.symbolic.g import G
from mathematics.sde.nonlinear.symbolic.schemes.strong_taylor_stratonovich_3p0_mp import ranges


def doit(b):
    diff_args = symbols("x1 x2")

    return Add(
        *[G(b[:, 1], b[0, 0], diff_args)
          for _ in range(500)]
    )


class Doit:
    def __init__(self, b):
        self.b = b

    def __call__(self, x):
        b = self.b
        return Add(*[G(b[:, 1], b[0, 0], symbols("x1 x2")) for _ in range(x)])


class TestMP(unittest.TestCase):

    def test_ranges(self):

        pprint(ranges(50, 100))

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_strat_mp(self):

        logging.basicConfig(level=logging.INFO)
        setrecursionlimit(c.recursion_limit)

        db.connect(c.database)

        init()

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

        taylor_higher_orders = (y0, m_a, m_b, 0.1, (0, 0.07, 20))

        # Euler
        np.random.seed(703)
        y, t = strong_taylor_stratonovich_3p0_mp(*taylor_higher_orders)

        self.assertEqual(True, True)

    @unittest.skip("Success")
    def test_mp(self):
        start_time = time()

        b = Matrix([
            ["0.5 * sin(x1) - 0.5 * cos(x2)", "0.75 * sin(x1) - 0.75 * cos(x2)"],
            ["-0.5 * sin(x1) + 0.5 * cos(x2)", "-0.75 * sin(x1) + 0.75 * cos(x2)"]
        ])

        input = [i for i in range(500)]

        print(cpu_count())
        with Pool(cpu_count()) as pool:
            r = pool.map(Doit(b), input)
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
