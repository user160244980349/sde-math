#!/usr/bin/env python
import config as c
import tools.database as db
from mathematics.sde.nonlinear.symbolic.coefficients.c import C


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
    dts = [2 ** (-1), 2 ** (-3), 2 ** (-5), 2 ** (-8)]

    print(f" # ============================================ #\n"
          f" # TAYLOR 1.5\n"
          f" # dts = [2**(-1), 2**(-3), 2**(-5), 2**(-8)]\n"
          f" # dts = {dts}\n"
          f" # ============================================ #\n")

    for dt in dts:
        print(f"dt = {dt},\n\n"
              f"\tq = {q(dt ** 2)}\n\n"

              f"\tq1        = {q_000(dt)}\n"
              f"\tq1 (1, 2) = {q_000_12(dt)}\n"
              f"\tq1 (1, 3) = {q_000_13(dt)}\n"
              f"\tq1 (2, 3) = {q_000_23(dt)}\n\n")


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
              f"\tq1 (1, 3) = {q_000_13(dt ** 2)}\n"
              f"\tq1 (2, 3) = {q_000_23(dt ** 2)}\n\n"

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
              f"\tq1 (1, 3) = {q_000_13(dt ** 3)}\n"
              f"\tq1 (2, 3) = {q_000_23(dt ** 3)}\n\n"

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
              f"\tiv.1   q4 (1, 2) (3, 4, 5) = {q_00000_12_345(dt)}\n"
              f"\tiv.2   q4 (1, 3) (2, 4, 5) = {q_00000_13_245(dt)}\n"
              f"\tiv.3   q4 (1, 4) (2, 3, 5) = {q_00000_14_235(dt)}\n"
              f"\tiv.4   q4 (1, 5) (2, 3, 4) = {q_00000_15_234(dt)}\n"
              f"\tiv.5   q4 (2, 3) (1, 4, 5) = {q_00000_23_145(dt)}\n"
              f"\tiv.6   q4 (2, 4) (1, 3, 5) = {q_00000_24_135(dt)}\n"
              f"\tiv.7   q4 (2, 5) (1, 3, 4) = {q_00000_25_134(dt)}\n"
              f"\tiv.8   q4 (3, 4) (1, 2, 5) = {q_00000_34_125(dt)}\n"
              f"\tiv.9   q4 (3, 5) (1, 2, 4) = {q_00000_35_124(dt)}\n"
              f"\tiv.10  q4 (4, 5) (1, 2, 3) = {q_00000_45_123(dt)}\n"
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
          f"\tiv.1   q4 (1, 2) (3, 4, 5) = {q_00000_12_345(dt)}\n"
          f"\tiv.2   q4 (1, 3) (2, 4, 5) = {q_00000_13_245(dt)}\n"
          f"\tiv.3   q4 (1, 4) (2, 3, 5) = {q_00000_14_235(dt)}\n"
          f"\tiv.4   q4 (1, 5) (2, 3, 4) = {q_00000_15_234(dt)}\n"
          f"\tiv.5   q4 (2, 3) (1, 4, 5) = {q_00000_23_145(dt)}\n"
          f"\tiv.6   q4 (2, 4) (1, 3, 5) = {q_00000_24_135(dt)}\n"
          f"\tiv.7   q4 (2, 5) (1, 3, 4) = {q_00000_25_134(dt)}\n"
          f"\tiv.8   q4 (3, 4) (1, 2, 5) = {q_00000_34_125(dt)}\n"
          f"\tiv.9   q4 (3, 5) (1, 2, 4) = {q_00000_35_124(dt)}\n"
          f"\tiv.10  q4 (4, 5) (1, 2, 3) = {q_00000_45_123(dt)}\n"
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
          f"\tq1 (1, 3) = {q_000_13(dt)}\n"
          f"\tq1 (2, 3) = {q_000_23(dt)}\n\n")


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


