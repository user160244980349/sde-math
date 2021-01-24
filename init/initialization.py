from config import database
from init.database import initdb
from tools.database import connect, disconnect


def initialization():
    """
    Initializes various components of application
    """
    connect(database)
    initdb()
    disconnect()
