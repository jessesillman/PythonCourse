# insertnotesuser.py -- Insert a new notes user in the users table in the notes database

import sqlite3

username = input("username: ")
password = input("password: ")
# Create database connection
con = sqlite3.connect("notes.sqlite")
cur = con.cursor()
# Try to create a database
try:
    cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, username, password)")
except:
    pass
    # Table likely exists - ignore and continue
# Insert a new user
cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", [username, password])
# Commit all the changes. This will make the changes permanent.
con.commit()
# Print all the users
res = cur.execute("SELECT id, username FROM users")
print(res.fetchall())
# Close the datanase connection
con.close()