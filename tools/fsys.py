from os.path import isfile, join

from config import resources


def is_locked(filename):
    if isfile(join(resources, filename)):
        return True
    else:
        return False


def lock(filename):
    f = open(join(resources, filename), 'w')
    f.close()
