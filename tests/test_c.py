import unittest

import sympy as sp

import mathematics.sde.nonlinear.c as c


class TestC(unittest.TestCase):
    def test_c_xxx(self):
        samples = [[[0, 0, 0], sp.S(4) / sp.S(3)],
                   [[0, 0, 1], sp.S(-2) / sp.S(3)],
                   [[2, 1, 5], sp.S(8) / sp.S(3465)],
                   [[2, 3, 2], sp.S(0)],
                   [[3, 0, 5], sp.S(2) / sp.S(693)],
                   [[3, 3, 0], sp.S(2) / sp.S(315)],
                   [[4, 6, 6], sp.S(-2) / sp.S(188955)],
                   [[6, 6, 2], sp.S(-4) / sp.S(36465)]]

        for i, e in samples:
            with self.subTest(i=i, e=e):
                self.assertEqual(c.getc(i), e)

    def test_c_xxxx(self):
        samples = [[[0, 0, 0, 0], sp.S(2) / sp.S(3)],
                   [[1, 0, 0, 1], sp.S(-2) / sp.S(9)],
                   [[1, 2, 0, 0], sp.S(-2) / sp.S(35)],
                   [[1, 2, 2, 0], sp.S(2) / sp.S(105)],
                   [[2, 0, 0, 1], sp.S(-2) / sp.S(35)],
                   [[2, 0, 2, 1], sp.S(2) / sp.S(105)],
                   [[2, 1, 0, 0], sp.S(2) / sp.S(21)],
                   [[2, 1, 2, 1], sp.S(2) / sp.S(225)]]

        for s in samples:
            with self.subTest(s=s):
                self.assertEqual(c.getc(s[0]), s[1])

    def test_c_xxxxx(self):
        samples = [[[0, 0, 0, 0, 0], sp.S(4) / sp.S(15)],
                   [[0, 0, 0, 1, 0], sp.S(-4) / sp.S(45)],
                   [[0, 0, 1, 0, 1], sp.S(4) / sp.S(315)],
                   [[0, 1, 0, 1, 0], sp.S(-4) / sp.S(315)],
                   [[0, 1, 1, 1, 1], sp.S(2) / sp.S(945)],
                   [[1, 0, 0, 1, 0], sp.S(-16) / sp.S(315)],
                   [[1, 0, 1, 0, 1], sp.S(0)],
                   [[1, 1, 0, 0, 1], sp.S(-2) / sp.S(45)]]

        for s in samples:
            with self.subTest(s=s):
                self.assertEqual(c.getc(s[0]), s[1])

    def test_c_xxx_xxx(self):

        x = sp.Symbol('x')

        samples = [[[[2, 0, 0], [1, 1, x + 1]], sp.S(-2) / sp.S(5)],
                   [[[2, 0, 1], [1, 1, x + 1]], sp.S(2) / sp.S(21)],
                   [[[2, 0, 2], [1, 1, x + 1]], sp.S(4) / sp.S(105)],
                   [[[2, 1, 0], [1, 1, x + 1]], sp.S(-22) / sp.S(105)],
                   [[[2, 1, 1], [1, 1, x + 1]], sp.S(4) / sp.S(105)],
                   [[[2, 1, 2], [1, 1, x + 1]], sp.S(2) / sp.S(105)],
                   [[[2, 2, 0], [1, 1, x + 1]], sp.S(0)],
                   [[[2, 2, 1], [1, 1, x + 1]], sp.S(-2) / sp.S(105)],
                   [[[2, 2, 2], [1, 1, x + 1]], sp.S(0)],
                   [[[1, 0, 0], [x + 1, 1, 1]], sp.S(-2) / sp.S(5)],
                   [[[1, 0, 1], [x + 1, 1, 1]], sp.S(2) / sp.S(45)],
                   [[[1, 0, 2], [x + 1, 1, 1]], sp.S(2) / sp.S(21)],
                   [[[1, 1, 0], [x + 1, 1, 1]], sp.S(-2) / sp.S(15)],
                   [[[1, 1, 1], [x + 1, 1, 1]], sp.S(-2) / sp.S(105)],
                   [[[1, 1, 2], [x + 1, 1, 1]], sp.S(4) / sp.S(105)],
                   [[[1, 2, 0], [x + 1, 1, 1]], sp.S(2) / sp.S(35)],
                   [[[1, 2, 1], [x + 1, 1, 1]], sp.S(-2) / sp.S(63)],
                   [[[1, 2, 2], [x + 1, 1, 1]], sp.S(-2) / sp.S(105)]]

        for s in samples:
            with self.subTest(s=s):
                self.assertEqual(c.getcw(s[0][0], s[0][1]), s[1])


if __name__ == '__main__':
    unittest.main()
