from os.path import isfile, join

from config import resources


def is_locked():
    if isfile(join(resources, '.init.lock')):
        return True
    else:
        return False


def lock():
    f = open(join(resources, '.init.lock'), 'w')
    f.close()
