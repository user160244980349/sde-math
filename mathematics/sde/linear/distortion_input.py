import tools.input as t
from .distortion import *


def zero():
    """
    Pseudo input for zero distortion
    
    Returns
    -------
    Zero
    """
    return Zero()


def const():
    """
    Input for const distortion
    
    Returns
    -------
    Const
    """
    return Const(float(input('const distortion = ?\n')))


def polynomial():
    """
    Input for polynomial distortion
    
    Returns
    -------
    Polynomial
    """
    print('U = U(1) + U(2) * t + ... + U(p+1) * t^p - k x 1\n')
    p = int(input('degree of distortion polynomial p = ?'))
    print('U = ? - 1 x p + 1\n')
    vec_u = t.input_vector(p + 1, ' ').astype(float)
    return Polynomial(vec_u)


def harmonic():
    """
    Input for harmonic distortion
    
    Returns
    -------
    Harmonic
    """
    print('U = D * sin(w * t + fi) - k x 1\nU = [D, w, fi]')
    vec_u = t.input_vector(3, ' ').astype(float)
    return Harmonic(vec_u)
