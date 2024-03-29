#!/usr/bin/env python
import logging
import os
import unittest

import config as c
import tools.database as db
from mathematics.sde.nonlinear.symbolic.coefficients.c import C


class TestHypothesis(unittest.TestCase):

    # @unittest.skip("Success")
    def test_run(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%H:%M:%S"
        )

        db.connect(c.database)

        C.preload(56, 56, 56, 56, 56)

        # m()
        # t1p5()
        # t1p5exponential()
        # t1p5fixed()
        t1p5s()
        t1p5sexponential()
        t1p5sfixed()
        # t2p0()
        # t2p5()


def m():
    dts = [2 ** (-1), 2 ** (-4), 2 ** (-8), 2 ** (-12)]

    print(f" # ============================================ #\n"
          f" # MILSTEIN\n"
          f" # dts = [2**(-1), 2**(-4), 2**(-8), 2**(-12)]\n"
          f" # dts = {dts}\n"
          f" # ============================================ #\n")

    for dt in dts:
        print(f"dt = {dt},\n\n"
              f"\tq = {q(dt)}\n\n")


def t1p5():
    dts = [0.011, 0.008, 0.0045, 0.0035, 0.0027, 0.0025]
    ps = [0, 0, 0, 0, 0, 0]

    print(f" # ============================================ #\n"
          f" # TAYLOR 1.5 (Ito)\n"
          f" # dts = {dts}\n"
          f" # ============================================ #\n")

    for i, dt in enumerate(dts):
        q0 = q(dt ** 2)
        q1 = q_000(dt, max_i=ps[i])
        q2 = q_000_12(dt, max_i=ps[i])
        q3 = q_000_13(dt, max_i=ps[i])
        q4 = q_000_23(dt, max_i=ps[i])
        print(f"dt = {dt},\n\n"
              f"\tq = {q0[0]},\tE = {q0[1]}\n\n"

              f"\tq1        = {q1[0]},\tE = {q1[1]}\n"
              f"\tq1 (1, 2) = {q2[0]},\tE = {q2[1]}\n"
              f"\tq1 (2, 3) = {q4[0]},\tE = {q4[1]}\n"
              f"\tq1 (1, 3) = {q3[0]},\tE = {q3[1]}\n\n")


def t1p5exponential():
    dts = [2 ** (-2), 2 ** (-3), 2 ** (-4), 2 ** (-5), 2 ** (-6), 2 ** (-7), 2 ** (-8)]
    ps = [0, 0, 0, 0, 0, 0, 0]

    print(f" # ============================================ #\n"
          f" # EXPONENTIAL TAYLOR 1.5 (Ito)\n"
          f" # dts = {dts}\n"
          f" # ============================================ #\n")

    for i, dt in enumerate(dts):
        q0 = q(dt ** 2)
        q1 = q_000(dt, max_i=ps[i])
        q2 = q_000_12(dt, max_i=ps[i])
        q3 = q_000_13(dt, max_i=ps[i])
        q4 = q_000_23(dt, max_i=ps[i])
        print(f"dt = {dt},\n\n"
              f"\tq = {q0[0]},\tE = {q0[1]}\n\n"

              f"\tq1        = {q1[0]},\tE = {q1[1]}\n"
              f"\tq1 (1, 2) = {q2[0]},\tE = {q2[1]}\n"
              f"\tq1 (2, 3) = {q4[0]},\tE = {q4[1]}\n"
              f"\tq1 (1, 3) = {q3[0]},\tE = {q3[1]}\n\n")


def t1p5fixed():
    dts = [0.011, 0.008, 0.0045, 0.0035, 0.0027, 0.0025]
    ps = [12, 16, 28, 36, 47, 50]

    print(f" # ============================================ #\n"
          f" # FIXED TAYLOR 1.5 (Ito)\n"
          f" # dts = {dts}\n"
          f" # ============================================ #\n")

    for i, dt in enumerate(dts):
        q0 = q(dt ** 2)
        q1 = q_000(dt, max_i=ps[i])
        q2 = q_000_12(dt, max_i=ps[i])
        q3 = q_000_13(dt, max_i=ps[i])
        q4 = q_000_23(dt, max_i=ps[i])
        print(f"dt = {dt},\n\n"
              f"\tq = {q0[0]},\tE = {q0[1]}\n\n"

              f"\tq1        = {q1[0]},\tE = {q1[1]}\n"
              f"\tq1 (1, 2) = {q2[0]},\tE = {q2[1]}\n"
              f"\tq1 (2, 3) = {q4[0]},\tE = {q4[1]}\n"
              f"\tq1 (1, 3) = {q3[0]},\tE = {q3[1]}\n\n")


def t1p5s():
    dts = [0.011, 0.008, 0.0045, 0.0035, 0.0027, 0.0025]
    ps = [0, 0, 0, 0, 0, 0]

    print(f" # ============================================ #\n"
          f" # TAYLOR 1.5 (Stratonovich)\n"
          f" # dts = {dts}\n"
          f" # ============================================ #\n")

    for i, dt in enumerate(dts):
        q0 = q(dt ** 2)
        q1 = q_000(dt, max_i=ps[i])
        q2 = qs_000_12(dt, max_i=ps[i])
        q3 = qs_000_13(dt, max_i=ps[i])
        q4 = qs_000_23(dt, max_i=ps[i])
        print(f"dt = {dt},\n\n"
              f"\tq = {q0[0]},\tE = {q0[1]}\n\n"

              f"\tq1        = {q1[0]},\tE = {q1[1]}\n"
              f"\tq1 (1, 2) = {q2[0]},\tE = {q2[1]}\n"
              f"\tq1 (2, 3) = {q4[0]},\tE = {q4[1]}\n"
              f"\tq1 (1, 3) = {q3[0]},\tE = {q3[1]}\n\n")


