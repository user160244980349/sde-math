import unittest

from sympy import S

from mathematics.sde.nonlinear.c import get_c


class TestC(unittest.TestCase):
    def test_c_xxx(self):
        samples = [
            [((0, 0, 0), (0, 0, 0)), S(4) / S(3)],
            [((0, 0, 1), (0, 0, 0)), S(-2) / S(3)],
            [((2, 1, 5), (0, 0, 0)), S(8) / S(3465)],
            [((2, 3, 2), (0, 0, 0)), S(0)],
            [((3, 0, 5), (0, 0, 0)), S(2) / S(693)],
            [((3, 3, 0), (0, 0, 0)), S(2) / S(315)],
            [((4, 6, 6), (0, 0, 0)), S(-2) / S(188955)],
            [((6, 6, 2), (0, 0, 0)), S(-4) / S(36465)]
        ]

        for i, e in samples:
            with self.subTest(i=i, e=e):
                self.assertEqual(get_c(i[0], i[1]), e)

    def test_c_xxxx(self):
        samples = [
            [((0, 0, 0, 0), (0, 0, 0, 0)), S(2) / S(3)],
            [((1, 0, 0, 1), (0, 0, 0, 0)), S(-2) / S(9)],
            [((1, 2, 0, 0), (0, 0, 0, 0)), S(-2) / S(35)],
            [((1, 2, 2, 0), (0, 0, 0, 0)), S(2) / S(105)],
            [((2, 0, 0, 1), (0, 0, 0, 0)), S(-2) / S(35)],
            [((2, 0, 2, 1), (0, 0, 0, 0)), S(2) / S(105)],
            [((2, 1, 0, 0), (0, 0, 0, 0)), S(2) / S(21)],
            [((2, 1, 2, 1), (0, 0, 0, 0)), S(2) / S(225)]
        ]

        for i, s in samples:
            with self.subTest(s=s):
                self.assertEqual(get_c(i[0], i[1]), s)

    def test_c_xxxxx(self):
        samples = [
            [((0, 0, 0, 0, 0), (0, 0, 0, 0, 0)), S(4) / S(15)],
            [((0, 0, 0, 1, 0), (0, 0, 0, 0, 0)), S(-4) / S(45)],
            [((0, 0, 1, 0, 1), (0, 0, 0, 0, 0)), S(4) / S(315)],
            [((0, 1, 0, 1, 0), (0, 0, 0, 0, 0)), S(-4) / S(315)],
            [((0, 1, 1, 1, 1), (0, 0, 0, 0, 0)), S(2) / S(945)],
            [((1, 0, 0, 1, 0), (0, 0, 0, 0, 0)), S(-16) / S(315)],
            [((1, 0, 1, 0, 1), (0, 0, 0, 0, 0)), S(0)],
            [((1, 1, 0, 0, 1), (0, 0, 0, 0, 0)), S(-2) / S(45)]
        ]

        for i, s in samples:
            with self.subTest(s=s):
                self.assertEqual(get_c(i[0], i[1]), s)

    def test_c_xxx_xxx(self):
        samples = [
            [((2, 0, 0), (0, 0, 1)), S(-2) / S(5)],
            [((2, 0, 1), (0, 0, 1)), S(2) / S(21)],
            [((2, 0, 2), (0, 0, 1)), S(4) / S(105)],
            [((2, 1, 0), (0, 0, 1)), S(-22) / S(105)],
            [((2, 1, 1), (0, 0, 1)), S(4) / S(105)],
            [((2, 1, 2), (0, 0, 1)), S(2) / S(105)],
            [((2, 2, 0), (0, 0, 1)), S(0)],
            [((2, 2, 1), (0, 0, 1)), S(-2) / S(105)],
            [((2, 2, 2), (0, 0, 1)), S(0)],
            [((1, 0, 0), (1, 0, 0)), S(-2) / S(5)],
            [((1, 0, 1), (1, 0, 0)), S(2) / S(45)],
            [((1, 0, 2), (1, 0, 0)), S(2) / S(21)],
            [((1, 1, 0), (1, 0, 0)), S(-2) / S(15)],
            [((1, 1, 1), (1, 0, 0)), S(-2) / S(105)],
            [((1, 1, 2), (1, 0, 0)), S(4) / S(105)],
            [((1, 2, 0), (1, 0, 0)), S(2) / S(35)],
            [((1, 2, 1), (1, 0, 0)), S(-2) / S(63)],
            [((1, 2, 2), (1, 0, 0)), S(-2) / S(105)]
        ]

        for i, s in samples:
            with self.subTest(s=s):
                self.assertEqual(get_c(i[0], i[1]), s)


if __name__ == "__main__":
    unittest.main()
