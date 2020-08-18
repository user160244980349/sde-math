import os

import config as c


def is_locked(filename: str):
    """
    Checks if lock is set

    Parameters
    ----------
    filename : str
        name of lock file
    Returns
    -------
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
    ----------
    filename : str
        name of lock file
    """
    f = open(os.path.join(c.resources, filename), "w")
    f.close()
