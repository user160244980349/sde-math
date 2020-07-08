from tools.input.matrix import matrix


def linito():
    print('''
    NUMERICAL SOLUTION OF LINEAR
    STATIONARY SYSTEM OF STOCHASTIC
    DIFFERENTIAL EQUATIONS
    
    dx = AX dt + BU dt + F df, X(0) = X0
    Y = HX
    X - size n x 1, Y - size 1 x 1, U - size k x 1
    f - size m x 1, A - size n x n, B - size n x k
    F - size n x m, H - size 1 x n    
    ''')

    # title
    # type title.doc
    
    # input sizes
    n = int(input('n = ? (n >= 1)\n'))
    while n < 1:
        n = int(input('input new n = ? (n >= 1)\n'))

    k = int(input('k = ? (k >= 1)\n'))
    while k < 1:
        k = int(input('input new k = ? (k >= 1)\n'))

    m = int(input('m = ? (m >= 1)\n'))
    while m < 1:
        m = int(input('input new m = ? (m >= 1)\n'))

    # input matrices
    print('A = ? - n x n')
    mat_a = matrix(n, n, ' ')

    print('B = ? - n x k')
    mat_b = matrix(n, k, ' ')

    print('F = ? - n x m')
    mat_f = matrix(n, m, ' ')

    print('H = ? - 1 x n')
    mat_h = matrix(1, n, ' ')

    print('x0 = ? - n x 1')
    x0 = matrix(n, 1, ' ')

    # integration range
    dt = float(input('dt = ? (dt > 0)\n'))
    t0 = float(input('t0 = ?\n'))
    tk = float(input('tk = ? (tk > t0 + dt)\n'))

    while dt <= 0 or t0 > tk - dt:
        dt = float(input('input new dt = ? (dt > 0)\n'))
        t0 = float(input('input new t0 = ?\n'))
        tk = float(input('input new tk = ? (tk > t0 + dt)\n'))

    # type uprav.doc


if __name__ == '__main__':
    linito()