def t1p5sexponential():
    dts = [2 ** (-2), 2 ** (-3), 2 ** (-4), 2 ** (-5), 2 ** (-6), 2 ** (-7), 2 ** (-8)]
    ps = [0, 0, 0, 0, 0, 0, 0]

    print(f" # ============================================ #\n"
          f" # EXPONENTIAL TAYLOR 1.5 (Stratonovich)\n"
          f" # dts = {dts}\n"
          f" # ============================================ #\n")

    for i, dt in enumerate(dts):
        q0 = q(dt ** 2)
        q1 = q_000(dt, max_i=ps[i])
        q2 = qs_000_12(dt, max_i=ps[i])
        q3 = qs_000_13(dt, max_i=ps[i])
        q4 = qs_000_23(dt, max_i=ps[i])
        print(f"dt = {dt},\n\n"
              f"\tq = {q0[0]},\tE = {q0[1]}\n\n"

              f"\tq1        = {q1[0]},\tE = {q1[1]}\n"
              f"\tq1 (1, 2) = {q2[0]},\tE = {q2[1]}\n"
              f"\tq1 (2, 3) = {q4[0]},\tE = {q4[1]}\n"
              f"\tq1 (1, 3) = {q3[0]},\tE = {q3[1]}\n\n")


def t1p5sfixed():
    dts = [0.011, 0.008, 0.0045, 0.0035, 0.0027, 0.0025]
    ps = [12, 16, 28, 36, 47, 50]

    print(f" # ============================================ #\n"
          f" # FIXED TAYLOR 1.5 (Stratonovich)\n"
          f" # dts = {dts}\n"
          f" # ============================================ #\n")

    for i, dt in enumerate(dts):
        q0 = q(dt ** 2)
        q1 = q_000(dt, max_i=ps[i])
        q2 = qs_000_12(dt, max_i=ps[i])
        q3 = qs_000_13(dt, max_i=ps[i])
        q4 = qs_000_23(dt, max_i=ps[i])
        print(f"dt = {dt},\n\n"
              f"\tq = {q0[0]},\tE = {q0[1]}\n\n"

              f"\tq1        = {q1[0]},\tE = {q1[1]}\n"
              f"\tq1 (1, 2) = {q2[0]},\tE = {q2[1]}\n"
              f"\tq1 (2, 3) = {q4[0]},\tE = {q4[1]}\n"
              f"\tq1 (1, 3) = {q3[0]},\tE = {q3[1]}\n\n")


def t2p0():
    dts = [2 ** (-1), 2 ** (-2), 2 ** (-3), 2 ** (-4)]

    print(f" # ============================================ #\n"
          f" # TAYLOR 2.0\n"
          f" # dts = [2**(-1), 2**(-2), 2**(-3), 2**(-4)]\n"
          f" # dts = {dts}\n"
          f" # ============================================ #\n")

    for dt in dts:
        print(f"dt = {dt},\n\n"
              f"\tq = {q(dt ** 3)}\n\n"

              f"\tq1        = {q_000(dt ** 2)}\n"
              f"\tq1 (1, 2) = {q_000_12(dt ** 2)}\n"
              f"\tq1 (2, 3) = {q_000_13(dt ** 2)}\n"
              f"\tq1 (1, 3) = {q_000_23(dt ** 2)}\n\n"

              f"\tq2 [01]        = {q_01_12(dt)}\n"
              f"\tq2 [01] (2, 1) = {q_01_21(dt)}\n"
              f"\tq2 [10]        = {q_10_12(dt)}\n"
              f"\tq2 [10] (2, 1) = {q_10_21(dt)}\n\n"

              f"\tq3        = {q_0000(dt)}\n"
              f"\tq3 (1, 2) = {q_0000_12(dt)}\n"
              f"\tq3 (1, 3) = {q_0000_13(dt)}\n"
              f"\tq3 (1, 4) = {q_0000_14(dt)}\n"
              f"\tq3 (2, 3) = {q_0000_23(dt)}\n"
              f"\tq3 (2, 4) = {q_0000_24(dt)}\n"
              f"\tq3 (3, 4) = {q_0000_34(dt)}\n"
              f"\tq3 (1) (2, 3, 4) = {q_0000_1_234(dt)}\n"
              f"\tq3 (2) (1, 3, 4) = {q_0000_2_134(dt)}\n"
              f"\tq3 (4) (1, 2, 3) = {q_0000_4_123(dt)}\n"
              f"\tq3 (3) (1, 2, 4) = {q_0000_3_124(dt)}\n"
              f"\tq3 (1, 2) (3, 4) = {q_0000_12_34(dt)}\n"
              f"\tq3 (1, 3) (2, 4) = {q_0000_13_24(dt)}\n"
              f"\tq3 (1, 4) (2, 3) = {q_0000_14_23(dt)}\n\n")