def main():
    db.connect(c.database)

    C.preload(56, 56, 56, 56, 56)

    dts = [0.5, 0.25, 0.1, 0.05, 0.025, 0.005]

    print("\nfor q with C000")
    for dt in dts:
        print(
            f"dt = {dt}, q1(1, 2) = {q_000_12(dt)}, q1(1, 3) = {q_000_13(dt)}, q1(2, 3) = {q_000_23(dt)}, q1 = {q_000(dt)}")

    print("\nfor q with C0000")
    for dt in dts:
        print(
            f"dt = {dt}, q3(1, 2) = {q_0000_12(dt)}, q3(1, 3) = {q_0000_13(dt)}, q3(2, 3) = {q_0000_23(dt)}, q3 = {q_0000(dt)}")

    print("\nfor q with C00000")
    for dt in dts:
        print(
            f"dt = {dt}, q4(1, 2) = {q_00000_12(dt)}, q4(4, 5) = {q_00000_45(dt)}, q4(2, 3) = {q_00000_23(dt)}, q4 = {q_00000(dt)}")

    # m()
    # t1p5()
    t2p0()
    t2p5()


# ============================ #
# Simple q                     #
# ============================ #


def q(dt):
    i = 1
    while True:
        value = 1 / 4 - 1 / 2 * sum([
            1 / (4 * j ** 2 - 1)
            for j in range(1, i + 1)
        ])
        if value <= dt:
            break
        i += 1
    return i


# ============================ #
# C10 & C01                    #
# ============================ #


def q_01_12(dt):
    i = 0
    while True:
        value = 1 / 4 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (C((j1, j2), (0, 1), True) ** 2)
            for j1 in range(i + 1)
            for j2 in range(i + 1)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q_01_21(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_10_12(dt):
    i = 0
    while True:
        value = 1 / 12 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (C((j1, j2), (1, 0), True) ** 2)
            for j1 in range(i + 1)
            for j2 in range(i + 1)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q_10_21(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


# ============================ #
# C000 group I                 #
# ============================ #


def q_000(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


# ============================ #
# C000 group III               #
# ============================ #


def q_000_12(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_000_13(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_000_23(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


# ============================ #
# C100 & C010 & C001           #
# ============================ #


def q_001(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_001_12(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_001_13(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_001_23(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_001_123(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_010(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_010_12(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_010_13(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_010_23(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_010_123(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_100(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_100_12(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_100_13(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_100_23(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_100_123(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


# ============================ #
# C0000 group I                #
# ============================ #


def q_0000(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


# ============================ #
# C0000 group III              #
# ============================ #


def q_0000_12(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_0000_13(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_0000_23(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_0000_14(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_0000_24(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_0000_34(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


# ============================ #
# C0000 group IV               #
# ============================ #


def q_0000_4_123(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_0000_3_124(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_0000_2_134(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_0000_1_234(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_0000_12_34(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_0000_13_24(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_0000_14_23(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


# ============================ #
# C00000 group I               #
# ============================ #


def q_00000(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


# ============================ #
# C00000 group III             #
# ============================ #


def q_00000_12(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_13(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_14(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_15(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_23(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_24(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_25(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_34(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_35(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_45(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


# ============================ #
# C00000 group IV              #
# ============================ #


def q_00000_12_345(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_13_245(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_14_235(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_15_234(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_23_145(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_24_135(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_25_134(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_34_125(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_35_124(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_45_123(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


# ============================ #
# C00000 group V               #
# ============================ #


def q_00000_1_2345(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_2_1345(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_3_1245(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_4_1235(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_5_1234(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


# ============================ #
# C00000 group VI              #
# ============================ #


def q_00000_vi_12_34(dt):
    i = 0
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
                    C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0), True) +
                    C((j5, j3, j4, j1, j2), (0, 0, 0, 0, 0), True)
            )
            for j1 in range(i + 1)
            for j2 in range(i + 1)
            for j3 in range(i + 1)
            for j4 in range(i + 1)
            for j5 in range(i + 1)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vi_13_24(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vi_14_23(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vi_12_35(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vi_15_23(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vi_25_13(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vi_25_14(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vi_12_45(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vi_24_15(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vi_14_35(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vi_13_45(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vi_15_34(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vi_23_45(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vi_24_35(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vi_25_34(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


# ============================ #
# C00000 group VII             #
# ============================ #


def q_00000_vii_123_45(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vii_124_35(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vii_125_34(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vii_234_15(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vii_235_14(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vii_245_13(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vii_345_12(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vii_135_24(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vii_134_25(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


def q_00000_vii_145_23(dt):
    i = 0
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
        if value <= dt:
            break
        i += 1
    return i


if __name__ == "__main__":
    main()
