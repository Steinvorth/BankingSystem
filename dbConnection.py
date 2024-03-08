# SQL connection to SQLite3

import sqlite3


class dbConnection:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect("db/DataBase.sqlite")
        return self.conn

    def close(self):
        self.conn.close()
        return "Connection Closed"
