#!/usr/bin/env python
import os.path as p

import config as conf
from mathematics.sde.nonlinear.c import get_c


def main():
    """
    Not actual currently
    Saves some of coefficients in text files
    """
    w = {"001": (0, 0, 1),
         "010": (0, 1, 1),
         "100": (1, 0, 0)}

    content = ""
    for c, v in w:
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    content += f"C_{i}{j}{k}({c}) = {get_c((i, j, k), v)}\n"

    file = open(p.join(conf.resources, "c_xxx(xxx).txt"), "w")
    file.write(content)
    file.close()

    content = ""
    for i in range(0, 7):
        for j in range(0, 7):
            for k in range(0, 7):
                content += f"C_{i}{j}{k} = {get_c((i, j, k), (0, 0, 0))}\n"

    file = open(p.join(conf.resources, "c_xxx.txt"), "w")
    file.write(content)
    file.close()

    content = ""
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                for m in range(0, 3):
                    content += f"C_{i}{j}{k}{m} = {get_c((i, j, k, m), (0, 0, 0, 0))}\n"

    file = open(p.join(conf.resources, "c_xxxx.txt"), "w")
    file.write(content)
    file.close()

    content = ""
    for i in range(0, 2):
        for j in range(0, 2):
            for k in range(0, 2):
                for m in range(0, 2):
                    for n in range(0, 2):
                        content += f"C_{i}{j}{k}{m}{n} = {get_c((i, j, k, m, n), (0, 0, 0, 0, 0))}\n"

    file = open(p.join(conf.resources, "c_xxxxx.txt"), "w")
    file.write(content)
    file.close()


if __name__ == "__main__":
    main()
