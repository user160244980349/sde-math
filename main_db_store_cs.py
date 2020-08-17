#!/usr/bin/env python
import config as c
import tools.database as db
from init.database import init


def main():
    """
    Runs database initialization if it is necessary and
    prints all of it contents
    """
    init()
    db.connect(c.database)
    print(db.execute("SELECT * FROM C"))
    db.disconnect()


if __name__ == "__main__":
    main()
