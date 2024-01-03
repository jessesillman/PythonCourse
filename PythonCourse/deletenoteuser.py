# deletenotesuser.py -- Delete notes user from the users table in the notes database

import sqlite3

username = input("username: ")
password = input("password: ")
# Create database connection
con = sqlite3.connect("notes.sqlite")
cur = con.cursor()
# Select user from the database and print the user
res = cur.execute("SELECT id, username FROM users WHERE username = ? AND password = ?", [username, password])
# Assuming that only one is found. If there are multiple only one is deleted.
notesuser = res.fetchone()
print(notesuser)
# Confirm delete
confirm = input("Do you want to delete the user? ")
if confirm == "yes":
    res = cur.execute("DELETE FROM users WHERE id = ? AND username = ?", notesuser)
else:
    print("Nothing done.")
# Commit all the changes. This will make the changes permanent.
con.commit()
# Print all the users
res = cur.execute("SELECT id, username FROM users")
print(res.fetchall())
# Close the datanase connection
con.close()