from mathematics.sde.nonlinear.functions.coefficients.c import C
from mathematics.sde.nonlinear.functions.coefficients.c000 import C000
from mathematics.sde.nonlinear.functions.coefficients.c0000 import C0000
from mathematics.sde.nonlinear.functions.coefficients.c00000 import C00000
from mathematics.sde.nonlinear.functions.coefficients.c000000 import C000000
from mathematics.sde.nonlinear.functions.coefficients.c0001 import C0001
from mathematics.sde.nonlinear.functions.coefficients.c001 import C001
from mathematics.sde.nonlinear.functions.coefficients.c0010 import C0010
from mathematics.sde.nonlinear.functions.coefficients.c01 import C01
from mathematics.sde.nonlinear.functions.coefficients.c010 import C010
from mathematics.sde.nonlinear.functions.coefficients.c0100 import C0100
from mathematics.sde.nonlinear.functions.coefficients.c02 import C02
from mathematics.sde.nonlinear.functions.coefficients.c10 import C10
from mathematics.sde.nonlinear.functions.coefficients.c100 import C100
from mathematics.sde.nonlinear.functions.coefficients.c1000 import C1000
from mathematics.sde.nonlinear.functions.coefficients.c11 import C11
from mathematics.sde.nonlinear.functions.coefficients.c20 import C20


def solve_q0(dt, eps):
    value = dt ** 2 / 4
    i = 1
    while value > eps:
        value -= dt ** 2 / 2 / (4 * i ** 2 - 1)
        i += 1
    return i


def solve_q1(dt, eps):
    value = dt ** 3
    i = 1
    while value > eps:
        C.preload(0, i)
        value -= 6 * sum([C000(j1, j2, j3, dt) ** 2
                          for j1 in range(i)
                          for j2 in range(i)
                          for j3 in range(i)])
        i += 1
    return i


def solve_q2(dt, eps):
    value = dt ** 4 / 2
    i = 1
    while value > eps:
        C.preload(i)
        value -= 2 * sum([C01(j1, j2, dt) ** 2
                          for j1 in range(i)
                          for j2 in range(i)])
        i += 1
    return i


def solve_q2_optional(dt, eps):
    value = dt ** 4 / 6
    i = 1
    while value > eps:
        C.preload(i)
        value -= 2 * sum([C10(j1, j2, dt) ** 2
                          for j1 in range(i)
                          for j2 in range(i)])
        i += 1
    return i


def solve_q3(dt, eps):
    value = dt ** 4 / 6
    i = 1
    while value > eps:
        C.preload(0, 0, i)
        value -= 4 * sum([C0000(j1, j2, j3, j4, dt) ** 2
                          for j1 in range(i)
                          for j2 in range(i)
                          for j3 in range(i)
                          for j4 in range(i)])
        i += 1
    return i


def solve_q4(dt, eps):
    value = dt ** 5 * 3 / 5
    i = 1
    while value > eps:
        C.preload(0, i)
        value -= 6 * sum([C001(j1, j2, j3, dt) ** 2
                          for j1 in range(i)
                          for j2 in range(i)
                          for j3 in range(i)])
        i += 1
    return i


def solve_q5(dt, eps):
    value = dt ** 5 * 3 / 10
    i = 1
    while value > eps:
        C.preload(0, i)
        value -= 6 * sum([C010(j1, j2, j3, dt) ** 2
                          for j1 in range(i)
                          for j2 in range(i)
                          for j3 in range(i)])
        i += 1
    return i


def solve_q6(dt, eps):
    value = dt ** 5 / 10
    i = 1
    while value > eps:
        C.preload(0, i)
        value -= 6 * sum([C100(j1, j2, j3, dt) ** 2
                          for j1 in range(i)
                          for j2 in range(i)
                          for j3 in range(i)])
        i += 1
    return i


def solve_q7(dt, eps):
    value = dt ** 5
    i = 1
    while value > eps:
        C.preload(0, 0, 0, i)
        value -= 120 * sum([C00000(j1, j2, j3, j4, j5, dt) ** 2
                            for j1 in range(i)
                            for j2 in range(i)
                            for j3 in range(i)
                            for j4 in range(i)
                            for j5 in range(i)])
        i += 1
    return i


