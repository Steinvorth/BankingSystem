# dbSetup.py


# class in charge of populating db with tables and admin user, and some other users.
class SetupDB:

    def createTables(self, conn):
        # This method creates the tables in the database file.
        try:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, email TEXT NOT NULL, role TEXT NOT NULL)"
            )

            print("Table users created")

            conn.execute(
                "CREATE TABLE IF NOT EXISTS Accounts (id INTEGER PRIMARY KEY AUTOINCREMENT, accName TEXT NOT NULL, balance REAL NOT NULL, transactions INTEGER NOT NULL)"
            )

            print("Table Accounts created")

            conn.execute(
                "CREATE TABLE IF NOT EXISTS Transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, Transaction_id INTEGER NOT NULL, account_id INTEGER NOT NULL, amount INTEGER NOT NULL, date TEXT NOT NULL)"
            )

            print("Table Transactions created")

            print("Database created")

        except Exception as e:
            print(f"Error with database: {e}")

    def CreateAdmin(self, conn):
        # This method creates the admin user in the database. The admin can see all the user accounts, and transactions, but not balance.

        try:
            admin = conn.execute(
                "Select * From users where username = 'admin'"
            ).fetchone()  # if this select comes back empty, then we create the admin. This is a way to check if the admin user is already in the db, so we don't create it again.

            if admin is None:
                conn.execute(
                    "INSERT INTO users (username, password, email, role) VALUES ('admin', 'admin', 'admin@bank.com', 'BankAdmin')"
                )
                print("Admin user created")

                conn.commit()

            else:
                print("Admin user already exists")
        except Exception as e:
            print(f"Error with database: {e}")

    def CreateUsers(self, conn):
        # This method creates 3 user accounts in the database. These accounts will be used to use and test the application.
        try:
            users = conn.execute(
                "Select * From users where username IN ('Joe', 'Mary', 'Fred')"
            ).fetchall()  # if this select comes back empty, then we create the user. This is a way to check if the user is already in the db, so we don't create it again.

            if not users:
                conn.execute(
                    "INSERT INTO users (username, password, email, role) VALUES ('Joe', 'Heart', 'joeheart@gmail.com', 'user')",
                )

                conn.execute(
                    "INSERT INTO users (username, password, email, role) VALUES ('Mary', 'Johnson', 'maryj@gmail.com', 'user')"
                )

                conn.execute(
                    "INSERT INTO users (username, password, email, role) VALUES ('Fred', 'Green', 'fgreen@gmail.com','user')"
                )

                conn.commit()
                print("User accounts created")
            else:
                print("User accounts already exist")

        except Exception as e:
            print(f"Error with database: {e}")

    def CreateAccounts(self, conn):
        # This method creates 3 accounts in the database. These accounts will be used to use and test the application.
        try:
            accounts = conn.execute(
                "Select * From Accounts where accName IN ('acc_jh098', 'acc_mj765', 'acc_fg432')"
            ).fetchall()  # if this select comes back empty, then we create the account. This is a way to check if the account is already in the db, so we don't create it again.

            if not accounts:
                conn.execute(
                    "INSERT INTO Accounts (accName, balance, transactions) VALUES ('acc_jh098', 50000, 0)"
                )

                conn.execute(
                    "INSERT INTO Accounts (accName, balance, transactions) VALUES ('acc_mj765', 12000, 0)"
                )

                conn.execute(
                    "INSERT INTO Accounts (accName, balance, transactions) VALUES ('acc_fg432', 3800, 0)"
                )

                conn.commit()
                print("Accounts created")
            else:
                print("Accounts already exist")

        except Exception as e:
            print(f"Error with database: {e}")
