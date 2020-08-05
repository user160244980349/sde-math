import config as c
import tools.database as db
from mathematics.sde.nonlinear.c import getc
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
               '    `index` text,'
               '    `value` text'
               ')' % table)

    pairs = []
    pairs.extend(["('%s', '%s')" % (("%d:%d:%d" % (i, j, k)), getc([i, j, k]))
                  for i in range(7)
                  for j in range(7)
                  for k in range(7)])

    pairs.extend(["('%s', '%s')" % (("%d:%d:%d:%d" % (i, j, k, m)), getc([i, j, k, m]))
                  for i in range(3)
                  for j in range(3)
                  for k in range(3)
                  for m in range(3)])

    pairs.extend(["('%s', '%s')" % (("%d:%d:%d:%d:%d" % (i, j, k, m, n)), getc([i, j, k, m, n]))
                  for i in range(2)
                  for j in range(2)
                  for k in range(2)
                  for m in range(2)
                  for n in range(2)])

    db.execute(("INSERT INTO `%s` (`index`, `value`) VALUES {}" % table).format(','.join(pairs)))

    db.disconnect()
