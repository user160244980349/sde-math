from time import time

import numpy as np
import sympy as sp

import mathematics.sde.nonlinear.functions as f


def euler(y0: np.array, a: sp.Matrix, b: sp.Matrix, times: tuple):
    """
    Performs modeling with Euler method with matrix substitutions in cycle
    Parameters
    ----------
        y0 - initial conditions
        mat_a - matrix a
        mat_b - matrix b
        times - modeling interval

    Returns
    -------
        y - solutions matrix
        t - list of time moments
    """
    start_time = time()
    print("--------------------------")
    print("[%.3f seconds] Start Euler" % (time() - start_time))

    # Ranges
    n = b.shape[0]
    m = b.shape[1]
    t1 = times[0]
    dt = times[1]
    t2 = times[2]

    # Defining context
    ticks = int((t2 - t1) / dt)

    # Symbols
    sym_i = sp.Symbol('i')
    sym_t = sp.Symbol('t')
    sym_ksi = sp.MatrixSymbol('ksi', 1, m)

    args = sp.symbols("x1:%d" % (n + 1))
    args_extended = list()
    args_extended.extend(args)
    args_extended.extend([sym_t, sym_ksi])

    # Static substitutions
    y = f.Euler(sym_i, sp.Matrix(args), a, b, dt, sym_ksi).doit()

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
        ksi = np.random.randn(1, m)
        values = list(y[:, p])
        values.extend([t[p], ksi])
        for tr in range(n):
            y[tr, p + 1] = y_compiled[tr](*values)

    print("[%.3f seconds] Calculations are finished" % (time() - start_time))

    return y, t
