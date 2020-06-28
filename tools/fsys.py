import os
import re
import shutil


def ext(path):
    return re.match(r'^.*\.(.*)$', os.path.basename(path)).group(1)


def name(path):
    return re.match(r'^(.*)\..*$', os.path.basename(path)).group(1)


def fullname(path):
    return os.path.basename(path)


def normalized_name(path):
    return re.sub('[ !@#$.,]', '', name(path)).lower()


def directory(path):
    return os.path.dirname(path)


def files(path):
    fs = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        fs.extend([os.path.join(os.path.abspath(dirpath), filename) for filename in filenames])
    return fs


def copy(path, dest):
    return shutil.copyfile(path, dest)


def is_locked(path):
    if os.path.isfile(path):
        return True
    else:
        return False


def lock(path):
    f = open(path, 'w')
    f.close()
