import config as c
import tools.database as db
from mathematics.sde.nonlinear.c import get_c
from tools import fsys


def init():
    """
    Initializes database with necessary table schemes
    """
    if not fsys.is_locked(".db.lock"):
        print("Initializing database...")
        create_c_table()
        fsys.lock(".db.lock")


def create_c_table():
    """
    Initializes coefficients table
    """
    db.connect(c.database)

    db.execute("DROP TABLE IF EXISTS `C`")
    db.execute(
        "CREATE TABLE `C` ("
        "    `id`    integer PRIMARY KEY AUTOINCREMENT,"
        "    `index` text,"
        "    `value` text"
        ")"
    )

    pairs = [f"('{i}:{j}:{k}_0:0:0', '{get_c((i, j, k), (0, 0, 0))}')"
             for i in range(7)
             for j in range(7)
             for k in range(7)]

    pairs.extend([f"('{i}:{j}:{k}:{m}_0:0:0:0', '{get_c((i, j, k, m), (0, 0, 0, 0))}')"
                  for i in range(3)
                  for j in range(3)
                  for k in range(3)
                  for m in range(3)])

    pairs.extend([f"('{i}:{j}:{k}:{m}:{n}_0:0:0:0:0', '{get_c((i, j, k, m, n), (0, 0, 0, 0, 0))}')"
                  for i in range(2)
                  for j in range(2)
                  for k in range(2)
                  for m in range(2)
                  for n in range(2)])

    db.execute(f"INSERT INTO `C` (`index`, `value`) VALUES {','.join(pairs)}")

    db.disconnect()
