# dbSetup.py

# This class is in charge of creating the database file (if not present) and the tables.

import sqlite3
import os


class SetupDB:

    def __init__(self, conection):
        self.conn = None

    def createDB(self):
        if not os.path.exists("db/DataBase.sqlite"):
            self.conn = sqlite3.connect("db/DataBase.sqlite")
            self.conn.close()
            print("Database created")
        else:
            print("Database already exists")
