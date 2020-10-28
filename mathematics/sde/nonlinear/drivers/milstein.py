import logging
from time import time

import numpy as np
from sympy import symbols, MatrixSymbol, Matrix, lambdify

from mathematics.sde.nonlinear.q import get_q
from mathematics.sde.nonlinear.symbolic.schemes.milstein import Milstein


def milstein(y0: np.array, a: Matrix, b: Matrix, k: float, times: tuple):
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
    q : tuple
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
    logging.info(f"Schemes: [{(time() - start_time):.3f} seconds] Milstein start")

    # Ranges
    n = b.shape[0]
    m = b.shape[1]
    t1 = times[0]
    dt = times[1]
    t2 = times[2]

    # Defining context
    args = symbols(f"x1:{n + 1}")
    ticks = int((t2 - t1) / dt)
    q = get_q(dt, k, 1)
    logging.info(f"Schemes: [{(time() - start_time):.3f} seconds] Using C = {k}")
    logging.info(f"Schemes: [{(time() - start_time):.3f} seconds] Using dt = {dt}")
    logging.info(f"Schemes: [{(time() - start_time):.3f} seconds] Using q = {q}")

    # Symbols
    sym_i, sym_t = symbols("i t")
    sym_ksi = MatrixSymbol("ksi", q[0] + 2, m)
    sym_y = Milstein(sym_i, Matrix(args), a, b, dt, sym_ksi, args, q)

    args_extended = list()
    args_extended.extend(args)
    args_extended.extend([sym_t, sym_ksi])

    # Compilation of formulas
    y_compiled = list()
    for tr in range(n):
        y_compiled.append(lambdify(args_extended, sym_y.subs(sym_i, tr), "numpy"))

    logging.info(f"Schemes: [{(time() - start_time):.3f} seconds] Milstein subs are finished")

    # Substitution values
    t = [t1 + i * dt for i in range(ticks)]
    y = np.zeros((n, ticks))
    y[:, 0] = y0[:, 0]

    # Dynamic substitutions with integration
    for p in range(ticks - 1):
        values = [*y[:, p], t[p], np.random.randn(q[0] + 2, m)]
        for tr in range(n):
            y[tr, p + 1] = y_compiled[tr](*values)

    logging.info(f"Schemes: [{(time() - start_time):.3f} seconds] Milstein calculations are finished")

    return y, t
