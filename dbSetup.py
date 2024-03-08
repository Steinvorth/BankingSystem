# dbSetup.py

# class in charge of populating db

import sqlite3
import os


class SetupDB:

    def __init__(self, conn):
        self.conn = conn

    def createTables(self):
        # This method creates the tables in the database file.
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, email TEXT NOT NULL, role TEXT NOT NULL)"
        )

        print("Table users created")

        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS Accounts (id INTEGER PRIMARY KEY AUTOINCREMENT, accName TEXT NOT NULL, balance REAL NOT NULL, transactions INTEGER NOT NULL)"
        )

        print("Table Accounts created")

        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS Transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, Transaction_id INTEGER NOT NULL, account_id INTEGER NOT NULL, amount INTEGER NOT NULL, date TEXT NOT NULL)"
        )

        print("Table Transactions created")

        print("Database created")

    def CreateAdmin(self):
        # This method creates the admin user in the database. The admin can see all the user accounts, and transactions, but not balance.
        self.conn.execute(
            "INSERT INTO IF NOT EXITS users (username, password, email, role) VALUES ('admin', 'admin', 'admin@bank.com', 'BankAdmin')"
        )

        print("Admin user created")
