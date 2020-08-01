from time import time

from numpy import array, zeros
from plotly import graph_objects

from mathematics.sde.linear.distortion_input import zero, harmonic, polynomial, const
from mathematics.sde.linear.dindet import dindet
from mathematics.sde.linear.distortion import Distortion
from mathematics.sde.linear.integration import Integral
from mathematics.sde.linear.stoch import stoch


def main():
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
    # mat_a = input_matrix(n, n, ' ').astype(float)
    #
    # print('B = ? - n x k')
    # mat_b = input_matrix(n, k, ' ').astype(float)
    #
    # print('F = ? - n x m')
    # mat_f = input_matrix(n, m, ' ').astype(float)
    #
    # print('H = ? - 1 x n')
    # mat_h = input_matrix(1, n, ' ').astype(float)
    #
    # print('x0 = ? - n x 1')
    # mat_x0 = input_matrix(n, 1, ' ').astype(float)
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

    integral = Integral(4)

    integral.k, integral.m, integral.dt, integral.t0, integral.tk = \
        3, 5, 0.001, 0, 10

    integral.mat_a = array([[-1, 0, 0, 0],
                            [0, -2, 0, 0],
                            [0, 0, -1, 0],
                            [0, 0, 0, -3]])

    integral.mat_b = array([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])

    integral.mat_f = array([[0.2, 0.1, 0.1, 0.1, 0.1],
                            [0.1, 0.2, 0.1, 0.1, 0.1],
                            [0.1, 0.1, 0.2, 0.1, 0.1],
                            [0.1, 0.1, 0.1, 0.2, 0.1]])

    integral.mat_h = array([[0, 0, 1, 0]])

    integral.mat_x0 = array([[2],
                             [2],
                             [2],
                             [2]])

    integral.mat_mx0 = array([[2],
                              [2],
                              [2],
                              [2]])

    integral.mat_dx0 = zeros((integral.n, integral.n))

    print('''
    CALCULATION OF MATRICES OF DYNAMICAL 
    PART OF SOLUTION - Ad AND DETERMINISTIC 
    PART OF SOLUTION - Bd (ALGORITHM 11.2)
    ''')

    integral.mat_ad, integral.mat_bd = dindet(integral.n, integral.k, integral.mat_a, integral.mat_b, integral.dt)

    print('Ab =')
    print(integral.mat_ad)
    print('Bb =')
    print(integral.mat_bd)

    print('''
    CALCULATION OF MATRIX OF STOCHASTIC
    PART OF SOLUTION - Fd (ALGORITHM 11.6)	
    ''')

    integral.mat_fd = stoch(integral.n, integral.mat_a, integral.mat_f, integral.dt)

    print('Fd = ')
    print(integral.mat_fd)

    mat_u = array([[object]] * integral.k)
    for i in range(integral.k):
        keysym = input('\nkey = ? [c,p,h,o]\n')
        if keysym == 'c':
            mat_u[i][0] = const()

        elif keysym == 'p':
            mat_u[i][0] = polynomial()

        elif keysym == 'h':
            mat_u[i][0] = harmonic()

        elif keysym == 'o':
            mat_u[i][0] = zero()

    integral.distortion = Distortion(integral.k, mat_u)

    print('\nwhich trajectories do you want to be shown?')
    trajectories = array(input().strip().split(' ')).astype(int)
    print('\ncalculating...')

    while True:
        t1 = int(round(time() * 1000))
        integral.integrate()
        t2 = int(round(time() * 1000))
        print("integration took %d" % (t2 - t1))

        # create traces
        fig1 = graph_objects.Figure()
        fig2 = graph_objects.Figure()
        for i in trajectories:
            fig1.add_trace(graph_objects.Scatter(x=integral.vec_t, y=integral.mat_xt[i],
                                                 mode='lines',
                                                 name="component %d" % i))
            fig1.add_trace(graph_objects.Scatter(x=integral.vec_t, y=integral.mat_mx[i],
                                                 mode='lines',
                                                 name="expectation of component %d" % i))
            fig2.add_trace(graph_objects.Scatter(x=integral.vec_t, y=integral.mat_dx[i],
                                                 mode='lines',
                                                 name="dispersion of component %d" % 0))
        fig1.show()
        fig2.show()

        integral.tk = integral.tk * 2

        if input('\nnext?\n') != 'y':
            break


if __name__ == '__main__':
    main()
