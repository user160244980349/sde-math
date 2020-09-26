#!/usr/bin/env python
import config as c
import tools.database as db
from mathematics.sde.nonlinear.functions.coefficients.c import C


def main():
    db.connect(c.database)

    C.preload(55, 55, 55, 55, 55)

    dts = [0.5, 0.25, 0.1, 0.05, 0.025, 0.002]

    print("\nfor q with C000")
    for dt in dts:
        print(f"dt = {dt}, "
              f"q1(1, 2) = {q_000_12(dt)}, "
              f"q1(1, 3) = {q_000_13(dt)}, "
              f"q1(2, 3) = {q_000_23(dt)}, "
              f"q1 = {q1(dt)}")

    print("\nfor q with C0000")
    for dt in dts:
        print(f"dt = {dt}, "
              f"q3(1, 2) = {q_0000_12(dt)}, "
              f"q3(1, 3) = {q_0000_13(dt)}, "
              f"q3(2, 3) = {q_0000_23(dt)}, "
              f"q3(1, 4) = {q_0000_14(dt)}, "
              f"q3 = {q3(dt)}")

    print("\nfor q with C00000")
    for dt in dts:
        print(f"dt = {dt}, "
              f"q4(1, 2) = {q_00000_15(dt)}, "
              f"q4(5, 4) = {q_00000_54(dt)}, "
              f"q4(2, 3) = {q_00000_23(dt)}, "
              f"q4(1, 2) = {q_00000_12(dt)}, "
              f"q4 = {q4(dt)}")


def q_000_12(dt):
    i = 1
    while True:
        value = 1 / 6 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (0, 0, 0)) ** 2 +
             C((j3, j2, j1), (0, 0, 0)) *
             C((j3, j1, j2), (0, 0, 0)))
            for j1 in range(i)
            for j2 in range(i)
            for j3 in range(i)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q_000_13(dt):
    i = 1
    while True:
        value = 1 / 6 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (0, 0, 0)) ** 2 +
             C((j3, j2, j1), (0, 0, 0)) *
             C((j1, j2, j3), (0, 0, 0)))
            for j1 in range(i)
            for j2 in range(i)
            for j3 in range(i)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q_000_23(dt):
    i = 1
    while True:
        value = 1 / 6 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (C((j3, j2, j1), (0, 0, 0)) ** 2 +
             C((j3, j2, j1), (0, 0, 0)) *
             C((j2, j3, j1), (0, 0, 0)))
            for j1 in range(i)
            for j2 in range(i)
            for j3 in range(i)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q1(dt):
    i = 1
    while True:
        value = 1 / 6 - 1 / 64 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            C((j1, j2, j3), (0, 0, 0)) ** 2
            for j1 in range(i)
            for j2 in range(i)
            for j3 in range(i)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q_0000_12(dt):
    i = 1
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (C((j4, j3, j2, j1), (0, 0, 0, 0)) ** 2 +
             C((j4, j3, j2, j1), (0, 0, 0, 0)) *
             C((j4, j3, j1, j2), (0, 0, 0, 0)))
            for j1 in range(i)
            for j2 in range(i)
            for j3 in range(i)
            for j4 in range(i)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q_0000_13(dt):
    i = 1
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (C((j4, j3, j2, j1), (0, 0, 0, 0)) ** 2 +
             C((j4, j3, j2, j1), (0, 0, 0, 0)) *
             C((j4, j1, j2, j3), (0, 0, 0, 0)))
            for j1 in range(i)
            for j2 in range(i)
            for j3 in range(i)
            for j4 in range(i)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q_0000_23(dt):
    i = 1
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (C((j4, j3, j2, j1), (0, 0, 0, 0)) ** 2 +
             C((j4, j3, j2, j1), (0, 0, 0, 0)) *
             C((j4, j2, j3, j1), (0, 0, 0, 0)))
            for j1 in range(i)
            for j2 in range(i)
            for j3 in range(i)
            for j4 in range(i)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q_0000_14(dt):
    i = 1
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (C((j4, j3, j2, j1), (0, 0, 0, 0)) ** 2 +
             C((j4, j3, j2, j1), (0, 0, 0, 0)) *
             C((j1, j3, j2, j4), (0, 0, 0, 0)))
            for j1 in range(i)
            for j2 in range(i)
            for j3 in range(i)
            for j4 in range(i)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q3(dt):
    i = 1
    while True:
        value = 1 / 24 - 1 / 256 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (C((j1, j2, j3, j4), (0, 0, 0, 0)) ** 2)
            for j1 in range(i)
            for j2 in range(i)
            for j3 in range(i)
            for j4 in range(i)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q_00000_15(dt):
    i = 1
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j4 + 1) *
            (C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0)) ** 2 +
             C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0)) *
             C((j1, j4, j3, j2, j5), (0, 0, 0, 0, 0)))
            for j1 in range(i)
            for j2 in range(i)
            for j3 in range(i)
            for j4 in range(i)
            for j5 in range(i)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q_00000_54(dt):
    i = 1
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j4 + 1) *
            (C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0)) ** 2 +
             C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0)) *
             C((j4, j5, j3, j2, j1), (0, 0, 0, 0, 0)))
            for j1 in range(i)
            for j2 in range(i)
            for j3 in range(i)
            for j4 in range(i)
            for j5 in range(i)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q_00000_23(dt):
    i = 1
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j4 + 1) *
            (C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0)) ** 2 +
             C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0)) *
             C((j5, j4, j2, j3, j1), (0, 0, 0, 0, 0)))
            for j1 in range(i)
            for j2 in range(i)
            for j3 in range(i)
            for j4 in range(i)
            for j5 in range(i)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q_00000_12(dt):
    i = 1
    while True:
        value = 1 / 120 - 1 / 32 ** 2 * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j4 + 1) *
            (C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0)) ** 2 +
             C((j5, j4, j3, j2, j1), (0, 0, 0, 0, 0)) *
             C((j5, j4, j3, j1, j2), (0, 0, 0, 0, 0)))
            for j1 in range(i)
            for j2 in range(i)
            for j3 in range(i)
            for j4 in range(i)
            for j5 in range(i)
        ])
        if value <= dt:
            break
        i += 1
    return i


def q4(dt):
    i = 1
    while True:
        value = 1 / 120 - 1 / (32 ** 2) * sum([
            (2 * j1 + 1) *
            (2 * j2 + 1) *
            (2 * j3 + 1) *
            (2 * j4 + 1) *
            (2 * j5 + 1) *
            (C((j1, j2, j3, j4, j5), (0, 0, 0, 0, 0)) ** 2)
            for j1 in range(i)
            for j2 in range(i)
            for j3 in range(i)
            for j4 in range(i)
            for j5 in range(i)
        ])
        if value <= dt:
            break
        i += 1
    return i


if __name__ == "__main__":
    main()