def solve_q8(dt, eps):
    value = dt ** 6 / 3
    i = 1
    while value > eps:
        C.preload(i)
        value -= 2 * sum([C02(j1, j2, dt) ** 2
                          for j1 in range(i)
                          for j2 in range(i)])
        i += 1
    return i


def solve_q9(dt, eps):
    value = dt ** 6 / 9
    i = 1
    while value > eps:
        C.preload(i)
        value -= 2 * sum([C11(j1, j2, dt) ** 2
                          for j1 in range(i)
                          for j2 in range(i)])
        i += 1
    return i


def solve_q10(dt, eps):
    value = dt ** 6 / 15
    i = 1
    while value > eps:
        C.preload(i)
        value -= 2 * sum([C20(j1, j2, dt) ** 2
                          for j1 in range(i)
                          for j2 in range(i)])
        i += 1
    return i


def solve_q11(dt, eps):
    value = dt ** 6 * 24 / 30
    i = 1
    while value > eps:
        C.preload(0, 0, i)
        value -= 24 * sum([C0001(j1, j2, j3, j4, dt) ** 2
                           for j1 in range(i)
                           for j2 in range(i)
                           for j3 in range(i)
                           for j4 in range(i)])
        i += 1
    return i


def solve_q12(dt, eps):
    value = dt ** 6 * 24 / 60
    i = 1
    while value > eps:
        C.preload(0, 0, i)
        value -= 24 * sum([C0010(j1, j2, j3, j4, dt) ** 2
                           for j1 in range(i)
                           for j2 in range(i)
                           for j3 in range(i)
                           for j4 in range(i)])
        i += 1
    return i


def solve_q13(dt, eps):
    value = dt ** 6 * 24 / 120
    i = 1
    while value > eps:
        C.preload(0, 0, i)
        value -= 24 * sum([C0100(j1, j2, j3, j4, dt) ** 2
                           for j1 in range(i)
                           for j2 in range(i)
                           for j3 in range(i)
                           for j4 in range(i)])
        i += 1
    return i


def solve_q14(dt, eps):
    value = dt ** 6 / 15
    i = 1
    while value > eps:
        C.preload(0, 0, i)
        value -= 24 * sum([C1000(j1, j2, j3, j4, dt) ** 2
                           for j1 in range(i)
                           for j2 in range(i)
                           for j3 in range(i)
                           for j4 in range(i)])
        i += 1
    return i


def solve_q15(dt, eps):
    value = dt ** 6
    i = 1
    while value > eps:
        C.preload(0, 0, 0, 0, i)
        value -= 720 * sum([C000000(j1, j2, j3, j4, j5, j6, dt) ** 2
                            for j1 in range(i)
                            for j2 in range(i)
                            for j3 in range(i)
                            for j4 in range(i)
                            for j5 in range(i)
                            for j6 in range(i)])
        i += 1
    return i


# This list determines which functions 
# is responsive for which q
# 1. q0  - I00
# 1. q1  - I000
# 1. q2  - I01
# 1. q2  - I10
# 1. q3  - I0000
# 1. q4  - I001
# 1. q5  - I010
# 1. q6  - I100
# 1. q7  - I00000
# 1. q8  - I02
# 1. q9  - I11
# 1. q10 - I20
# 1. q11 - I0001
# 1. q12 - I0010
# 1. q13 - I0100
# 1. q14 - I1000
# 1. q15 - I000000
solvers = [
    solve_q0,
    solve_q1,
    solve_q2,
    solve_q3,
    solve_q4,
    solve_q5,
    solve_q6,
    solve_q7,
    solve_q8,
    solve_q9,
    solve_q10,
    solve_q11,
    solve_q12,
    solve_q13,
    solve_q14,
    solve_q15,
]


def get_q(count: int, dt: float, k: float, r: float):
    """
    Iterates solvers and get q values necessary to
    achieve given precision

    Parameters
    ----------
    qs: tuple
        indices of q necessary to calculate
    dt: float
        integration step
    eps: float
        max error
    Returns
    -------
    qs_result: tuple
        q values
    """
    # qs_result = []
    # for q in range(count):
    #     qs_result.append(solvers[q](dt, k, r))
    C.preload(3, 3, 3, 3, 3, 3)

    return 40, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1,
