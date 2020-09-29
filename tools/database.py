import logging
import re
import sqlite3

connection: sqlite3.Connection
cursor: sqlite3.Cursor


def is_connected():
    """
    Checks if application is connected to database
    
    Returns
    -------
    True or False
    """
    global connection
    if connection is None:
        return False
    else:
        return True


def connect(db: str):
    """
    Connects application to database

    Parameters
    ----------
    db : str
        path to database file
    """
    try:
        global connection
        global cursor

        connection = sqlite3.connect(db)
        connection.create_function("REGEXP", 2, regex)

        cursor = connection.cursor()
        logging.info(f"Database: SQLite Database is successfully connected")

        query = "select sqlite_version();"
        cursor.execute(query)
        record = cursor.fetchall()
        logging.info(f"Database: SQLite Database Version is: {record[0][0]}")

        query = "PRAGMA foreign_keys = ON;"
        cursor.execute(query)

    except sqlite3.Error as error:
        logging.error(f"Database: Error while connecting to sqlite: {error}")


def disconnect():
    """
    Disconnects application from database
    """
    try:
        global connection
        global cursor

        connection.close()
        logging.info("Database: The SQLite connection is closed")

    except sqlite3.Error as error:
        logging.error(f"Database: Error while connecting to sqlite: {error}")


def execute(query: str):
    """
    Sends query to database and receives data
    
    Parameters
    ----------
    query : str
        query to database
    Returns
    -------
        list of tuples (rows)
    """
    try:
        global connection
        global cursor

        cursor.execute(query)
        records = cursor.fetchall()
        connection.commit()
        return records

    except sqlite3.Error as error:
        logging.error(f"Database: Error while connecting to sqlite: {error}")


def regex(value, pattern):
    """
    Regular expression for search in database
    
    Parameters
    ----------
    value 
        column to apply
    pattern
        regular expression
    Returns
    -------
    Search results
    """
    c_pattern = re.compile(r"\b" + pattern.lower() + r"\b")
    return c_pattern.search(value) is not None
