import config as c
import mathematics.sde.nonlinear.c as cs
import tools.database as db
from tools import fsys


def init():
    """
    Initializes database with necessary table schemes
    """
    if not fsys.is_locked('.db.lock'):
        print('Initializing database...')
        create_c_table()
        fsys.lock('.db.lock')


def create_c_table():
    """
    Initializes coefficients table
    """
    db.connect(c.database)

    db.execute("DROP TABLE IF EXISTS `C`")
    db.execute('CREATE TABLE `C` ('
               '    `id`    integer PRIMARY KEY AUTOINCREMENT,'
               '    `index` text,'
               '    `value` text'
               ')')

    pairs = []
    pairs.extend(["('%s', '%s')" % ("%d:%d:%d_%d:%d:%d" %
                                    (i, j, k, 0, 0, 0), cs.getc((i, j, k), (0, 0, 0)))
                  for i in range(7)
                  for j in range(7)
                  for k in range(7)])

    pairs.extend(["('%s', '%s')" % ("%d:%d:%d:%d_%d:%d:%d:%d" %
                                    (i, j, k, m, 0, 0, 0, 0), cs.getc((i, j, k, m), (0, 0, 0, 0)))
                  for i in range(3)
                  for j in range(3)
                  for k in range(3)
                  for m in range(3)])

    pairs.extend(["('%s', '%s')" % ("%d:%d:%d:%d:%d_%d:%d:%d:%d:%d" %
                                    (i, j, k, m, n, 0, 0, 0, 0, 0), cs.getc((i, j, k, m, n), (0, 0, 0, 0, 0)))
                  for i in range(2)
                  for j in range(2)
                  for k in range(2)
                  for m in range(2)
                  for n in range(2)])

    db.execute("INSERT INTO `C` (`index`, `value`) VALUES {}".format(','.join(pairs)))

    db.disconnect()
