from config import database as dbname
from init import database
from tools import database as db


def init():
    """
    Initializes various components of application
    """
    db.connect(dbname)
    database.init()
    db.disconnect()