def t2p5():
    dts = [2 ** (-1), 2 ** (-3 / 2), 2 ** (-2), 2 ** (-5 / 2)]

    print(f" # ============================================ #\n"
          f" # TAYLOR 2.5\n"
          f" # dts = [2**(-1), 2**(-3/2), 2**(-2), 2**(-5/2)]\n"
          f" # dts = {dts}\n"
          f" # ============================================ #\n")

    for dt in dts:
        print(f"dt = {dt},\n\n"
              f"\tq = {q(dt ** 4)}\n\n"

              f"\tq1        = {q_000(dt ** 3)}\n"
              f"\tq1 (1, 2) = {q_000_12(dt ** 3)}\n"
              f"\tq1 (2, 3) = {q_000_13(dt ** 3)}\n"
              f"\tq1 (1, 3) = {q_000_23(dt ** 3)}\n\n"

              f"\tq2 [01]        = {q_01_12(dt ** 2)}\n"
              f"\tq2 [01] (2, 1) = {q_01_21(dt ** 2)}\n"
              f"\tq2 [10]        = {q_10_12(dt ** 2)}\n"
              f"\tq2 [10] (2, 1) = {q_10_21(dt ** 2)}\n\n"

              f"\tq3        = {q_0000(dt ** 2)}\n"
              f"\tq3 (1, 2) = {q_0000_12(dt ** 2)}\n"
              f"\tq3 (1, 3) = {q_0000_13(dt ** 2)}\n"
              f"\tq3 (1, 4) = {q_0000_14(dt ** 2)}\n"
              f"\tq3 (2, 3) = {q_0000_23(dt ** 2)}\n"
              f"\tq3 (2, 4) = {q_0000_24(dt ** 2)}\n"
              f"\tq3 (3, 4) = {q_0000_34(dt ** 2)}\n"
              f"\tq3 (1) (2, 3, 4) = {q_0000_1_234(dt ** 2)}\n"
              f"\tq3 (2) (1, 3, 4) = {q_0000_2_134(dt ** 2)}\n"
              f"\tq3 (4) (1, 2, 3) = {q_0000_4_123(dt ** 2)}\n"
              f"\tq3 (3) (1, 2, 4) = {q_0000_3_124(dt ** 2)}\n"
              f"\tq3 (1, 2) (3, 4) = {q_0000_12_34(dt ** 2)}\n"
              f"\tq3 (1, 3) (2, 4) = {q_0000_13_24(dt ** 2)}\n"
              f"\tq3 (1, 4) (2, 3) = {q_0000_14_23(dt ** 2)}\n\n"

              f"\tq3 [001]           = {q_001(dt)}\n"
              f"\tq3 [001] (1, 2)    = {q_001_12(dt)}\n"
              f"\tq3 [001] (1, 3)    = {q_001_13(dt)}\n"
              f"\tq3 [001] (2, 3)    = {q_001_23(dt)}\n"
              f"\tq3 [001] (1, 2, 3) = {q_001_123(dt)}\n"
              f"\tq3 [010]           = {q_010(dt)}\n"
              f"\tq3 [010] (1, 2)    = {q_010_12(dt)}\n"
              f"\tq3 [010] (1, 3)    = {q_010_13(dt)}\n"
              f"\tq3 [010] (2, 3)    = {q_010_23(dt)}\n"
              f"\tq3 [010] (1, 2, 3) = {q_010_123(dt)}\n"
              f"\tq3 [100]           = {q_100(dt)}\n"
              f"\tq3 [100] (1, 2)    = {q_100_12(dt)}\n"
              f"\tq3 [100] (1, 3)    = {q_100_13(dt)}\n"
              f"\tq3 [100] (2, 3)    = {q_100_23(dt)}\n"
              f"\tq3 [100] (1, 2, 3) = {q_100_123(dt)}\n\n"

              f"\ti      q4        = {q_00000(dt)}\n"
              f"\tiii.1  q4 (1, 2) = {q_00000_15(dt)}\n"
              f"\tiii.2  q4 (1, 3) = {q_00000_13(dt)}\n"
              f"\tiii.3  q4 (1, 4) = {q_00000_14(dt)}\n"
              f"\tiii.4  q4 (1, 5) = {q_00000_15(dt)}\n"
              f"\tiii.5  q4 (2, 3) = {q_00000_23(dt)}\n"
              f"\tiii.6  q4 (2, 4) = {q_00000_24(dt)}\n"
              f"\tiii.7  q4 (2, 5) = {q_00000_25(dt)}\n"
              f"\tiii.8  q4 (3, 4) = {q_00000_34(dt)}\n"
              f"\tiii.9  q4 (3, 5) = {q_00000_35(dt)}\n"
              f"\tiii.10 q4 (4, 5) = {q_00000_45(dt)}\n"
              f"\tiv.1   q4 (3, 4, 5) = {q_00000_345(dt)}\n"
              f"\tiv.2   q4 (2, 4, 5) = {q_00000_245(dt)}\n"
              f"\tiv.3   q4 (2, 3, 5) = {q_00000_235(dt)}\n"
              f"\tiv.4   q4 (2, 3, 4) = {q_00000_234(dt)}\n"
              f"\tiv.5   q4 (1, 4, 5) = {q_00000_145(dt)}\n"
              f"\tiv.6   q4 (1, 3, 5) = {q_00000_135(dt)}\n"
              f"\tiv.7   q4 (1, 3, 4) = {q_00000_134(dt)}\n"
              f"\tiv.8   q4 (1, 2, 5) = {q_00000_125(dt)}\n"
              f"\tiv.9   q4 (1, 2, 4) = {q_00000_124(dt)}\n"
              f"\tiv.10  q4 (1, 2, 3) = {q_00000_123(dt)}\n"
              f"\tv.1    q4 (1) (2, 3, 4, 5) = {q_00000_1_2345(dt)}\n"
              f"\tv.2    q4 (2) (1, 3, 4, 5) = {q_00000_2_1345(dt)}\n"
              f"\tv.3    q4 (3) (1, 2, 4, 5) = {q_00000_3_1245(dt)}\n"
              f"\tv.4    q4 (4) (1, 2, 3, 5) = {q_00000_4_1235(dt)}\n"
              f"\tv.5    q4 (5) (1, 2, 3, 4) = {q_00000_5_1234(dt)}\n"
              f"\tvi.1   q4 (3, 4) (1, 2) = {q_00000_vi_12_34(dt)}\n"
              f"\tvi.2   q4 (2, 4) (1, 3) = {q_00000_vi_13_24(dt)}\n"
              f"\tvi.3   q4 (2, 3) (1, 4) = {q_00000_vi_14_23(dt)}\n"
              f"\tvi.4   q4 (3, 5) (1, 2) = {q_00000_vi_12_35(dt)}\n"
              f"\tvi.5   q4 (2, 3) (1, 5) = {q_00000_vi_15_23(dt)}\n"
              f"\tvi.6   q4 (1, 3) (2, 5) = {q_00000_vi_25_13(dt)}\n"
              f"\tvi.7   q4 (1, 4) (2, 5) = {q_00000_vi_25_14(dt)}\n"
              f"\tvi.8   q4 (4, 5) (1, 2) = {q_00000_vi_12_45(dt)}\n"
              f"\tvi.9   q4 (1, 5) (2, 4) = {q_00000_vi_24_15(dt)}\n"
              f"\tvi.10  q4 (3, 5) (1, 4) = {q_00000_vi_14_35(dt)}\n"
              f"\tvi.11  q4 (4, 5) (1, 3) = {q_00000_vi_13_45(dt)}\n"
              f"\tvi.12  q4 (3, 4) (1, 5) = {q_00000_vi_15_34(dt)}\n"
              f"\tvi.13  q4 (4, 5) (2, 3) = {q_00000_vi_23_45(dt)}\n"
              f"\tvi.14  q4 (3, 5) (2, 4) = {q_00000_vi_24_35(dt)}\n"
              f"\tvi.15  q4 (3, 4) (2, 5) = {q_00000_vi_25_34(dt)}\n"
              f"\tvii.1  q4 (4, 5) (1, 2, 3) = {q_00000_vii_123_45(dt)}\n"
              f"\tvii.2  q4 (3, 5) (1, 2, 4) = {q_00000_vii_124_35(dt)}\n"
              f"\tvii.3  q4 (3, 4) (1, 2, 5) = {q_00000_vii_125_34(dt)}\n"
              f"\tvii.4  q4 (1, 5) (2, 3, 4) = {q_00000_vii_234_15(dt)}\n"
              f"\tvii.5  q4 (1, 4) (2, 3, 5) = {q_00000_vii_235_14(dt)}\n"
              f"\tvii.6  q4 (1, 3) (2, 4, 5) = {q_00000_vii_245_13(dt)}\n"
              f"\tvii.7  q4 (1, 2) (3, 4, 5) = {q_00000_vii_345_12(dt)}\n"
              f"\tvii.8  q4 (2, 4) (1, 3, 5) = {q_00000_vii_135_24(dt)}\n"
              f"\tvii.9  q4 (2, 5) (1, 3, 4) = {q_00000_vii_134_25(dt)}\n"
              f"\tvii.10 q4 (2, 3) (1, 4, 5) = {q_00000_vii_145_23(dt)}\n\n")


