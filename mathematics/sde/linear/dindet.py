from numpy import ndarray, zeros, eye, hstack, vstack
from scipy.linalg import expm

"""
Algorithm in this module are implementation
from the book named "xxx" in chapter nnn
"""


# algorithm 11.2
def dindet(n: int, k: int, mat_a: ndarray, mat_b: ndarray, dt: float):
    mat_okn = zeros((k, n))
    mat_okk = zeros((k, k))
    mat_idt = eye(n + k) * dt
    mat_aa = vstack((hstack((mat_a, mat_b)), hstack((mat_okn, mat_okk))))
    mat_ex_aah = expm(mat_aa.dot(mat_idt))
    mat_ad = mat_ex_aah[:n, :n]
    mat_bd = mat_ex_aah[:n, n:(n + k)]
    return mat_ad, mat_bd
