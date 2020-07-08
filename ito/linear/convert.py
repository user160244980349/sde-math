from numpy import zeros, transpose


def convert(mat_a, n):
    mat_a_conv = zeros(n, n)
    mat_one_1 = zeros(n, n)
    rr1 = 1
    for jj1 in range(1, n):
        nb1 = n - jj1 + 1
        for kk1 in range(1, nb1):
            ii1 = kk1 + jj1 - 1
            mat_one_1[kk1, ii1] = 1
            mat_one_1[ii1, kk1] = 1
            mat_one_a = mat_one_1 * transpose(mat_a) + mat_a * mat_one_1
            oo1 = 0
            for ss1 in range(1, n):
                ll11 = n-ss1+1
                for ll1 in range(1, ll11):
                    mat_a_conv[ll1+oo1, rr1] = mat_one_a[ll1, ll1 + ss1 - 1]
                oo1 = oo1 + n - ss1 + 1
            mat_one_1 = zeros(n, n)
            rr1 = rr1 + 1
    return mat_a_conv
