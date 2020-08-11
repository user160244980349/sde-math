from time import time

import numpy as np
import sympy as sp

from ..functions.coefficients.C import C
from ..functions.schemes.StrongTaylorStratonovich1p5 import StrongTaylorStratonovich1p5


def strong_taylor_stratonovich_1p5(y0: np.array, a: sp.Matrix, b: sp.Matrix,
                                   q: int, q1: int, times: tuple):
    """
    Performs modeling with Strong Taylor-Stratonovich 1.5 method with matrix substitutions in a loop

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
    print("[%.3f seconds] Start Strong Taylor-Stratonovich 1.5" % (time() - start_time))

    # Ranges
    n = b.shape[0]
    m = b.shape[1]
    t1 = times[0]
    dt = times[1]
    t2 = times[2]
    C.preload(q1)

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
    y = StrongTaylorStratonovich1p5(sym_i, sym_yp, sym_a, sym_b,
                                    q, q1, dt, sym_ksi, args)

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
