import sqlite3
import tkinter as tk
from dbSetup import SetupDB


# Main Class
class Main:
    def __init__(self):
        self.connection = sqlite3.connect(
            "db/DataBase.sqlite"
        )  # this command creates the database file if it doesn't exist, and also connects to it.

        self.root = tk.Tk()

        self.db = SetupDB()  # db setup instance

    def SetupDB(self):
        # Setup the database
        self.db.createTables(self.connection)
        self.db.CreateAdmin(self.connection)
        self.db.CreateUsers(self.connection)
        self.db.CreateAccounts(self.connection)

    def LoginWindow(self):
        # Simple Login to Differentiate between admin, and users.
        self.root.title("Login")
        self.root.geometry("500x600")

        lblusername = tk.Label(self.root, text="Username")
        lblusername.grid(row=0, column=0, padx=5, pady=5)

        usernameEntry = tk.Entry(self.root)
        usernameEntry.grid(row=0, column=1, padx=5, pady=5)

        lblpassword = tk.Label(self.root, text="Password")
        lblpassword.grid(row=1, column=0, padx=5, pady=5)

        passwordEntry = tk.Entry(self.root, show="*")
        passwordEntry.grid(row=1, column=1, padx=5, pady=5)

        btnLogin = tk.Button(
            self.root,
            text="Login",
            commands=self.handleLogin(usernameEntry, passwordEntry),
        )
        btnLogin.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.root.mainloop()

    def handleLogin(self, usernameEntry, passwordEntry):
        pass

    def Start(self):
        self.SetupDB()
        self.LoginWindow()


# Main
if __name__ == "__main__":
    Main().Start()
