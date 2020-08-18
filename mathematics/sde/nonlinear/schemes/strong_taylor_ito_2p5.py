from time import time

import numpy as np
import sympy as sp

from mathematics.sde.nonlinear.functions.schemes.strong_taylor_ito_2p5 import StrongTaylorIto2p5


def strong_taylor_ito_2p5(y0: np.array, a: sp.Matrix, b: sp.Matrix,
                          q: int, q1: int, q2: int, q3: int, q4: int, q5: int, times: tuple):
    """
    Performs modeling with Strong Taylor-Ito 2.0 method with matrix substitutions in a loop

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
    q1 : int
        amount of independent random variables
    q2 : int
        amount of independent random variables
    q3 : int
        amount of independent random variables
    q4 : int
        amount of independent random variables
    q5 : int
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
    print(f"[{(time() - start_time):.3f} seconds] Start Strong Taylor-Ito 2.5")

    # Ranges
    n = b.shape[0]
    m = b.shape[1]
    t1 = times[0]
    dt = times[1]
    t2 = times[2]

    # Defining context
    args = sp.symbols("x1:%d" % (n + 1))
    ticks = int((t2 - t1) / dt)

    # Symbols
    sym_i, sym_t = sp.Symbol("i"), sp.Symbol("t")
    sym_ksi = sp.MatrixSymbol("ksi", q + 1, m)
    y = StrongTaylorIto2p5(sym_i, sp.Matrix(args), a, b,
                           q, q1, q2, q3, q4, q5, dt, sym_ksi, args).doit()

    args_extended = list()
    args_extended.extend(args)
    args_extended.extend([sym_t, sym_ksi])

    # Compilation of formulas
    y_compiled = list()
    for tr in range(n):
        y_compiled.append(sp.utilities.lambdify(args_extended, y.subs(sym_i, tr), "numpy"))

    print(f"[{(time() - start_time):.3f} seconds] Subs are finished")

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

    print(f"[{(time() - start_time):.3f} seconds] Calculations are finished")

    return y, t
