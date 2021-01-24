import csv
import logging
import os

import sympy as sp

import config as c
from tools import fsys
from tools.database import execute
from tools.fsys import get_files

logger = logging.getLogger(__name__)


def initdb():
    """
    Initializes database with necessary table drivers
    """

    if not fsys.is_locked(".db.lock"):
        logger.info("Initializing database...")
        create_files_table()
        create_c_table()
        fsys.lock(".db.lock")
    else:
        logger.info("Updating database...")
        update_coefficients()


def create_files_table():
    """
    Initializes coefficients table
    """
    execute("DROP TABLE IF EXISTS `files`")
    execute(
        "CREATE TABLE `files` ("
        "    `id`   integer PRIMARY KEY AUTOINCREMENT,"
        "    `name` text unique"
        ")"
    )


def create_c_table():
    """
    Initializes coefficients table
    """
    execute("DROP TABLE IF EXISTS `C`")
    execute(
        "CREATE TABLE `C` ("
        "    `id`    integer PRIMARY KEY AUTOINCREMENT,"
        "    `index` text unique,"
        "    `value` text,"
        "    `value_f` double"
        ")"
    )

    update_coefficients()


def update_coefficients():
    """
    Updates coefficients table
    """
    files = get_files(c.csv, r'c_.*\.csv')
    loaded_files = [record[0] for record in execute("SELECT `name` FROM `files`")]
    difference = [f for f in files if f not in loaded_files]

    rows = []
    for file in difference:

        with open(os.path.join(file)) as f:
            reader = csv.reader(f, delimiter=';', quotechar='"')
            for row in reader:
                if len(rows) > c.read_buffer_size:
                    execute(f"INSERT INTO `C` (`index`, `value`, `value_f`) VALUES {','.join(rows)}")
                    rows.clear()

                rows.append(f"('{row[0]}', '{row[1]}', {float(sp.sympify(row[1]).evalf())})")

        execute(f"INSERT INTO `files` (`name`) VALUES ('{file}')")

    if len(rows) > 0:
        execute(f"INSERT INTO `C` (`index`, `value`, `value_f`) VALUES {','.join(rows)}")
