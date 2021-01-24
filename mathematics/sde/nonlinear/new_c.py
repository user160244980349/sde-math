from mathematics.sde.nonlinear.c import get_c


def split_task(tasks):
    c = len(tasks[1])

    if c == 2:
        return split_2(tasks)

    if c == 3:
        return split_3(tasks)

    if c == 4:
        return split_4(tasks)

    if c == 5:
        return split_5(tasks)

    if c == 6:
        return split_6(tasks)


def split_2(ranges):
    return [((i, j), ranges[1])
            for j in range(ranges[0][1][1])
            for i in range(ranges[0][0][1])
            if i >= ranges[0][1][0]
            or j >= ranges[0][0][1]]


def split_3(ranges):
    return [((i, j, k), ranges[1])
            for k in range(ranges[0][2][1])
            for j in range(ranges[0][1][1])
            for i in range(ranges[0][0][1])
            if k >= ranges[0][2][0]
            or j >= ranges[0][1][0]
            or i >= ranges[0][0][0]]


def split_4(ranges):
    return [((i, j, k, l), ranges[1])
            for j in range(*ranges[0][3])
            for i in range(*ranges[0][2])
            for k in range(*ranges[0][1])
            for l in range(*ranges[0][0])
            if l >= ranges[0][3][0]
            or k >= ranges[0][2][0]
            or j >= ranges[0][1][0]
            or i >= ranges[0][0][0]]


def split_5(ranges):
    return [((i, j, k, l, m), ranges[1])
            for j in range(*ranges[0][4])
            for i in range(*ranges[0][3])
            for k in range(*ranges[0][2])
            for l in range(*ranges[0][1])
            for m in range(*ranges[0][0])
            if m >= ranges[0][4][0]
            if l >= ranges[0][3][0]
            or k >= ranges[0][2][0]
            or j >= ranges[0][1][0]
            or i >= ranges[0][0][0]]


def split_6(ranges):
    return [((i, j, k, l, m, n), ranges[1])
            for j in range(*ranges[0][5])
            for i in range(*ranges[0][4])
            for k in range(*ranges[0][3])
            for l in range(*ranges[0][2])
            for m in range(*ranges[0][1])
            for n in range(*ranges[0][0])
            if n >= ranges[0][5][0]
            if m >= ranges[0][4][0]
            if l >= ranges[0][3][0]
            or k >= ranges[0][2][0]
            or j >= ranges[0][1][0]
            or i >= ranges[0][0][0]]


def thread_c(ranges):
    c = len(ranges[1])

    if c == 2:
        return gen_2(*ranges[0], ranges[1])

    if c == 3:
        return gen_3(*ranges[0], ranges[1])

    if c == 4:
        return gen_4(*ranges[0], ranges[1])

    if c == 5:
        return gen_5(*ranges[0], ranges[1])

    if c == 6:
        return gen_6(*ranges[0], ranges[1])


def gen_2(i, j, w):
    return f"\"{i}:{j}_{w[0]}:{w[1]}\";\"{get_c((i, j), w)}\""


def gen_3(i, j, k, w):
    return f"\"{i}:{j}:{k}_{w[0]}:{w[1]}:{w[2]}\";\"{get_c((i, j, k), w)}\""


def gen_4(i, j, k, l, w):
    return f"\"{i}:{j}:{k}:{l}_{w[0]}:{w[1]}:{w[2]}:{w[3]}\";\"{get_c((i, j, k, l), w)}\""


def gen_5(i, j, k, l, m, w):
    return f"\"{i}:{j}:{k}:{l}:{m}_{w[0]}:{w[1]}:{w[2]}:{w[3]}:{w[4]}\";\"{get_c((i, j, k, l, m), w)}\""


def gen_6(i, j, k, l, m, n, w):
    return f"\"{i}:{j}:{k}:{l}:{m}_{w[0]}:{w[1]}:{w[2]}:{w[3]}:{w[4]}:{w[5]}\";\"{get_c((i, j, k, l, m, n), w)}\""
