from mathematics.sde.linear.dindet import dindet
from mathematics.sde.linear.stoch import stoch
from mathematics.input import input_matrix
from mathematics.matrix import extending_assignment
from numpy import transpose, zeros, array
from numpy.random import randn
from scipy.linalg import expm
from math import sin


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
    
    n, k, m >= 1
    ''')

    # type title.doc

    # input sizes
    # n = int(input('n = ? (n >= 1)\n'))
    # while n < 1:
    #     n = int(input('input new n = ? (n >= 1)\n'))
    #
    # k = int(input('k = ? (k >= 1)\n'))
    # while k < 1:
    #     k = int(input('input new k = ? (k >= 1)\n'))
    #
    # m = int(input('m = ? (m >= 1)\n'))
    # while m < 1:
    #     m = int(input('input new m = ? (m >= 1)\n'))
    #
    # # input matrices
    # print('A = ? - n x n')
    # mat_a = input_matrix(n, n, ' ')
    #
    # print('B = ? - n x k')
    # mat_b = input_matrix(n, k, ' ')
    #
    # print('F = ? - n x m')
    # mat_f = input_matrix(n, m, ' ')
    #
    # print('H = ? - 1 x n')
    # mat_h = input_matrix(1, n, ' ')
    #
    # print('x0 = ? - n x 1')
    # mat_x0 = input_matrix(n, 1, ' ')
    # print(transpose(mat_x0))
    #
    # # integration range
    # dt = float(input('dt = ? (dt > 0)\n'))
    # t0 = float(input('t0 = ?\n'))
    # tk = float(input('tk = ? (tk > t0 + dt)\n'))
    #
    # while dt <= 0 or t0 > tk - dt:
    #     dt = float(input('input new dt = ? (dt > 0)\n'))
    #     t0 = float(input('input new t0 = ?\n'))
    #     tk = float(input('input new tk = ? (tk > t0 + dt)\n'))

    # type uprav.doc

    n, k, m, dt, t0, tk = 4, 3, 5, 0.001, 0, 10

    mat_d, mat_w, mat_fi, mat_u, mat_ut, mat_u0 = \
        zeros((k, 1)), zeros((k, 1)), zeros((k, 1)), None, None, None
    un, u00, u01, u02, u03, d0, p, w0, fi0, t, tk2 = 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    mat_yt, mat_my, mat_dy, mat_kt, mat_ry, vec_ua = \
        array([[]]), array([[]]), array([[]]), array([[]]), array([[]]), array([])

    mat_a = array([[-1, 0, 0, 0],
                   [0, -2, 0, 0],
                   [0, 0, -1, 0],
                   [0, 0, 0, -3]])

    mat_b = array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])

    mat_f = array([[0.2, 0.1, 0.1, 0.1, 0.1],
                   [0.0, 0.2, 0.1, 0.1, 0.1],
                   [0.1, 0.1, 0.2, 0.1, 0.1],
                   [0.1, 0.1, 0.1, 0.2, 0.1]])

    mat_h = array([[0, 0, 1, 0]])

    mat_x0 = array([[2],
                    [2],
                    [2],
                    [2]])

    # keysym = input('key = ? [c,p,h,o,z]\n')
    keysym = 'o'
    if keysym == 'c':
        print('U = u0 - k x 1')
        print('u0 = ? - k x 1')
        mat_u0 = input_matrix(k, 1, ' ')
        un = 1

    elif keysym == 'p':
        print('U = U(1) + U(2) * t + ... + U(p+1) * t^p - k x 1\n')
        p = int(input('degree of polynomial p = ?\n'))
        mat_u = zeros((k, p))

        for i in range(p):
            print('i = #d\nU(i) = ? - k x 1' % i)
            mat_u[:, i] = input_matrix(k, 1, ' ')[:, 0]

        un = 2
        print(mat_u)

    elif keysym == 'h':
        print('U = D * sin(w * t + fi) - k x 1\nD = ? - k x 1\n')
        mat_d = input_matrix(k, 1, ' ')
        print('w = ? - k x 1\n')
        mat_w = input_matrix(k, 1, ' ')
        print('fi = ? - k x 1\n')
        mat_fi = input_matrix(k, 1, ' ')
        un = 3

    elif keysym == 'o':
        un = 4

    elif keysym == 'z':

        for i in range(k):
            # type upr.doc
            print("i = #d\n" % i)
            keysym = input('key = ? [c,p,h]\n')

            if keysym == 'c':
                u00 = input('u00 = ?\n')
                vec_ua[i] = 1

            elif keysym == 'p':
                u01 = input('u01 = ?\n')
                u02 = input('u02 = ?\n')
                u03 = input('u03 = ?\n')
                vec_ua[i] = 2

            elif keysym == 'h':
                d0 = input('D0 = ?\n')
                w0 = input('w0 = ?\n')
                fi0 = input('fi0 = ?\n')
                vec_ua[i] = 3

            else:
                un = 5

    print('''
    CALCULATION OF MATRICES OF DYNAMICAL 
    PART OF SOLUTION - Ad AND DETERMINISTIC 
    PART OF SOLUTION - Bd (ALGORITHM 11.2)
    ''')

    mat_ad, mat_bd = dindet(n, k, mat_a, mat_b, dt)

    # ans = input('see Ad and Bd? [y/n]\n')
    ans = 'n'
    if ans == 'y':
        print('Ab =')
        print(mat_ad)
        print('Bb =')
        print(mat_bd)

    print('''
    CALCULATION OF MATRIX OF STOCHASTIC
    PART OF SOLUTION - Fd (ALGORITHM 11.6)	
    ''')

    mat_fd = stoch(n, mat_a, mat_f, dt)

    # ans = input('see Fd? [y/n]\n')
    ans = 'n'
    if ans == 'y':
        print('Fd = ')
        print(mat_fd)
        # type press.doc

    t1 = t0
    tk1 = tk
    x1 = mat_x0

    # ans = input('continue? [y/n]\n')
    ans = 'y'
    if ans == 'y':
        t0 = t1
        tk = tk1
        mat_x0 = x1
        mat_mx0 = mat_x0
        mat_dx0 = zeros((n, n))

        # ans = input('modelling? [y/n]\n')
        ans = 'y'
        while ans == 'y':
            kk = 0
            mat_yt = extending_assignment(mat_yt, 0, kk, mat_h.dot(mat_x0))
            mat_my = extending_assignment(mat_my, 0, kk, mat_h.dot(mat_mx0))
            mat_dy = extending_assignment(mat_dy, 0, kk, mat_h.dot(mat_dx0).dot(transpose(mat_h)))
            mat_kt = extending_assignment(mat_kt, 0, kk, t0)
            tk2, t2 = tk, tk - t0
            nn = int(t2 / dt + 1)

            for kk in range(nn):
                t = t0 + (kk - 1) * dt

                # calculating of control
                # constant control
                if un == 1:
                    mat_ut = mat_u0

                # polynomial control
                elif un == 2:
                    mat_ut = zeros((k, 1))

                    for i in range(p):
                        mat_ut = mat_ut + mat_u[:, i] * t ** (i - 1)

                # harmonic control
                elif un == 3:
                    mat_ut = zeros((k, 1))

                    for i in range(k):
                        mat_ut[i][0] = mat_ut[i][0] + mat_d[i][0] * sin(mat_w[i][0] * t + mat_fi[i][0])

                # zero control
                elif un == 4:
                    mat_ut = zeros((k, 1))

                # combine control
                elif un == 5:

                    for j in range(k):
                        if vec_ua[j] == 1:
                            mat_ut[j][0] = u00

                        elif vec_ua[j] == 2:
                            mat_ut[j][0] = u01 + u02 * t + u03 * t**2

                        elif vec_ua[j] == 3:
                            mat_ut[j][0] = d0 * sin(w0 * t + fi0)

                # modelling of solution of sde
                ft = randn(n, 1)

                # solution of sde
                xt = mat_ad.dot(mat_x0) + mat_bd.dot(mat_ut) + mat_fd.dot(ft)

                # expectation of solution of sde
                mx = mat_ad.dot(mat_mx0) + mat_bd.dot(mat_ut)

                # dispersion of solution of sde
                mat_dx = mat_ad.dot(mat_dx0).dot(transpose(mat_ad)) + mat_fd.dot(transpose(mat_fd))

                # covariance matrix of solution of sde
                rx = expm(mat_a * (tk - t)).dot(mat_dx)

                # exit process of stochastic system
                mat_yt = extending_assignment(mat_yt, 0, kk, mat_h.dot(xt))

                # expectation of exit process
                mat_my = extending_assignment(mat_my, 0, kk, mat_h.dot(mx))

                # dispersion of exit process
                mat_dy = extending_assignment(mat_dy, 0, kk, mat_h.dot(mat_dx).dot(transpose(mat_h)))

                # covariance matrix of exit process
                mat_ry = extending_assignment(mat_ry, 0, kk, mat_h.dot(rx).dot(transpose(mat_h)))
                mat_kt = extending_assignment(mat_kt, 0, kk, t)
                mat_x0, mat_mx0, mat_dx0 = xt, mx, mat_dx
                t0, tk = tk2, tk2 + t2
                
                print('\n Xt = ')
                print(xt)

                # plot(kt,yt,'b',kt,my,'r'),
                # ylabel('blue - SDE, red - ODE'),
                # xlabel('time'),
                # type press.doc
                # pause
                # plot(kt,Dy,'b'),
                # ylabel('dispertion of Y'),
                # xlabel('time'),
                # type press.doc
                # pause

            ans = input('modelling on next interval? [y/n]\n')


if __name__ == '__main__':
    linito()
