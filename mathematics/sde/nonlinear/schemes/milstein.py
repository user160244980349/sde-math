from time import time

import numpy as np
import sympy as sp

from mathematics.sde.nonlinear.functions.schemes.milstein import Milstein


def milstein(y0: np.array, a: sp.Matrix, b: sp.Matrix, q: int, times: tuple):
    """
    Performs modeling with Milstein method with matrix substitutions in a loop
    
    Parameters
    ----------
    y0 : numpy.ndarray
        initial conditions
    a : numpy.ndarray
        matrix a
    b : numpy.ndarray
        matrix b
    q : int
        amount of independent random variables
    times : tuple
        integration limits and step
    Returns
    -------
    y : numpy.ndarray
        solutions matrix
    t : list
        list of time moments
    """
    start_time = time()
    print("--------------------------")
    print(f"[{(time() - start_time):.3f} seconds] Start Milstein")

    # Ranges
    n = b.shape[0]
    m = b.shape[1]
    t1 = times[0]
    dt = times[1]
    t2 = times[2]

    # Defining context
    args = sp.symbols(f"x1:{n + 1}")
    ticks = int((t2 - t1) / dt)

    # Symbols
    sym_i, sym_t = sp.Symbol("i"), sp.Symbol("t")
    sym_ksi = sp.MatrixSymbol("ksi", q + 1, m)
    sym_y = Milstein(sym_i, sp.Matrix(args), a, b, q, dt, sym_ksi, args).doit()

    args_extended = list()
    args_extended.extend(args)
    args_extended.extend([sym_t, sym_ksi])

    # Compilation of formulas
    y_compiled = list()
    for tr in range(n):
        y_compiled.append(sp.utilities.lambdify(args_extended, sym_y.subs(sym_i, tr), "numpy"))

    print(f"[{(time() - start_time):.3f} seconds] Subs are finished")

    # Substitution values
    t = [t1 + i * dt for i in range(ticks)]
    y = np.zeros((n, ticks))
    y[:, 0] = y0[:, 0]

    # Dynamic substitutions with integration
    for p in range(ticks - 1):
        values = [*y[:, p], t[p], np.random.randn(q + 1, m)]
        for tr in range(n):
            y[tr, p + 1] = y_compiled[tr](*values)

    print(f"[{(time() - start_time):.3f} seconds] Calculations are finished")

    return y, t
