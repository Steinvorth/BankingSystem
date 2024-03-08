import sqlite3
from dbSetup import SetupDB
from dbConnection import dbConnection


# Main Class
class Main:
    def __init__(self):
        self.connection = None

        # DB Class Instance
        self.db = SetupDB()

    def ConnectDB(self):
        self.connection = sqlite3.connect("db/DataBase.sqlite")

        self.db.createDB(self.connection)
        self.db.createTables(self.connection)

    def Start(self):
        self.ConnectDB()


# Main
if __name__ == "__main__":
    Main().Start()
