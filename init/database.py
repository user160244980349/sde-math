import csv
import os

import config as c
import tools.database as db
from tools import fsys
from tools.fsys import get_files


def init():
    """
    Initializes database with necessary table schemes
    """
    db.connect(c.database)

    if not fsys.is_locked(".db.lock"):
        print("Initializing database...")
        create_files_table()
        create_c_table()
        fsys.lock(".db.lock")
    else:
        update_coefficients()

    db.disconnect()


def create_files_table():
    """
    Initializes coefficients table
    """
    db.execute("DROP TABLE IF EXISTS `files`")
    db.execute(
        "CREATE TABLE `files` ("
        "    `id`    integer PRIMARY KEY AUTOINCREMENT,"
        "    `name` text unique"
        ")"
    )


def create_c_table():
    """
    Initializes coefficients table
    """
    db.execute("DROP TABLE IF EXISTS `C`")
    db.execute(
        "CREATE TABLE `C` ("
        "    `id`    integer PRIMARY KEY AUTOINCREMENT,"
        "    `index` text unique,"
        "    `value` text"
        ")"
    )

    update_coefficients()


def update_coefficients():
    """
    Updates coefficients table
    """
    files = get_files(c.resources, r'c_.*\.csv')
    loaded_files = [record[0] for record in db.execute("SELECT `name` FROM `files`")]
    difference = [f for f in files if f not in loaded_files]

    pairs = []
    for file in difference:

        with open(os.path.join(file)) as f:
            reader = csv.reader(f, delimiter=';', quotechar='"')
            for row in reader:
                if len(pairs) > c.read_buffer_size:
                    db.execute(f"INSERT INTO `C` (`index`, `value`) VALUES {','.join(pairs)}")
                    pairs.clear()

                pairs.append(f"('{row[0]}', '{row[1]}')")

        db.execute(f"INSERT INTO `files` (`name`) VALUES ('{file}')")

    if len(pairs) > 0:
        db.execute(f"INSERT INTO `C` (`index`, `value`) VALUES {','.join(pairs)}")
