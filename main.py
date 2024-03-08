import sqlite3
from dbSetup import SetupDB


# Main Class
class Main:
    def __init__(self):
        self.connection = sqlite3.connect(
            "db/DataBase.sqlite"
        )  # this command creates the database file if it doesn't exist, and also connects to it.

        self.db = SetupDB()  # db setup instance

    def ConnectDB(self):
        # Connect to the database
        self.db.createTables(self.connection)
        self.db.CreateAdmin(self.connection)

    def Start(self):
        self.ConnectDB()


# Main
if __name__ == "__main__":
    Main().Start()
