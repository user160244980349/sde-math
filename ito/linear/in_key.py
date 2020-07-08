from tools.input.matrix import matrix, BoundExceedError


def in_key(n, k, m, mat_a, mat_b, mat_f, mat_h, x0, dt, t0, tk):
    n = int(input('n=? (n>=1) '))
    while n < 1:
        n = int(input('<82>¢¥¤¨â¥ ­®¢®¥ n (n>=1) '))

    k = int(input('k=? ((k>=1)&(k<=n)) '))
    while k < 1 or k > n:
        k = int(input('<82>¢¥¤¨â¥ ­®¢®¥ k (k>=1)&(k<=n) '))

    m = int(input('m=? ((m>=1)&(m<=n)) '))
    while m < 1 or m > n:
        m = int(input('<82>¢¥¤¨â¥ ­®¢®¥ m (m>=1)&(m<=n) '))

    try:
        print('A=?(n*n)')
        mat_a = matrix(n, n, ' ')
        print('B=?(n*k)')
        mat_b = matrix(n, k, ' ')
        print('F=?(n*m)')
        mat_f = matrix(n, m, ' ')
        print('H=?(1*n)')
        mat_h = matrix(1, n, ' ')
        print('x0=?(n*1)')
        x0 = matrix(n, 1, ' ')

    except BoundExceedError:
        print('error occurred')

    dt = float(input('dt=? (dt>0) '))
    t0 = float(input('t0=? '))
    tk = float(input('tk=? (tk>t0+dt) '))

    while dt <= 0 or t0 > tk - dt:
        dt = input('<8f>«®å¨¥ ¤ ­­ë¥, ¨§¬¥­¨â¥ dt (dt>0) ')
        t0 = input('t0=? ')
        tk = input('tk=? (tk>t0+dt) ')

    return n, k, m, mat_a, mat_b, mat_f, mat_h, x0, dt, t0, tk
