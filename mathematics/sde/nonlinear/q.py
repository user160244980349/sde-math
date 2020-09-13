from mathematics.sde.nonlinear.functions.coefficients.c01 import C01
from mathematics.sde.nonlinear.functions.coefficients.c10 import C10
# from mathematics.sde.nonlinear.functions.coefficients.c20 import C20
# from mathematics.sde.nonlinear.functions.coefficients.c02 import C02
from mathematics.sde.nonlinear.functions.coefficients.c000 import C000
# from mathematics.sde.nonlinear.functions.coefficients.c000 import C001
# from mathematics.sde.nonlinear.functions.coefficients.c000 import C010
# from mathematics.sde.nonlinear.functions.coefficients.c000 import C100
from mathematics.sde.nonlinear.functions.coefficients.c0000 import C0000
# from mathematics.sde.nonlinear.functions.coefficients.c0001 import C0001
# from mathematics.sde.nonlinear.functions.coefficients.c0010 import C0010
# from mathematics.sde.nonlinear.functions.coefficients.c0100 import C0100
# from mathematics.sde.nonlinear.functions.coefficients.c1000 import C1000
from mathematics.sde.nonlinear.functions.coefficients.c00000 import C00000
# from mathematics.sde.nonlinear.functions.coefficients.c000000 import C000000


def solve_q(dt, eps):

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
        value -= 2 * sum([C01(j1, j2, dt) ** 2
                          for j1 in range(i)
                          for j2 in range(i)])
        i += 1

    return i


def solve_q2_optional(dt, eps):

    value = dt ** 4 / 6
    i = 1
    while value > eps:
        value -= 2 * sum([C10(j1, j2, dt) ** 2
                          for j1 in range(i)
                          for j2 in range(i)])
        i += 1

    return i


def solve_q3(dt, eps):

    value = dt ** 4 / 6
    i = 1
    while value > eps:
        value -= 4 * sum([C0000(j1, j2, j3, j4, dt) ** 2
                          for j1 in range(i)
                          for j2 in range(i)
                          for j3 in range(i)
                          for j4 in range(i)])
        i += 1

    return i


def solve_q4(dt, eps):

    value = dt ** 5
    i = 1
    while value > eps:
        value -= 120 * sum([C00000(j1, j2, j3, j4, j5, dt) ** 2
                            for j1 in range(i)
                            for j2 in range(i)
                            for j3 in range(i)
                            for j4 in range(i)
                            for j5 in range(i)])
        i += 1

    return i


# def solve_q5(dt, eps):

#     value = dt ** 6 / 15
#     i = 1
#     while value > eps:
#         value -= 2 * sum([C20(j1, j2, dt) ** 2
#                           for j1 in range(i)
#                           for j2 in range(i)])
#         i += 1

#     return i


# def solve_q6(dt, eps):

#     value = dt ** 6 / 9
#     i = 1
#     while value > eps:
#         value -= 2 * sum([C11(j1, j2, dt) ** 2
#                           for j1 in range(i)
#                           for j2 in range(i)])
#         i += 1

#     return i


# def solve_q7(dt, eps):

#     value = dt ** 6 / 3
#     i = 1
#     while value > eps:
#         value -= 2 * sum([C02(j1, j2, dt) ** 2
#                           for j1 in range(i)
#                           for j2 in range(i)])
#         i += 1

#     return i


# def solve_q8(dt, eps):

#     value = dt ** 5 * 3 / 5
#     i = 1
#     while value > eps:
#         value -= 6 * sum([C001(j1, j2, j3, dt) ** 2
#                           for j1 in range(i)
#                           for j2 in range(i)
#                           for j3 in range(i)])
#         i += 1

#     return i


# def solve_q9(dt, eps):

#     value = dt ** 5 * 3 / 10
#     i = 1
#     while value > eps:
#         value -= 6 * sum([C010(j1, j2, j3, dt) ** 2
#                           for j1 in range(i)
#                           for j2 in range(i)
#                           for j3 in range(i)])
#         i += 1

#     return i


# def solve_q10(dt, eps):

#     value = dt ** 5 / 10
#     i = 1
#     while value > eps:
#         value -= 6 * sum([C100(j1, j2, j3, dt) ** 2
#                           for j1 in range(i)
#                           for j2 in range(i)
#                           for j3 in range(i)])
#         i += 1

#     return i


# def solve_q11(dt, eps):

#     value = dt ** 6 * 2 / 3
#     i = 1
#     while value > eps:
#         value -= 24 * sum([C0001(j1, j2, j3, j4, dt) ** 2
#                            for j1 in range(i)
#                            for j2 in range(i)
#                            for j3 in range(i)
#                            for j4 in range(i)])
#         i += 1

#     return i


# def solve_q12(dt, eps):

#     value = dt ** 6 * 2 / 5
#     i = 1
#     while value > eps:
#         value -= 24 * sum([C0010(j1, j2, j3, j4, dt) ** 2
#                            for j1 in range(i)
#                            for j2 in range(i)
#                            for j3 in range(i)
#                            for j4 in range(i)])
#         i += 1

#     return i


# def solve_q13(dt, eps):

#     value = dt ** 6 / 5
#     i = 1
#     while value > eps:
#         value -= 24 * sum([C0100(j1, j2, j3, j4, dt) ** 2
#                            for j1 in range(i)
#                            for j2 in range(i)
#                            for j3 in range(i)
#                            for j4 in range(i)])
#         i += 1

#     return i


# def solve_q14(dt, eps):

#     value = dt ** 6 / 15
#     i = 1
#     while value > eps:
#         value -= 24 * sum([C1000(j1, j2, j3, j4, dt) ** 2
#                            for j1 in range(i)
#                            for j2 in range(i)
#                            for j3 in range(i)
#                            for j4 in range(i)])
#         i += 1

#     return i


# def solve_q15(dt, eps):

#     value = dt ** 6
#     i = 1
#     while value > eps:
#         value -= 720 * sum([C000000(j1, j2, j3, j4, j5, j6, dt) ** 2
#                             for j1 in range(i)
#                             for j2 in range(i)
#                             for j3 in range(i)
#                             for j4 in range(i)
#                             for j5 in range(i)
#                             for j6 in range(i)])
#         i += 1

#     return i


# This list determines which functions 
# is responsive for which q
solvers = [
    solve_q,
    solve_q1,
    solve_q2,
    # solve_q2_optional,
    solve_q3,
    solve_q4,
    # solve_q5,
    # solve_q6,
    # solve_q7,
    # solve_q8,
    # solve_q9,
    # solve_q10,
    # solve_q11,
    # solve_q12,
    # solve_q13,
    # solve_q14,
    # solve_q15,
]


def get_q(qs: tuple, dt: float, eps: float):
    """
    Inerates solvers and get q values necessary to
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
    qs_result = []
    for q in qs:
        qs_result.append(solvers[q](dt, eps))

    return tuple(qs_result)