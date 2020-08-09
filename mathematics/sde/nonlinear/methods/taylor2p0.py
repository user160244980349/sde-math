from time import time

import numpy as np
import sympy as sp

import mathematics.sde.nonlinear.functions as f


def taylor2p0(y0: np.array, a: sp.Matrix, b: sp.Matrix,
              q: int, q1: int, q2: int, q3: int, times: tuple):
    """
    Performs modeling with Milstein method with scalar substitutions in cycle
    Parameters
    ----------
        y0 - initial conditions
        mat_a - matrix a
        mat_b - matrix b
        q - amount of independent random variables
        times - modeling interval

    Returns
    -------
        y - solutions matrix
        t - list of time moments
    """
    start_time = time()
    print("--------------------------")
    print("[%.3f seconds] Start Taylor 2.0" % (time() - start_time))

    # Ranges
    n = b.shape[0]
    m = b.shape[1]
    t1 = times[0]
    dt = times[1]
    t2 = times[2]
    f.C.preload(q, q1)

    # Defining context
    args = sp.symbols("x1:%d" % (n + 1))
    ticks = int((t2 - t1) / dt)

    # Symbols
    sym_i = sp.Symbol('i')
    sym_yp = sp.MatrixSymbol('yp', n, 1)
    sym_a = sp.MatrixSymbol('a', n, 1)
    sym_b = sp.MatrixSymbol('b', n, m)
    sym_t = sp.Symbol('t')
    sym_ksi = sp.MatrixSymbol('ksi', q + 1, m)
    y = f.Taylor2p0(sym_i, sym_yp, sym_a, sym_b,
                    q, q1, q2, q3, dt, sym_ksi, args)

    args_extended = list()
    args_extended.extend(args)
    args_extended.extend([sym_t, sym_ksi])

    # Static substitutions
    start_time = time()
    y = y.subs([(sym_yp, sp.Matrix(args)),
                (sym_b, b),
                (sym_a, a)]).doit()

    # Compilation of formulas
    y_compiled = list()
    for tr in range(n):
        y_compiled.append(sp.utilities.lambdify(args_extended, y.subs(sym_i, tr), 'numpy'))

    print("[%.3f seconds] Subs are finished" % (time() - start_time))

    # Substitution values
    t = [t1 + i * dt for i in range(ticks)]
    y = np.zeros((n, ticks))
    y[:, 0] = y0[:, 0]

    # Dynamic substitutions with integration
    for p in range(ticks - 1):
        ksi = np.random.randn(q + 1, m)
        values = list(y[:, p])
        values.extend([t[p], ksi])
        for tr in range(n):
            y[tr, p + 1] = y_compiled[tr](*values)

    print("[%.3f seconds] Calculations are finished" % (time() - start_time))

    return y, t
