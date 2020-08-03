from sympy import Matrix, Function, Sum, symbols, Symbol, MatrixSymbol

from mathematics.sde.nonlinear.functions.G import G
from mathematics.sde.nonlinear.functions.Io import Io
from mathematics.sde.nonlinear.functions.Ioo import Ioo


class Milstein(Function):
    nargs = 0

    @classmethod
    def context(cls, i, n, m, q, diff_args):
        cls.i = i
        cls.m = m
        cls.n = n
        cls.q = q
        cls.t = Symbol('t')
        cls.dt = Symbol('dt')
        cls.a = MatrixSymbol('a', n, 1)
        cls.b = MatrixSymbol('b', n, m)
        cls.yp = MatrixSymbol('yp', n, 1)
        cls.ksi = MatrixSymbol('ksi', q, m)
        cls.diff_args = diff_args

    @classmethod
    def eval(cls):
        i1, i2 = symbols('i1 i2')
        return cls.yp[cls.i, 0] + cls.a[cls.i, 0] * cls.dt + \
               Sum(cls.b[cls.i, i1] * Io(i1, cls.dt, cls.ksi), (i1, 0, cls.m - 1)) + \
               Sum(Sum(G(Matrix(cls.b[:, i1]), cls.b[cls.i, i2], cls.diff_args) * \
                       Ioo(i1, i2, cls.q, cls.dt, cls.ksi), (i2, 0, cls.m - 1)), (i1, 0, cls.m - 1))