def c00000_density(dt):
    print(f"\ti      q4        = {q_00000(dt)}\n"
          f"\tiii.1  q4 (1, 2) = {q_00000_15(dt)}\n"
          f"\tiii.2  q4 (1, 3) = {q_00000_13(dt)}\n"
          f"\tiii.3  q4 (1, 4) = {q_00000_14(dt)}\n"
          f"\tiii.4  q4 (1, 5) = {q_00000_15(dt)}\n"
          f"\tiii.5  q4 (2, 3) = {q_00000_23(dt)}\n"
          f"\tiii.6  q4 (2, 4) = {q_00000_24(dt)}\n"
          f"\tiii.7  q4 (2, 5) = {q_00000_25(dt)}\n"
          f"\tiii.8  q4 (3, 4) = {q_00000_34(dt)}\n"
          f"\tiii.9  q4 (3, 5) = {q_00000_35(dt)}\n"
          f"\tiii.10 q4 (4, 5) = {q_00000_45(dt)}\n"
          f"\tiv.1   q4 (1, 2) (3, 4, 5) = {q_00000_345(dt)}\n"
          f"\tiv.2   q4 (1, 3) (2, 4, 5) = {q_00000_245(dt)}\n"
          f"\tiv.3   q4 (1, 4) (2, 3, 5) = {q_00000_235(dt)}\n"
          f"\tiv.4   q4 (1, 5) (2, 3, 4) = {q_00000_234(dt)}\n"
          f"\tiv.5   q4 (2, 3) (1, 4, 5) = {q_00000_145(dt)}\n"
          f"\tiv.6   q4 (2, 4) (1, 3, 5) = {q_00000_135(dt)}\n"
          f"\tiv.7   q4 (2, 5) (1, 3, 4) = {q_00000_134(dt)}\n"
          f"\tiv.8   q4 (3, 4) (1, 2, 5) = {q_00000_125(dt)}\n"
          f"\tiv.9   q4 (3, 5) (1, 2, 4) = {q_00000_124(dt)}\n"
          f"\tiv.10  q4 (4, 5) (1, 2, 3) = {q_00000_123(dt)}\n"
          f"\tv.1    q4 (1) (2, 3, 4, 5) = {q_00000_1_2345(dt)}\n"
          f"\tv.2    q4 (2) (1, 3, 4, 5) = {q_00000_2_1345(dt)}\n"
          f"\tv.3    q4 (3) (1, 2, 4, 5) = {q_00000_3_1245(dt)}\n"
          f"\tv.4    q4 (4) (1, 2, 3, 5) = {q_00000_4_1235(dt)}\n"
          f"\tv.5    q4 (5) (1, 2, 3, 4) = {q_00000_5_1234(dt)}\n"
          f"\tvi.1   q4 (3, 4) (1, 2) = {q_00000_vi_12_34(dt)}\n"
          f"\tvi.2   q4 (2, 4) (1, 3) = {q_00000_vi_13_24(dt)}\n"
          f"\tvi.3   q4 (2, 3) (1, 4) = {q_00000_vi_14_23(dt)}\n"
          f"\tvi.4   q4 (3, 5) (1, 2) = {q_00000_vi_12_35(dt)}\n"
          f"\tvi.5   q4 (2, 3) (1, 5) = {q_00000_vi_15_23(dt)}\n"
          f"\tvi.6   q4 (1, 3) (2, 5) = {q_00000_vi_25_13(dt)}\n"
          f"\tvi.7   q4 (1, 4) (2, 5) = {q_00000_vi_25_14(dt)}\n"
          f"\tvi.8   q4 (4, 5) (1, 2) = {q_00000_vi_12_45(dt)}\n"
          f"\tvi.9   q4 (1, 5) (2, 4) = {q_00000_vi_24_15(dt)}\n"
          f"\tvi.10  q4 (3, 5) (1, 4) = {q_00000_vi_14_35(dt)}\n"
          f"\tvi.11  q4 (4, 5) (1, 3) = {q_00000_vi_13_45(dt)}\n"
          f"\tvi.12  q4 (3, 4) (1, 5) = {q_00000_vi_15_34(dt)}\n"
          f"\tvi.13  q4 (4, 5) (2, 3) = {q_00000_vi_23_45(dt)}\n"
          f"\tvi.14  q4 (3, 5) (2, 4) = {q_00000_vi_24_35(dt)}\n"
          f"\tvi.15  q4 (3, 4) (2, 5) = {q_00000_vi_25_34(dt)}\n"
          f"\tvii.1  q4 (4, 5) (1, 2, 3) = {q_00000_vii_123_45(dt)}\n"
          f"\tvii.2  q4 (3, 5) (1, 2, 4) = {q_00000_vii_124_35(dt)}\n"
          f"\tvii.3  q4 (3, 4) (1, 2, 5) = {q_00000_vii_125_34(dt)}\n"
          f"\tvii.4  q4 (1, 5) (2, 3, 4) = {q_00000_vii_234_15(dt)}\n"
          f"\tvii.5  q4 (1, 4) (2, 3, 5) = {q_00000_vii_235_14(dt)}\n"
          f"\tvii.6  q4 (1, 3) (2, 4, 5) = {q_00000_vii_245_13(dt)}\n"
          f"\tvii.7  q4 (1, 2) (3, 4, 5) = {q_00000_vii_345_12(dt)}\n"
          f"\tvii.8  q4 (2, 4) (1, 3, 5) = {q_00000_vii_135_24(dt)}\n"
          f"\tvii.9  q4 (2, 5) (1, 3, 4) = {q_00000_vii_134_25(dt)}\n"
          f"\tvii.10 q4 (2, 3) (1, 4, 5) = {q_00000_vii_145_23(dt)}\n\n")


