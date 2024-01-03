import sqlite3

# connect to the database
def connect() -> sqlite3.Connection:
    con = sqlite3.connect("notes.sqlite")
    # Try to create a table everytime to ensure that database exists
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE notes(id INTEGER PRIMARY KEY AUTOINCREMENT, userid, subject, date, text, url)")
    except:
        pass
        # Table likely exists - ignore and continue
    return con

# create a new note for a specific user
# arguments : userid, subject, date, text
# returns : noteid or -1 if note creation fails
def createnote(userid, subject, date, text, url="") -> int:
    con = connect()
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO notes (userid, subject, date, text, url) VALUES (?, ?, ?, ?, ?)", [userid, subject, date, text, url])
        noteid = cur.lastrowid
        con.commit()
    except:
        noteid = int(-1)
    con.close()
    return(noteid)

# list database ids of notes of a user
# arguments : userid
# returns : list of user's notes
def listusernotes(userid) -> []:
    con = connect()
    # Create a new empty list that will contain ids and subject of a user notes
    usernotes = []
    cur = con.cursor()
    cur.execute("SELECT id, subject FROM notes WHERE userid = ?", [userid])
    usernotes = cur.fetchall()
    con.close()
    return usernotes

# list note details
# arguments : noteid
# returns : a note item as a dictionary
def notedetails(noteid) -> {}:
    con = connect()
    note = {}
    cur = con.cursor()
    cur.execute("SELECT userid, subject, date, text, url FROM notes WHERE id = ?", [noteid[0]])
    # Take only first. There should not be more than one because id is the primary key
    res = cur.fetchone()
    con.close()
    # Database result res is tuple. It needs to be converted to dictionary
    note = {
        "userid": res[0],
        "subject": res[1],
        "date": res[2],
        "text": res[3],
        "url": res[4]
    }
    return note

# delete a note
# arguments : noteid
# returns : True is success or False in case of failure
def deletenote(noteid) -> bool:
    print(noteid)
    result = False
    con = connect()
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM notes WHERE id = ?", [noteid[0]])
        con.commit()
        result = True
    except:
        result = False
    con.close()
    # Return True for now
    return result