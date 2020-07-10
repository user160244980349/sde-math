from os.path import join
from sympy import Symbol
from config import resources
from mathematics.symbolic.c import getcw, getc


def main():
    x = Symbol('x')
    
    w = {'001': [1, 1, x + 1],
         '010': [1, x + 1, 1],
         '100': [x + 1, 1, 1]}
    
    content = ''
    
    for c, v in w:
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    content += "C_%d%d%d(%s) = %s\n" % (i, j, k, c, getcw([i, j, k], v))
    
    file = open(join(resources, 'c_xxx(xxx).txt'), 'w')
    file.write(content)
    file.close()
    
    content = ''
    
    for i in range(0, 7):
        for j in range(0, 7):
            for k in range(0, 7):
                content += "C_%d%d%d = %s\n" % (i, j, k, getc([i, j, k]))
    
    file = open(join(resources, 'c_xxx.txt'), 'w')
    file.write(content)
    file.close()
    
    content = ''
    
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                for m in range(0, 3):
                    content += "C_%d%d%d%d = %s\n" % (i, j, k, m, getc([i, j, k, m]))
    
    file = open(join(resources, 'c_xxxx.txt'), 'w')
    file.write(content)
    file.close()
    
    content = ''
    
    for i in range(0, 2):
        for j in range(0, 2):
            for k in range(0, 2):
                for m in range(0, 2):
                    for n in range(0, 2):
                        content += "C_%d%d%d%d%d = %s\n" % (i, j, k, m, n, getc([i, j, k, m, n]))
    
    file = open(join(resources, 'c_xxxxx.txt'), 'w')
    file.write(content)
    file.close()


if __name__ == '__main__':
    main()
