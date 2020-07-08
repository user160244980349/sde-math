from numpy import transpose


def in_file(mat_v, tt1, tt2, tt3, tt4, tt5, tt6, key):
    n = tt1
    k = tt2
    m = tt3
    mat_a = mat_v
    mat_b = mat_v

    mat_f = mat_v
    mat_h = mat_v

    mat_ht = transpose(mat_h)
    x0 = mat_v
    
    dt = tt4
    t0 = tt5
    tk = tt6
    
    return n, k, m, mat_a, mat_b, mat_f, mat_ht, x0, dt, t0, tk, key

