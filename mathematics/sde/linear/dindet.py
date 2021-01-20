from pprint import pprint

import numpy as np
import scipy.linalg as sci


def dindet(n: int, k: int, m_a: np.ndarray, m_b: np.ndarray, dt: float):
    """ Algorithm 11.2
    Algorithm in this module is implementation
    from the book named "xxx" in chapter nnn
    Parameters
    ==========
    n : int
    k : int
    m_a : numpy.array
    m_b : numpy.array
    dt : float
    Returns
    =======
    m_ad : numpy.array
    m_bd : numpy.array
    """
    m_okn = np.zeros((k, n))
    m_okk = np.zeros((k, k))
    m_idt = np.eye(n + k) * dt
    m_aa = np.vstack((np.hstack((m_a, m_b)),
                      np.hstack((m_okn, m_okk))))
    m_ex_aah = sci.expm(m_aa.dot(m_idt))
    m_ad = m_ex_aah[:n, :n]
    m_bd = m_ex_aah[:n, n:(n + k)]
    return m_ad, m_bd
