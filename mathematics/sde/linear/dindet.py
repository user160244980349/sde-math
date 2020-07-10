from numpy import zeros, eye, hstack, vstack
from scipy.linalg import expm


# algorithm 11.2
def dindet(n, k, mat_a, mat_b, dt):
    mat_okn = zeros((k, n))
    mat_okk = zeros((k, k))
    mat_idt = eye(n + k) * dt
    mat_aa = vstack((hstack((mat_a, mat_b)), hstack((mat_okn, mat_okk))))
    mat_ex_aah = expm(mat_aa.dot(mat_idt))
    mat_ad = mat_ex_aah[:n, :n]
    mat_bd = mat_ex_aah[:n, n:(n + k)]
    return mat_ad, mat_bd
