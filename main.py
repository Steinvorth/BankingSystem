import sqlite3
from dbSetup import SetupDB


# Main Class
class Main:
    def __init__(self):
        self.connection = sqlite3.connect("db/DataBase.sqlite")

    def ConnectDB(self):
        # Connect to the database
        self.db = SetupDB(self.connection)
        self.db.createTables()
        self.db.CreateAdmin()

    def Start(self):
        self.ConnectDB()


# Main
if __name__ == "__main__":
    Main().Start()
