import os
import re

import config as c


def get_files(path, pattern):
    """
    Gives list of files containing coefficients
    Returns
    =======
    list
        list of available files
    """
    return [os.path.join(path, f)
            for f in os.listdir(path) if re.match(pattern, f)]


def is_locked(filename: str):
    """
    Checks if lock is set
    Parameters
    ==========
    filename : str
        name of lock file
    Returns
    =======
    True of False
    """
    if os.path.isfile(os.path.join(c.resources, filename)):
        return True
    else:
        return False


def lock(filename):
    """
    Performs locking
    Parameters
    ==========
    filename : str
        name of lock file
    """
    f = open(os.path.join(c.resources, filename), "w")
    f.close()


def unlock(filename):
    """
    Performs unlocking
    Parameters
    ==========
    filename : str
        name of lock file
    """
    os.remove(os.path.join(c.resources, filename))
