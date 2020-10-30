import unittest
from copy import copy
from multiprocessing import Pool, cpu_count
from time import time

from sympy import Add, Matrix, MatrixSymbol, symbols

from mathematics.sde.nonlinear.symbolic.g import G


def doit(b):

    diff_args = symbols("x1 x2")

    return Add(
        *[G(b[:, 1], b[0, 0], diff_args)
          for _ in range(500)]
    )


class TestMP(unittest.TestCase):

    def test_mp(self):
        start_time = time()

        b = Matrix([
            ["0.5 * sin(x1) - 0.5 * cos(x2)", "0.75 * sin(x1) - 0.75 * cos(x2)"],
            ["-0.5 * sin(x1) + 0.5 * cos(x2)", "-0.75 * sin(x1) + 0.75 * cos(x2)"]
        ])

        input = [b for _ in range(500)]

        with Pool(cpu_count()) as pool:
            r = pool.map(doit, input)
            pool.close()
            pool.join()

        # print(r)
        print(f"mp: {time() - start_time}")

        self.assertEqual(True, True)

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