def c0000_density(dt):
    print(f"\tq3        = {q_0000(dt)}\n"
          f"\tq3 (1, 2) = {q_0000_12(dt)}\n"
          f"\tq3 (1, 3) = {q_0000_13(dt)}\n"
          f"\tq3 (1, 4) = {q_0000_14(dt)}\n"
          f"\tq3 (2, 3) = {q_0000_23(dt)}\n"
          f"\tq3 (2, 4) = {q_0000_24(dt)}\n"
          f"\tq3 (3, 4) = {q_0000_34(dt)}\n"
          f"\tq3 (1) (2, 3, 4) = {q_0000_1_234(dt)}\n"
          f"\tq3 (2) (1, 3, 4) = {q_0000_2_134(dt)}\n"
          f"\tq3 (4) (1, 2, 3) = {q_0000_4_123(dt)}\n"
          f"\tq3 (3) (1, 2, 4) = {q_0000_3_124(dt)}\n"
          f"\tq3 (1, 2) (3, 4) = {q_0000_12_34(dt)}\n"
          f"\tq3 (1, 3) (2, 4) = {q_0000_13_24(dt)}\n"
          f"\tq3 (1, 4) (2, 3) = {q_0000_14_23(dt)}\n\n")


def c000_density(dt):
    print(f"\tq1        = {q_000(dt)}\n"
          f"\tq1 (1, 2) = {q_000_12(dt)}\n"
          f"\tq1 (2, 3) = {q_000_13(dt)}\n"
          f"\tq1 (1, 3) = {q_000_23(dt)}\n\n")


def c111_density(dt):
    print(f"\tq3 [001]           = {q_001(dt)}\n"
          f"\tq3 [001] (1, 2)    = {q_001_12(dt)}\n"
          f"\tq3 [001] (1, 3)    = {q_001_13(dt)}\n"
          f"\tq3 [001] (2, 3)    = {q_001_23(dt)}\n"
          f"\tq3 [001] (1, 2, 3) = {q_001_123(dt)}\n"
          f"\tq3 [010]           = {q_10_12(dt)}\n"
          f"\tq3 [010] (1, 2)    = {q_010_12(dt)}\n"
          f"\tq3 [010] (1, 3)    = {q_010_13(dt)}\n"
          f"\tq3 [010] (2, 3)    = {q_010_23(dt)}\n"
          f"\tq3 [010] (1, 2, 3) = {q_010_123(dt)}\n"
          f"\tq3 [100]           = {q_10_12(dt)}\n"
          f"\tq3 [100] (1, 2)    = {q_100_12(dt)}\n"
          f"\tq3 [100] (1, 3)    = {q_100_13(dt)}\n"
          f"\tq3 [100] (2, 3)    = {q_100_23(dt)}\n"
          f"\tq3 [100] (1, 2, 3) = {q_100_123(dt)}\n\n")


def c11_density(dt):
    print(f"\tq2 [01]        = {q_01_12(dt)}\n"
          f"\tq2 [01] (2, 1) = {q_01_21(dt)}\n"
          f"\tq2 [10]        = {q_10_12(dt)}\n"
          f"\tq2 [10] (2, 1) = {q_10_21(dt)}\n\n")


# ============================ #
# Simple q                     #
# ============================ #


