import sys
import sqlite3

# connect to the database
def connect() -> sqlite3.Connection:
    con = sqlite3.connect("notes.sqlite")
    return con

# authentication function
# returns : userid as an integer
# return value -1 means that user was not found
def authenticate(username, password) -> int:
    # Connect to the database
    con = connect()
    # Set cursor
    cur = con.cursor()
    # Create a request and execute it
    res = cur.execute("SELECT id FROM users WHERE username = ? AND password = ?", [username, password])
    # Assuming that there is only one user with this username and password
    userid = res.fetchone()
    # Close database connection
    con.close()
    # Nothing was found if userid is None
    if userid == None:
        return -1
    else:
        return userid[0]

# main function
def main() -> int:
    username = input("username: ")
    password = input("password: ")
    result = authenticate(username, password)
    print(result)
    if result >= 0:
        #Authentication was successful
        return 0
    else:
        #Authentication failed
        return 1

# main function entry point
if __name__ == '__main__':
    sys.exit(main())

