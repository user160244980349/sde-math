import config as c
import mathematics.sde.nonlinear.c as cs
import tools.database as db
from tools import fsys


def init():
    if not fsys.is_locked('.db.lock'):
        print('Initializing database...')
        create_c_table('C')
        fsys.lock('.db.lock')


def create_c_table(table):
    db.connect(c.database)

    db.execute("DROP TABLE IF EXISTS `%s`" % table)
    db.execute('CREATE TABLE `%s` ('
               '    `id`    integer PRIMARY KEY AUTOINCREMENT,'
               '    `dimensions` int,'
               '    `index` text,'
               '    `value` text'
               ')' % table)

    pairs = []
    pairs.extend(["(%d, '%s', '%s')" % (3, ("%d:%d:%d" % (i, j, k)), cs.getc([i, j, k]))
                  for i in range(7)
                  for j in range(7)
                  for k in range(7)])

    pairs.extend(["(%d, '%s', '%s')" % (4, ("%d:%d:%d:%d" % (i, j, k, m)), cs.getc([i, j, k, m]))
                  for i in range(3)
                  for j in range(3)
                  for k in range(3)
                  for m in range(3)])

    pairs.extend(["(%d, '%s', '%s')" % (5, ("%d:%d:%d:%d:%d" % (i, j, k, m, n)), cs.getc([i, j, k, m, n]))
                  for i in range(2)
                  for j in range(2)
                  for k in range(2)
                  for m in range(2)
                  for n in range(2)])

    db.execute(("INSERT INTO `%s` (`dimensions`, `index`, `value`) VALUES {}" % table).format(','.join(pairs)))

    db.disconnect()
