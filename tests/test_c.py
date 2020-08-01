import unittest

from sympy import S, Symbol

from mathematics.sde.nonlinear.c import getc, getcw


class TestC(unittest.TestCase):
    def test_c_xxx(self):
        samples = [[[0, 0, 0], S(4) / S(3)],
                   [[0, 0, 1], S(-2) / S(3)],
                   [[2, 1, 5], S(8) / S(3465)],
                   [[2, 3, 2], S(0)],
                   [[3, 0, 5], S(2) / S(693)],
                   [[3, 3, 0], S(2) / S(315)],
                   [[4, 6, 6], S(-2) / S(188955)],
                   [[6, 6, 2], S(-4) / S(36465)]]

        for i, e in samples:
            with self.subTest(i=i, e=e):
                self.assertEqual(getc(i), e)

    def test_c_xxxx(self):
        samples = [[[0, 0, 0, 0], S(2) / S(3)],
                   [[1, 0, 0, 1], S(-2) / S(9)],
                   [[1, 2, 0, 0], S(-2) / S(35)],
                   [[1, 2, 2, 0], S(2) / S(105)],
                   [[2, 0, 0, 1], S(-2) / S(35)],
                   [[2, 0, 2, 1], S(2) / S(105)],
                   [[2, 1, 0, 0], S(2) / S(21)],
                   [[2, 1, 2, 1], S(2) / S(225)]]

        for s in samples:
            with self.subTest(s=s):
                self.assertEqual(getc(s[0]), s[1])

    def test_c_xxxxx(self):
        samples = [[[0, 0, 0, 0, 0], S(4) / S(15)],
                   [[0, 0, 0, 1, 0], S(-4) / S(45)],
                   [[0, 0, 1, 0, 1], S(4) / S(315)],
                   [[0, 1, 0, 1, 0], S(-4) / S(315)],
                   [[0, 1, 1, 1, 1], S(2) / S(945)],
                   [[1, 0, 0, 1, 0], S(-16) / S(315)],
                   [[1, 0, 1, 0, 1], S(0)],
                   [[1, 1, 0, 0, 1], S(-2) / S(45)]]

        for s in samples:
            with self.subTest(s=s):
                self.assertEqual(getc(s[0]), s[1])

    def test_c_xxx_xxx(self):

        x = Symbol('x')

        samples = [[[[2, 0, 0], [1, 1, x + 1]], S(-2) / S(5)],
                   [[[2, 0, 1], [1, 1, x + 1]], S(2) / S(21)],
                   [[[2, 0, 2], [1, 1, x + 1]], S(4) / S(105)],
                   [[[2, 1, 0], [1, 1, x + 1]], S(-22) / S(105)],
                   [[[2, 1, 1], [1, 1, x + 1]], S(4) / S(105)],
                   [[[2, 1, 2], [1, 1, x + 1]], S(2) / S(105)],
                   [[[2, 2, 0], [1, 1, x + 1]], S(0)],
                   [[[2, 2, 1], [1, 1, x + 1]], S(-2) / S(105)],
                   [[[2, 2, 2], [1, 1, x + 1]], S(0)],
                   [[[1, 0, 0], [x + 1, 1, 1]], S(-2) / S(5)],
                   [[[1, 0, 1], [x + 1, 1, 1]], S(2) / S(45)],
                   [[[1, 0, 2], [x + 1, 1, 1]], S(2) / S(21)],
                   [[[1, 1, 0], [x + 1, 1, 1]], S(-2) / S(15)],
                   [[[1, 1, 1], [x + 1, 1, 1]], S(-2) / S(105)],
                   [[[1, 1, 2], [x + 1, 1, 1]], S(4) / S(105)],
                   [[[1, 2, 0], [x + 1, 1, 1]], S(2) / S(35)],
                   [[[1, 2, 1], [x + 1, 1, 1]], S(-2) / S(63)],
                   [[[1, 2, 2], [x + 1, 1, 1]], S(-2) / S(105)]]

        for s in samples:
            with self.subTest(s=s):
                self.assertEqual(getcw(s[0][0], s[0][1]), s[1])


if __name__ == '__main__':
    unittest.main()
