from tools.input.matrix import matrix
from numpy import transpose, zeros


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
    print(transpose(x0))

    # integration range
    dt = float(input('dt = ? (dt > 0)\n'))
    t0 = float(input('t0 = ?\n'))
    tk = float(input('tk = ? (tk > t0 + dt)\n'))

    while dt <= 0 or t0 > tk - dt:
        dt = float(input('input new dt = ? (dt > 0)\n'))
        t0 = float(input('input new t0 = ?\n'))
        tk = float(input('input new tk = ? (tk > t0 + dt)\n'))

    # type uprav.doc
    keysym = input('key = ? [c,p,h,o,z]\n')
    if keysym == 'c':
        print('U = u0 - k x 1 ')
        print('u0 = ? - k x 1 ')
        mat_u0 = matrix(k, 1, ' ')
        un = 1

    elif keysym == 'p':
        print('U = U(1) + U(2) * t + ... + U(p+1) * t^p - k x 1')
        p = int(input('degree of polynomial p = ?\n'))
        mat_u = zeros((k, p))
        for i in range(p):
            print('i = %d\nU(i) = ? - k x 1 ' % i)
            mat_u[:, i] = matrix(k, 1, ' ')[:, 0]
        un = 2
        print(mat_u)

    elif keysym == 'h':
        print('U = D * sin(w * t + fi) - k x 1\nD = ? - k x 1')
        mat_d = matrix(k, 1, ' ')
        print('w = ? - k x 1')
        mat_w = matrix(k, 1, ' ')
        print('fi = ? - k x 1')
        mat_fi = matrix(k, 1, ' ')
        un = 3
        
   # elif key == 'o'
	# un = 4;
   # elif key == 'z'
   #     for i = 1:k,
	#         type upr.doc;
   #        disp('i = ');
	#   disp(i);
	#   key=input('key = ? [c,p,h]  ','s');
	#      if key == 'c',
	#          u00 = input('u00 = ? ');
   #               ua(i) = 1;
   #                  key = 0;
   #            elif key == 'p'
   #               u01 = input('u01 = ? ');
   #               u02 = input('u02 = ? ');
   #               u03 = input('u03 = ? ');
   #               ua(i) = 2;
   #                  key = 0;
   #            elif key == 'h'
   #               D0 = input('D0 = ? ');
   #               w0 = input('w0 = ? ');
   #               fi0 = input('fi0 = ? ');
   #               ua(i) = 3;
   #                  key = 0;
   #           else
   #            end; %if
   #   	     end; % for
   #   	     un = 5;
   #         else
   #         end; % if key == 'z'


if __name__ == '__main__':
    linito()
