import config as c
from init.database import init as init_db_if_not
from tools import database as db


def main():
    init_db_if_not()
    db.connect(c.database)
    print(db.execute("SELECT * FROM C"))
    db.disconnect()


if __name__ == '__main__':
    main()
