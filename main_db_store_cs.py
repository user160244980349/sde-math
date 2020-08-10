#!/usr/bin/env python
import config as c
import init.database as idb
import tools.database as db


def main():
    """
    Not actual currently
    Runs database initialization if it is necessary and
    prints all of it contents
    """
    idb.init()
    db.connect(c.database)
    print(db.execute("SELECT * FROM C"))
    db.disconnect()


if __name__ == '__main__':
    main()
