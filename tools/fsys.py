from os.path import isfile, join

import config as c


def is_locked(filename):
    if isfile(join(c.resources, filename)):
        return True
    else:
        return False


def lock(filename):
    f = open(join(c.resources, filename), 'w')
    f.close()
