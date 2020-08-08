import numpy as np
import scipy as sci

"""
Algorithm in this module are implementation
from the book named "xxx" in chapter nnn
"""


# algorithm 11.2
def dindet(n: int, k: int, mat_a: np.ndarray, mat_b: np.ndarray, dt: float):
    mat_okn = np.zeros((k, n))
    mat_okk = np.zeros((k, k))
    mat_idt = np.eye(n + k) * dt
    mat_aa = np.vstack((np.hstack((mat_a, mat_b)), np.hstack((mat_okn, mat_okk))))
    mat_ex_aah = sci.linalg.expm(mat_aa.dot(mat_idt))
    mat_ad = mat_ex_aah[:n, :n]
    mat_bd = mat_ex_aah[:n, n:(n + k)]
    return mat_ad, mat_bd
