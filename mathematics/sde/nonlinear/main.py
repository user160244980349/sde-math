from sympy import Matrix, pprint, diff


def main():
    # n = int(input())
    # a = input_matrix(n, 1, ';')
    # b = input_matrix(n, 1, ';')

    n = 3

    a = [['x1**2 * x2**2 * t'],
         ['x2 * x1**2 * 5 * t**3']]

    b = [['sin(x1)', 'cos(x2)', 'cos(2 * x1)'],
         ['x2**2', 't * x1**2', 't * x2**3']]

    mat_a = Matrix(a)
    mat_b = Matrix(b)

    pprint(mat_a * mat_b)

    for s in mat_b.free_symbols:
        for i in range(1):
            for j in range(3):
                print("s: %s, index: %d %d, exp: %s" % (s, i, j, mat_b[i, j]))
                mat_b[i, j] = diff(mat_b[i, j], s)

    pprint(mat_b)


if __name__ == '__main__':
    main()
