# dbSetup.py

# This class is in charge of creating the database file (if not present) and the tables.

import sqlite3
import os


class SetupDB:

    def __init__(self):
        self.conn = None

    def createDB(self, conn):
        self.conn = conn
        # This method creates the Database File if not present already.
        if not os.path.exists("db/DataBase.sqlite"):
            conn = sqlite3.connect("db/DataBase.sqlite")
            # self.conn.close()
            print("Database created")

        else:
            print("Database already exists")

    def createTables(self, conn):
        # This method creates the tables in the database file.
        conn.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, email TEXT NOT NULL, role TEXT NOT NULL)"
        )

        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS Accounts (id INTEGER PRIMARY KEY AUTOINCREMENT, accName TEXT NOT NULL, balance REAL NOT NULL, transactions INTEGER NOT NULL)"
        )

        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS Transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, Transaction_id INTEGER NOT NULL, account_id INTEGER NOT NULL, amount INTEGER NOT NULL, date TEXT NOT NULL)"
        )

        self.conn.close()

        print("Tables created")
