import numpy as np

from mathematics.sde.linear.dindet import dindet
from mathematics.sde.linear.matrix import vec_to_eye


def stoch(n: int, m_a: np.ndarray, m_f: np.ndarray, dt: float):
    """
    Root function for set of algorithms implemented below
    
    Parameters
    ----------
    n : int
    m_a : numpy.ndarray
    m_f : numpy.ndarray
    dt : float
    Returns
    -------
    numpy.ndarray
    """
    v_l2, m_s, m_d1 = algorithm_11_2(n, m_a, m_f, dt)
    mat_l = vec_to_eye(np.sqrt(v_l2))
    return m_s.dot(mat_l)


def algorithm_11_2(n: int, m_a: np.ndarray, m_f: np.ndarray, dt: float):
    """ Algorithm 11.2
    Algorithm in this module is implementation
    from the book named "xxx" in chapter nnn
    
    Parameters
    ----------
    n : int
    m_a : numpy.ndarray
    m_f : numpy.ndarray
    dt : float
    Returns
    -------
    eigenvalues : numpy.ndarray
    eigenvectors : numpy.ndarray
    m_d1 : numpy.ndarray
    """
    m_ac = algorithm_11_5(n, m_a)
    m_g = m_f.dot(np.transpose(m_f))
    m_gv = algorithm_11_3(n, m_g)
    m_dd, m_dv = dindet(int(n * (n + 1) / 2), 1, m_ac, m_gv, dt)
    m_d1 = algorithm_11_4(n, m_dv)
    eigenvalues, eigenvectors = np.linalg.eig(m_d1)
    return eigenvalues, eigenvectors, m_d1


def algorithm_11_3(n: int, m_g: np.ndarray):
    """ Algorithm 11.3
    Algorithm in this module is implementation
    from the book named "xxx" in chapter nnn
    
    Parameters
    ----------
    n : int
    m_g : numpy.ndarray
    Returns
    -------
    m_vec : numpy.ndarray
        column vector
    """
    # calculating dimensions sizes
    # these are complicated thoughts
    # about indices just leave as they are
    i2 = 0
    v_size = 0
    for i in range(n):
        n2 = n - i
        for j in range(n2):
            if v_size < j + i2:
                v_size = j + i2
        i2 = i2 + n - i

    m_vec = np.ndarray((v_size + 1, 1))

    # actual algorithm
    i2 = 0
    for i in range(n):
        n2 = n - i
        for j in range(n2):
            m_vec[j + i2][0] = m_g[j][j + i]
        i2 = i2 + n - i

    return m_vec


def algorithm_11_4(n: int, m_dv: np.ndarray):
    """ Algorithm 11.4
    Algorithm in this module is implementation
    from the book named "xxx" in chapter nnn
    
    Parameters
    ----------
    n : int
    m_dv : numpy.ndarray
    Returns
    -------
    m_d1 : numpy.ndarray
    """
    # calculating dimensions sizes
    # these are complicated thoughts
    # about indices just leave as they are
    i2 = 0
    size = 0
    for i in range(n):
        n2 = n - i
        for j in range(n2):
            if size < j + i:
                size = j + i
        i2 = i2 + n - i

    m_d1 = np.ndarray((size + 1, size + 1))

    # actual algorithm
    i2 = 0
    for i in range(n):
        n2 = n - i
        for j in range(n2):
            m_d1[j][j + i] = m_dv[j + i2][0]
            m_d1[j + i][j] = m_dv[j + i2][0]
        i2 = i2 + n - i

    return m_d1


def algorithm_11_5(n: int, m_a: np.ndarray):
    """ Algorithm 11.5
    Algorithm in this module is implementation
    from the book named "xxx" in chapter nnn
    
    Parameters
    ----------
    n : int
    m_a : numpy.ndarray
    Returns
    -------
    m_ac : numpy.ndarray
    """
    # calculating dimensions sizes
    # these are complicated thoughts
    # about indices just leave as they are
    r = 0
    v_size = 0
    h_size = 0

    for i in range(n):
        n2 = n - i
        for j in range(n2):
            o = 0
            for k in range(n):
                n3 = n - k
                for m in range(n3):
                    if v_size < m + o:
                        v_size = m + o
                    if h_size < r:
                        h_size = r
                o = o + n - k
            r = r + 1

    m_ones = np.zeros((n, n))
    m_ac = np.ndarray((v_size + 1, h_size + 1))

    # actual algorithm
    r = 0
    for i in range(n):
        n2 = n - i
        for j in range(n2):
            i2 = j + i
            m_ones[j][i2] = 1
            m_ones[i2][j] = 1
            m_one_a = m_ones.dot(np.transpose(m_a)) + m_a.dot(m_ones)
            o = 0
            for k in range(n):
                n3 = n - k
                for m in range(n3):
                    m_ac[m + o][r] = m_one_a[m][m + k]
                o = o + n - k
            m_ones = np.zeros((n, n))
            r = r + 1

    return m_ac
