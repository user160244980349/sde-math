import os.path as p

import sympy as sp

import config as conf
import mathematics.sde.nonlinear.c as ct


def main():
    x = sp.Symbol('x')

    w = {'001': [1, 1, x + 1],
         '010': [1, x + 1, 1],
         '100': [x + 1, 1, 1]}

    content = ''

    for c, v in w:
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    content += "C_%d%d%d(%s) = %s\n" % (i, j, k, c, ct.getcw([i, j, k], v))

    file = open(p.join(conf.resources, 'c_xxx(xxx).txt'), 'w')
    file.write(content)
    file.close()

    content = ''

    for i in range(0, 7):
        for j in range(0, 7):
            for k in range(0, 7):
                content += "C_%d%d%d = %s\n" % (i, j, k, ct.getc([i, j, k]))

    file = open(p.join(conf.resources, 'c_xxx.txt'), 'w')
    file.write(content)
    file.close()

    content = ''

    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                for m in range(0, 3):
                    content += "C_%d%d%d%d = %s\n" % (i, j, k, m, ct.getc([i, j, k, m]))

    file = open(p.join(conf.resources, 'c_xxxx.txt'), 'w')
    file.write(content)
    file.close()

    content = ''

    for i in range(0, 2):
        for j in range(0, 2):
            for k in range(0, 2):
                for m in range(0, 2):
                    for n in range(0, 2):
                        content += "C_%d%d%d%d%d = %s\n" % (i, j, k, m, n, ct.getc([i, j, k, m, n]))

    file = open(p.join(conf.resources, 'c_xxxxx.txt'), 'w')
    file.write(content)
    file.close()


if __name__ == '__main__':
    main()
