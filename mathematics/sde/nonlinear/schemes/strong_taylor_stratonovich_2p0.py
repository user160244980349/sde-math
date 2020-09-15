import logging
from time import time

import numpy as np
import sympy as sp

from mathematics.sde.nonlinear.functions.schemes.strong_taylor_stratonovich_2p0 import StrongTaylorStratonovich2p0
from mathematics.sde.nonlinear.q import get_q


def strong_taylor_stratonovich_2p0(y0: np.array, a: sp.Matrix, b: sp.Matrix, k: float, times: tuple):
    """
    Performs modeling with Strong Taylor-Stratonovich 2.0 method with matrix substitutions in a loop

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
    logging.info(f"Schemes: [{(time() - start_time):.3f} seconds] Strong Taylor-Stratonovich 2.0 start")

    # Ranges
    n = b.shape[0]
    m = b.shape[1]
    t1 = times[0]
    dt = times[1]
    t2 = times[2]

    # Defining context
    args = sp.symbols(f"x1:{n + 1}")
    ticks = int((t2 - t1) / dt)
    q = get_q(4, dt, k, 2)

    # Symbols
    sym_i, sym_t = sp.Symbol("i"), sp.Symbol("t")
    sym_ksi = sp.MatrixSymbol("ksi", q[0] + 1, m)
    sym_y = StrongTaylorStratonovich2p0(sym_i, sp.Matrix(args), a, b, dt, sym_ksi, args, q).doit()

    args_extended = list()
    args_extended.extend(args)
    args_extended.extend([sym_t, sym_ksi])

    # Compilation of formulas
    y_compiled = list()
    for tr in range(n):
        y_compiled.append(sp.utilities.lambdify(args_extended, sym_y.subs(sym_i, tr), "numpy"))

    logging.info(f"Schemes: [{(time() - start_time):.3f} seconds] Strong "
                 f"Taylor-Stratonovich 2.0 subs are finished")

    # Substitution values
    t = [t1 + i * dt for i in range(ticks)]
    y = np.zeros((n, ticks))
    y[:, 0] = y0[:, 0]

    # Dynamic substitutions with integration
    for p in range(ticks - 1):
        values = [*y[:, p], t[p], np.random.randn(q[0] + 1, m)]
        for tr in range(n):
            y[tr, p + 1] = y_compiled[tr](*values)

    logging.info(f"Schemes: [{(time() - start_time):.3f} seconds] Strong "
                 f"Taylor-Stratonovich 2.0 calculations are finished")

    return y, t
