from mathematics.sde.nonlinear.symbolic.coefficients.c import C


def solve_q(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 4 - 1 / 2 * sum([
        1 / (4 * j ** 2 - 1)
        for j in range(1, i + 1)
    ])


def solve_q1(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 6 - 1 / 64 * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (2 * j3 + 1) *
        C((j1, j2, j3), (0, 0, 0)) ** 2
        for j1 in range(i + 1)
        for j2 in range(i + 1)
        for j3 in range(i + 1)
    ])


def solve_q2(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 4 - 1 / 64 * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (C((j1, j2), (0, 1)) ** 2)
        for j1 in range(i + 1)
        for j2 in range(i + 1)
    ])


def solve_q2_optional(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 12 - 1 / 64 * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (C((j1, j2), (1, 0)) ** 2)
        for j1 in range(i + 1)
        for j2 in range(i + 1)
    ])


def solve_q3(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 24 - 1 / 256 * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (2 * j3 + 1) *
        (2 * j4 + 1) *
        (C((j1, j2, j3, j4), (0, 0, 0, 0)) ** 2)
        for j1 in range(i + 1)
        for j2 in range(i + 1)
        for j3 in range(i + 1)
        for j4 in range(i + 1)
    ])


def solve_q4(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 120 - 1 / (32 ** 2) * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (2 * j3 + 1) *
        (2 * j4 + 1) *
        (2 * j5 + 1) *
        (C((j1, j2, j3, j4, j5), (0, 0, 0, 0, 0)) ** 2)
        for j1 in range(i + 1)
        for j2 in range(i + 1)
        for j3 in range(i + 1)
        for j4 in range(i + 1)
        for j5 in range(i + 1)
    ])


def solve_q5(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 60 - 1 / 256 * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (C((j1, j2), (2, 0)) ** 2)
        for j1 in range(i + 1)
        for j2 in range(i + 1)
    ])


def solve_q6(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 18 - 1 / 256 * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (C((j1, j2), (1, 1)) ** 2)
        for j1 in range(i + 1)
        for j2 in range(i + 1)
    ])


def solve_q7(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 6 - 1 / 256 * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (C((j1, j2), (0, 2)) ** 2)
        for j1 in range(i + 1)
        for j2 in range(i + 1)
    ])


def solve_q8(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 10 - 1 / 256 * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (2 * j3 + 1) *
        (C((j1, j2, j3), (0, 0, 1)) ** 2)
        for j1 in range(i + 1)
        for j2 in range(i + 1)
        for j3 in range(i + 1)
    ])


def solve_q9(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 20 - 1 / 256 * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (2 * j3 + 1) *
        (C((j1, j2, j3), (0, 1, 0)) ** 2)
        for j1 in range(i + 1)
        for j2 in range(i + 1)
        for j3 in range(i + 1)
    ])


def solve_q10(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 60 - 1 / 256 * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (2 * j3 + 1) *
        (C((j1, j2, j3), (1, 0, 0)) ** 2)
        for j1 in range(i + 1)
        for j2 in range(i + 1)
        for j3 in range(i + 1)
    ])


def solve_q11(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 36 - 1 / (32 ** 2) * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (2 * j3 + 1) *
        (2 * j4 + 1) *
        (C((j1, j2, j3, j4), (0, 0, 0, 1)) ** 2)
        for j1 in range(i + 1)
        for j2 in range(i + 1)
        for j3 in range(i + 1)
        for j4 in range(i + 1)
    ])


def solve_q12(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 60 - 1 / (32 ** 2) * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (2 * j3 + 1) *
        (2 * j4 + 1) *
        (C((j1, j2, j3, j4), (0, 0, 1, 0)) ** 2)
        for j1 in range(i + 1)
        for j2 in range(i + 1)
        for j3 in range(i + 1)
        for j4 in range(i + 1)
    ])


def solve_q13(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 120 - 1 / (32 ** 2) * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (2 * j3 + 1) *
        (2 * j4 + 1) *
        (C((j1, j2, j3, j4), (0, 1, 0, 0)) ** 2)
        for j1 in range(i + 1)
        for j2 in range(i + 1)
        for j3 in range(i + 1)
        for j4 in range(i + 1)
    ])


def solve_q14(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 360 - 1 / (32 ** 2) * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (2 * j3 + 1) *
        (2 * j4 + 1) *
        (C((j1, j2, j3, j4), (1, 0, 0, 0)) ** 2)
        for j1 in range(i + 1)
        for j2 in range(i + 1)
        for j3 in range(i + 1)
        for j4 in range(i + 1)
    ])


def solve_q15(i):
    """
    Calculates value for iteration of loop

    Parameters
    ----------
    i : int
        amount of members

    Returns
    -------
    values : float
        value for iteration of loop that calculates amount of q
    """
    return 1 / 720 - 1 / (64 ** 2) * sum([
        (2 * j1 + 1) *
        (2 * j2 + 1) *
        (2 * j3 + 1) *
        (2 * j4 + 1) *
        (2 * j5 + 1) *
        (2 * j6 + 1) *
        (C((j1, j2, j3, j4, j5, j6), (0, 0, 0, 0, 0, 0)) ** 2)
        for j1 in range(i + 1)
        for j2 in range(i + 1)
        for j3 in range(i + 1)
        for j4 in range(i + 1)
        for j5 in range(i + 1)
        for j6 in range(i + 1)
    ])


solvers = [
    solve_q, solve_q1, solve_q2, solve_q3, solve_q8,
    solve_q9, solve_q10, solve_q4, solve_q7, solve_q6,
    solve_q5, solve_q11, solve_q12, solve_q13,
    solve_q14, solve_q15,
]

dt_degrees = [
    [1],
    [2, 1],
    [3, 2, 1, 1],
    [4, 3, 2, 2, 1, 1, 1, 1],
    [5, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
]

q_ranges = [
    1, 2, 4, 8, 16
]


def loop(dt: float, k: float, degree: int, solver):
    """
    Loop that choses amount of q that provides necessary accuracy

    Parameters
    ----------
    dt : float
        delta time
    k : float
        user chosen coefficient of accuracy
    degree : int
        degree of dt depending on q
    solver : function
        function that

    Returns
    -------
    i : int
        amount of q
    """
    i = 0
    while True:
        if solver(i) <= k * dt ** degree:
            break
        i += 1
    return i


def get_q(dt: float, k: float, r: float):
    """
    Iterates solvers and get q values necessary to
    achieve given accuracy

    Parameters
    ----------
    dt: float
        integration step
    k: float
        user chosen coefficient of accuracy
    r: float
        strong numerical scheme order

    Returns
    -------
    qs_result: tuple
        q values
    """
    qs_result = []

    C.preload(50, 50, 50, 50, 50)

    degree = int(r * 2)
    range_id = degree - 2

    for q_id in range(q_ranges[range_id]):
        qs_result.append(loop(dt, k, dt_degrees[range_id][q_id], solvers[q_id]))

    return tuple(qs_result)
