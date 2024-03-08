import sqlite3


# Main Class
class Main:
    def __init__(self):
        self.conn = sqlite3.connect("db/DataBase.sqlite")

    def SetupDB(self, conn):
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS Users
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, password TEXT)"""
        )
        conn.commit()
        c.close()