def q(dt, max_i=0):
    i = 1
    while True:
        value = 1 / 4 - 1 / 2 * sum([
            1 / (4 * j ** 2 - 1)
            for j in range(1, i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


# ============================ #
# C10 & C01                    #
# ============================ #


def q_01_12(dt, max_i=0, i=0):
    while True:
        value = 1 / 4 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (C((j1, j2), (0, 1), True) ** 2)
            for j1 in range(i + 1)
            for j2 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_01_21(dt, max_i=0, i=0):
    while True:
        value = 1 / 4 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            C((j1, j2), (0, 1), True) * (
                    C((j1, j2), (0, 1), True) +
                    C((j2, j1), (0, 1), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_10_12(dt, max_i=0, i=0):
    while True:
        value = 1 / 12 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (C((j1, j2), (1, 0), True) ** 2)
            for j1 in range(i + 1)
            for j2 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_10_21(dt, max_i=0, i=0):
    while True:
        value = 1 / 12 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            C((j1, j2), (1, 0), True) * (
                    C((j1, j2), (1, 0), True) +
                    C((j2, j1), (1, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


# ============================ #
# C000 group I                 #
# ============================ #


def q_000(dt, max_i=0, i=0):
    while True:
        value = 1 / 6 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            C((j1, j2, j3), (0, 0, 0), True) ** 2
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


# ============================ #
# C000 group III (I)           #
# ============================ #


def q_000_12(dt, max_i=0, i=0):
    while True:
        value = 1 / 6 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (0, 0, 0), True) ** 2 +
             C((j3, j2, j1), (0, 0, 0), True) *
             C((j3, j1, j2), (0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_000_13(dt, max_i=0, i=0):
    while True:
        value = 1 / 6 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (0, 0, 0), True) ** 2 +
             C((j3, j2, j1), (0, 0, 0), True) *
             C((j1, j2, j3), (0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_000_23(dt, max_i=0, i=0):
    while True:
        value = 1 / 6 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (0, 0, 0), True) ** 2 +
             C((j3, j2, j1), (0, 0, 0), True) *
             C((j2, j3, j1), (0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


# ============================ #
# C000 group III (S)           #
# ============================ #


def qs_000_12(dt, max_i=0, i=0):
    while True:
        value = 1 / 4 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (0, 0, 0), True) ** 2 +
             C((j3, j2, j1), (0, 0, 0), True) *
             C((j3, j1, j2), (0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ]) - 1 / 16 * sum([
            (2 * j1 + 1) *
            (C((0, j1, j1), (0, 0, 0), True) +
             C((1, j1, j1), (0, 0, 0), True))
            for j1 in range(i + 1)
        ]) + 1 / 64 * sum([
            (2 * j3 + 1) *
            sum([
                (2 * j1 + 1) * C((j3, j1, j1), (0, 0, 0), True)
                for j1 in range(i + 1)
            ]) ** 2
            for j3 in range(i + 1)
        ])

        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def qs_000_23(dt, max_i=0, i=0):
    while True:
        value = 1 / 4 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (0, 0, 0), True) ** 2 +
             C((j3, j2, j1), (0, 0, 0), True) *
             C((j2, j3, j1), (0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ]) - 1 / 16 * sum([
            (2 * j3 + 1) *
            (C((j3, j3, 0), (0, 0, 0), True) -
             C((j3, j3, 1), (0, 0, 0), True))
            for j3 in range(i + 1)
        ]) + 1 / 64 * sum([
            (2 * j1 + 1) *
            sum([
                (2 * j3 + 1) * C((j3, j3, j1), (0, 0, 0), True)
                for j3 in range(i + 1)
            ]) ** 2
            for j1 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def qs_000_13(dt, max_i=0, i=0):
    while True:
        value = 1 / 6 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (0, 0, 0), True) ** 2 +
             C((j3, j2, j1), (0, 0, 0), True) *
             C((j1, j2, j3), (0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ]) + 1 / 64 * sum([
            (2 * j2 + 1) *
            sum([
                (2 * j1 + 1) * C((j1, j2, j1), (0, 0, 0), True)
                for j1 in range(i + 1)
            ]) ** 2
            for j2 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


# ============================ #
# C100 & C010 & C001           #
# ============================ #


def q_001(dt, max_i=0, i=0):
    while True:
        value = 1 / 10 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            C((j1, j2, j3), (0, 0, 1), True) ** 2
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_001_12(dt, max_i=0, i=0):
    while True:
        value = 1 / 10 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (0, 0, 1), True) ** 2 +
             C((j3, j2, j1), (0, 0, 1), True) *
             C((j3, j1, j2), (0, 0, 1), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_001_13(dt, max_i=0, i=0):
    while True:
        value = 1 / 10 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (0, 0, 1), True) ** 2 +
             C((j3, j2, j1), (0, 0, 1), True) *
             C((j1, j2, j3), (0, 0, 1), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_001_23(dt, max_i=0, i=0):
    while True:
        value = 1 / 10 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (0, 0, 1), True) ** 2 +
             C((j3, j2, j1), (0, 0, 1), True) *
             C((j2, j3, j1), (0, 0, 1), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_001_123(dt, max_i=0, i=0):
    while True:
        value = 1 / 10 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            C((j3, j2, j1), (0, 0, 1), True) * (
                    C((j3, j2, j1), (0, 0, 1), True) +
                    C((j3, j1, j2), (0, 0, 1), True) +
                    C((j2, j3, j1), (0, 0, 1), True) +
                    C((j2, j1, j3), (0, 0, 1), True) +
                    C((j1, j2, j3), (0, 0, 1), True) +
                    C((j1, j3, j2), (0, 0, 1), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_010(dt, max_i=0, i=0):
    while True:
        value = 1 / 20 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            C((j1, j2, j3), (0, 1, 0), True) ** 2
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_010_12(dt, max_i=0, i=0):
    while True:
        value = 1 / 20 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (0, 1, 0), True) ** 2 +
             C((j3, j2, j1), (0, 1, 0), True) *
             C((j3, j1, j2), (0, 1, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_010_13(dt, max_i=0, i=0):
    while True:
        value = 1 / 20 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (0, 1, 0), True) ** 2 +
             C((j3, j2, j1), (0, 1, 0), True) *
             C((j1, j2, j3), (0, 1, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_010_23(dt, max_i=0, i=0):
    while True:
        value = 1 / 20 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (0, 1, 0), True) ** 2 +
             C((j3, j2, j1), (0, 1, 0), True) *
             C((j2, j3, j1), (0, 1, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_010_123(dt, max_i=0, i=0):
    while True:
        value = 1 / 20 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            C((j3, j2, j1), (0, 1, 0), True) * (
                    C((j3, j2, j1), (0, 1, 0), True) +
                    C((j3, j1, j2), (0, 1, 0), True) +
                    C((j2, j3, j1), (0, 1, 0), True) +
                    C((j2, j1, j3), (0, 1, 0), True) +
                    C((j1, j2, j3), (0, 1, 0), True) +
                    C((j1, j3, j2), (0, 1, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_100(dt, max_i=0, i=0):
    while True:
        value = 1 / 60 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            C((j1, j2, j3), (1, 0, 0), True) ** 2
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_100_12(dt, max_i=0, i=0):
    while True:
        value = 1 / 60 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (1, 0, 0), True) ** 2 +
             C((j3, j2, j1), (1, 0, 0), True) *
             C((j3, j1, j2), (1, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_100_13(dt, max_i=0, i=0):
    while True:
        value = 1 / 60 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (1, 0, 0), True) ** 2 +
             C((j3, j2, j1), (1, 0, 0), True) *
             C((j1, j2, j3), (1, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_100_23(dt, max_i=0, i=0):
    while True:
        value = 1 / 60 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (1, 0, 0), True) ** 2 +
             C((j3, j2, j1), (1, 0, 0), True) *
             C((j2, j3, j1), (1, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_100_123(dt, max_i=0, i=0):
    while True:
        value = 1 / 60 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            C((j3, j2, j1), (1, 0, 0), True) * (
                    C((j3, j2, j1), (1, 0, 0), True) +
                    C((j3, j1, j2), (1, 0, 0), True) +
                    C((j2, j3, j1), (1, 0, 0), True) +
                    C((j2, j1, j3), (1, 0, 0), True) +
                    C((j1, j2, j3), (1, 0, 0), True) +
                    C((j1, j3, j2), (1, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


# ============================ #
# C0000 group I                #
# ============================ #


def q_0000(dt, max_i=0, i=0):
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (C((j1, j2, j3, j4), (0, 0, 0, 0), True) ** 2)
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


# ============================ #
# C0000 group III              #
# ============================ #


def q_0000_12(dt, max_i=0, i=0):
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (C((j4, j3, j2, j1), (0, 0, 0, 0), True) ** 2 +
             C((j4, j3, j2, j1), (0, 0, 0, 0), True) *
             C((j4, j3, j1, j2), (0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_0000_13(dt, max_i=0, i=0):
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (C((j4, j3, j2, j1), (0, 0, 0, 0), True) ** 2 +
             C((j4, j3, j2, j1), (0, 0, 0, 0), True) *
             C((j4, j1, j2, j3), (0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_0000_23(dt, max_i=0, i=0):
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (C((j4, j3, j2, j1), (0, 0, 0, 0), True) ** 2 +
             C((j4, j3, j2, j1), (0, 0, 0, 0), True) *
             C((j4, j2, j3, j1), (0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_0000_14(dt, max_i=0, i=0):
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (C((j4, j3, j2, j1), (0, 0, 0, 0), True) ** 2 +
             C((j4, j3, j2, j1), (0, 0, 0, 0), True) *
             C((j1, j3, j2, j4), (0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_0000_24(dt, max_i=0, i=0):
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (C((j4, j3, j2, j1), (0, 0, 0, 0), True) ** 2 +
             C((j4, j3, j2, j1), (0, 0, 0, 0), True) *
             C((j2, j3, j4, j1), (0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_0000_34(dt, max_i=0, i=0):
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (C((j4, j3, j2, j1), (0, 0, 0, 0), True) ** 2 +
             C((j4, j3, j2, j1), (0, 0, 0, 0), True) *
             C((j3, j4, j2, j1), (0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


# ============================ #
# C0000 group IV               #
# ============================ #


def q_0000_4_123(dt, max_i=0, i=0):
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            C((j4, j3, j2, j1), (0, 0, 0, 0), True) * (
                    C((j4, j3, j2, j1), (0, 0, 0, 0), True) +
                    C((j4, j3, j1, j2), (0, 0, 0, 0), True) +
                    C((j4, j2, j3, j1), (0, 0, 0, 0), True) +
                    C((j4, j2, j1, j3), (0, 0, 0, 0), True) +
                    C((j4, j1, j2, j3), (0, 0, 0, 0), True) +
                    C((j4, j1, j3, j2), (0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_0000_3_124(dt, max_i=0, i=0):
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            C((j4, j3, j2, j1), (0, 0, 0, 0), True) * (
                    C((j4, j3, j2, j1), (0, 0, 0, 0), True) +
                    C((j4, j3, j1, j2), (0, 0, 0, 0), True) +
                    C((j2, j3, j4, j1), (0, 0, 0, 0), True) +
                    C((j2, j3, j1, j4), (0, 0, 0, 0), True) +
                    C((j1, j3, j2, j4), (0, 0, 0, 0), True) +
                    C((j1, j3, j4, j2), (0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_0000_2_134(dt, max_i=0, i=0):
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            C((j4, j3, j2, j1), (0, 0, 0, 0), True) * (
                    C((j4, j3, j2, j1), (0, 0, 0, 0), True) +
                    C((j4, j1, j2, j3), (0, 0, 0, 0), True) +
                    C((j3, j4, j2, j1), (0, 0, 0, 0), True) +
                    C((j3, j1, j2, j4), (0, 0, 0, 0), True) +
                    C((j1, j4, j2, j3), (0, 0, 0, 0), True) +
                    C((j1, j3, j2, j4), (0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_0000_1_234(dt, max_i=0, i=0):
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            C((j4, j3, j2, j1), (0, 0, 0, 0), True) * (
                    C((j4, j3, j2, j1), (0, 0, 0, 0), True) +
                    C((j4, j2, j3, j1), (0, 0, 0, 0), True) +
                    C((j3, j4, j2, j1), (0, 0, 0, 0), True) +
                    C((j3, j2, j4, j1), (0, 0, 0, 0), True) +
                    C((j2, j4, j3, j1), (0, 0, 0, 0), True) +
                    C((j2, j3, j4, j1), (0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_0000_12_34(dt, max_i=0, i=0):
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            C((j4, j3, j2, j1), (0, 0, 0, 0), True) * (
                    C((j4, j3, j2, j1), (0, 0, 0, 0), True) +
                    C((j3, j4, j2, j1), (0, 0, 0, 0), True) +
                    C((j4, j3, j1, j2), (0, 0, 0, 0), True) +
                    C((j3, j4, j1, j2), (0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_0000_13_24(dt, max_i=0, i=0):
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            C((j4, j3, j2, j1), (0, 0, 0, 0), True) * (
                    C((j4, j3, j2, j1), (0, 0, 0, 0), True) +
                    C((j2, j3, j4, j1), (0, 0, 0, 0), True) +
                    C((j4, j1, j2, j3), (0, 0, 0, 0), True) +
                    C((j2, j1, j4, j3), (0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_0000_14_23(dt, max_i=0, i=0):
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            C((j4, j3, j2, j1), (0, 0, 0, 0), True) * (
                    C((j4, j3, j2, j1), (0, 0, 0, 0), True) +
                    C((j4, j2, j3, j1), (0, 0, 0, 0), True) +
                    C((j1, j3, j2, j4), (0, 0, 0, 0), True) +
                    C((j1, j2, j3, j4), (0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


# ============================ #
# C00000 group I               #
# ============================ #


def q_00000(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / (32 ** 2) * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            (C((j1, j2, j3, j4, j5), (0, 0, 0, 0, 0), True) ** 2)
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


# ============================ #
# C00000 group III             #
# ============================ #


def q_00000_12(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            (C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) ** 2 +
             C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) *
             C((j5, j4, j3, j1, j2), (0, 0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_13(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            (C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) ** 2 +
             C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) *
             C((j5, j4, j1, j2, j3), (0, 0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_14(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            (C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) ** 2 +
             C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) *
             C((j5, j1, j3, j2, j4), (0, 0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_15(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            (C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) ** 2 +
             C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) *
             C((j1, j4, j3, j2, j5), (0, 0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_23(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            (C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) ** 2 +
             C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) *
             C((j5, j4, j2, j3, j1), (0, 0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_24(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            (C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) ** 2 +
             C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) *
             C((j5, j2, j3, j4, j1), (0, 0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_25(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            (C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) ** 2 +
             C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) *
             C((j2, j4, j3, j5, j1), (0, 0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_34(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            (C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) ** 2 +
             C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) *
             C((j5, j3, j4, j2, j1), (0, 0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_35(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            (C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) ** 2 +
             C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) *
             C((j3, j4, j5, j2, j1), (0, 0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_45(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            (C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) ** 2 +
             C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) *
             C((j4, j5, j3, j2, j1), (0, 0, 0, 0, 0), True))
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


# ============================ #
# C00000 group IV              #
# ============================ #


def q_00000_345(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j3, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j5, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j2, j1), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_245(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j2, j3, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j5, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j5, j1), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_235(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j2, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j5, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j5, j1), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_234(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j2, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j4, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j4, j1), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_145(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j1, j3, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j5, j3, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j2, j5), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_135(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j1, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j5, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j2, j5), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_134(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j1, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j4, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j2, j4), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_125(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j3, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j1, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j5, j2), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j2, j5), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_124(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j3, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j1, j4), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j4, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j2, j4), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_123(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j3, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j1, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j3, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j2, j3), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


# ============================ #
# C00000 group V               #
# ============================ #


def q_00000_1_2345(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j2, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j4, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j3, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j3, j2, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j2, j5, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j2, j3, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j5, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j5, j2, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j2, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j2, j5, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j2, j4, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j5, j4, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j5, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j5, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j3, j5, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j3, j4, j5, j1), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_2_1345(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j1, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j4, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j1, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j4, j3, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j3, j1, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j4, j1, j5, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j4, j1, j3, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j3, j5, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j5, j1, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j1, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j3, j1, j5, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j3, j1, j4, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j5, j4, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j1, j5, j3, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j5, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j3, j5, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j1, j3, j4, j2, j5), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_3_1245(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j3, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j1, j4), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j4, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j4, j2, j3, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j2, j3, j1, j5), (0, 0, 0, 0, 0), True) +
                    C((j4, j1, j3, j5, j2), (0, 0, 0, 0, 0), True) +
                    C((j4, j1, j3, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j2, j5, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j5, j3, j1, j4), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j1, j5), (0, 0, 0, 0, 0), True) +
                    C((j2, j1, j3, j5, j4), (0, 0, 0, 0, 0), True) +
                    C((j2, j1, j3, j4, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j5, j3, j4, j2), (0, 0, 0, 0, 0), True) +
                    C((j1, j5, j3, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j5, j2), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j2, j3, j5, j4), (0, 0, 0, 0, 0), True) +
                    C((j1, j2, j3, j4, j5), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_4_1235(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j3, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j1, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j3, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j2, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j2, j1, j5), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j1, j5, j2), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j1, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j5, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j5, j1, j3), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j1, j5), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j1, j5, j3), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j1, j3, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j5, j3, j2), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j5, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j5, j2), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j2, j5, j3), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j2, j3, j5), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_5_1234(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j3, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j1, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j3, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j2, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j2, j1, j4), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j1, j4, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j1, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j4, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j4, j1, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j1, j4), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j1, j4, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j1, j3, j4), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j4, j3, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j4, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j4, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j2, j4, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j2, j3, j4), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


# ============================ #
# C00000 group VI              #
# ============================ #


def q_00000_vi_12_34(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j3, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j1, j2), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vi_13_24(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j1, j4, j3), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vi_14_23(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j2, j3, j4), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vi_12_35(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j3, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j1, j2), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vi_15_23(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j2, j3, j5), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vi_25_13(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j1, j5, j3), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vi_25_14(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j2, j1, j3, j5, j4), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vi_12_45(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j3, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j1, j2), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vi_24_15(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j2, j3, j4, j5), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vi_14_35(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j1, j5, j2, j4), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vi_13_45(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j1, j2, j3), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vi_15_34(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j1, j3, j4, j2, j5), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vi_23_45(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j2, j3, j1), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vi_24_35(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j2, j5, j4, j1), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vi_25_34(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j3, j4, j5, j1), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


# ============================ #
# C00000 group VII             #
# ============================ #


def q_00000_vii_123_45(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j3, j1, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j1, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j3, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j1, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j2, j1, j3), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j1, j3, j2), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j1, j2, j3), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vii_124_35(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j3, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j1, j4), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j4, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j3, j2, j5, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j2, j5, j1, j4), (0, 0, 0, 0, 0), True) +
                    C((j3, j1, j5, j4, j2), (0, 0, 0, 0, 0), True) +
                    C((j3, j1, j5, j2, j4), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vii_125_34(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j3, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j1, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j5, j2), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j2, j3, j4, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j3, j4, j1, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j3, j4, j5, j2), (0, 0, 0, 0, 0), True) +
                    C((j1, j3, j4, j2, j5), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vii_234_15(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j2, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j4, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j2, j3, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j3, j4, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j3, j2, j4, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j2, j4, j3, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j2, j3, j4, j5), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vii_235_14(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j2, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j5, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j2, j3, j4), (0, 0, 0, 0, 0), True) +
                    C((j3, j1, j5, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j3, j1, j2, j5, j4), (0, 0, 0, 0, 0), True) +
                    C((j2, j1, j5, j3, j4), (0, 0, 0, 0, 0), True) +
                    C((j2, j1, j3, j5, j4), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vii_245_13(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j2, j3, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j5, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j1, j4, j3), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j1, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j4, j2, j1, j5, j3), (0, 0, 0, 0, 0), True) +
                    C((j2, j5, j1, j4, j3), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j1, j5, j3), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vii_345_12(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j3, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j5, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j3, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j4, j3, j5, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j3, j5, j4, j1, j2), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j1, j2), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vii_135_24(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j5, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j4, j1, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j5, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j3, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j2, j1, j4, j3), (0, 0, 0, 0, 0), True) +
                    C((j3, j2, j5, j4, j1), (0, 0, 0, 0, 0), True) +
                    C((j3, j2, j1, j4, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j2, j5, j4, j3), (0, 0, 0, 0, 0), True) +
                    C((j1, j2, j3, j4, j5), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vii_134_25(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j1, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j1, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j4, j2, j3), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j3, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j4, j1, j5, j3), (0, 0, 0, 0, 0), True) +
                    C((j2, j3, j4, j5, j1), (0, 0, 0, 0, 0), True) +
                    C((j2, j3, j1, j5, j4), (0, 0, 0, 0, 0), True) +
                    C((j2, j1, j4, j5, j3), (0, 0, 0, 0, 0), True) +
                    C((j2, j1, j3, j5, j4), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


def q_00000_vii_145_23(dt, max_i=0, i=0):
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) * (
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j3, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j1, j3, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j5, j3, j2, j4), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j3, j2, j5), (0, 0, 0, 0, 0), True) +
                    C((j5, j4, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j1, j2, j3, j4), (0, 0, 0, 0, 0), True) +
                    C((j4, j5, j2, j3, j1), (0, 0, 0, 0, 0), True) +
                    C((j4, j1, j2, j3, j5), (0, 0, 0, 0, 0), True) +
                    C((j1, j5, j2, j3, j4), (0, 0, 0, 0, 0), True) +
                    C((j1, j4, j2, j3, j5), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if max_i == 0 and value <= dt:
            break
        if i >= max_i > 0:
            break
        i += 1
    return i, value


if __name__ == "__main__":
    unittest.main()
