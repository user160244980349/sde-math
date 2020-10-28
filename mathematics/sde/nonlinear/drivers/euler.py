import logging
from time import time

import numpy as np
from sympy import lambdify, Matrix, symbols, MatrixSymbol, Symbol

from mathematics.sde.nonlinear.symbolic.schemes.euler import Euler


def euler(y0: np.array, a: Matrix, b: Matrix, times: tuple):
    """
    Performs modeling with Euler method with matrix substitutions in a loop
    Parameters
    ==========
    y0 : numpy.ndarray
        initial conditions
    a : numpy.ndarray
        matrix a
    b : numpy.ndarray
        matrix b
    times : tuple
        integration limits and step
    Returns
    =======
    y : numpy.ndarray
        solutions matrix
    t : list
        list of time moments
    """
    start_time = time()
    logging.info(f"Schemes: [{(time() - start_time):.3f} seconds] Euler start")

    # Ranges
    n = b.shape[0]
    m = b.shape[1]
    t1 = times[0]
    dt = times[1]
    t2 = times[2]

    # Defining context
    args = symbols(f"x1:{n + 1}")
    ticks = int((t2 - t1) / dt)

    # Symbols
    sym_i, sym_t = Symbol("i"), Symbol("t")
    sym_ksi = MatrixSymbol("ksi", 1, m)
    sym_y = Euler(sym_i, Matrix(args), a, b, dt, sym_ksi)

    args_extended = list()
    args_extended.extend(args)
    args_extended.extend([sym_t, sym_ksi])

    # Compilation of formulas
    y_compiled = list()
    for tr in range(n):
        y_compiled.append(lambdify(args_extended, sym_y.subs(sym_i, tr), "numpy"))

    logging.info(f"Schemes: [{(time() - start_time):.3f} seconds] Euler subs are finished")

    # Substitution values
    t = [t1 + i * dt for i in range(ticks)]
    y = np.zeros((n, ticks))
    y[:, 0] = y0[:, 0]

    # Dynamic substitutions with integration
    for p in range(ticks - 1):
        values = [*y[:, p], t[p], np.random.randn(1, m)]
        for tr in range(n):
            y[tr, p + 1] = y_compiled[tr](*values)

    logging.info(f"Schemes: [{(time() - start_time):.3f} seconds] Euler calculations are finished")

    return y, t
