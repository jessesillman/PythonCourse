# MODULES:
import sys, getpass, datetime

# PREDEFINED ACCOUNTS AND PASSWORDS:
users = {
    "user1": "pass1",
    "user2": "pass2",
    "user3": "pass3"
}

# EMPTY LIST OF NOTES:
notes = []

# LOGIN MENU:
def main():
    welcome_message()
    while True:
        username = input("Type your username: ")
        # IF THE USERNAME DOES NOT EXIST:
        if not check_username(username):
            print("Invalid username. Try again.")
            continue

        # IF THE USERNAME EXISTS:
        while True:
            password = getpass.getpass("Type your password: ")
            userid = authenticate(username, password)
            
            if userid != -1:
                print("\nHello, " + username + "!")
                notes_menu(userid)
                break
            else:
                print("Invalid password. Try again.")

# CHECK USERNAME FUNCTION:
def check_username(username) -> bool:
    return username in users

# AUTHENTICATION THAT USERNAME MATCHES WITH THE PASSWORD:
def authenticate(username, password) -> int:
    if users[username] == password:
        return list(users.keys()).index(username)
    return -1

# NOTES MENU:
def notes_menu(userid):
    while True:
        print("\nNotes view:")
        print("1. Create a new note")
        print("2. Retrieve a note")
        print("3. Log out")
        print("4. Close the application \n")

        # USER'S CHOICE:
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            create_note(userid)
        elif choice == "2":
            retrieve_notes(userid)
        elif choice == "3":
            logout(userid)
        elif choice == "4":
            close(userid)
        else:
            print("\nInvalid choice.")

# CHOICE 1:
def create_note(userid):
    print("\nYou chose to create a new note.\n")
    subject = input("Enter the subject: ")
    text = input("Type the text: ")
    # DATETIME VARIABLE DISPLAYING A WEEKDAY AND A MONTH:
    date = datetime.datetime.now().strftime('%A, %B %d, %Y. %H:%M')

    # DICTIONARY FOR THE NOTES:
    note = {
        "userid": userid,
        "subject": subject,
        "date": date,
        "text": text
    }

    notes.append(note)
    print("\nNote added successfully!")

# CHOICE 2:
def retrieve_notes(userid):
    print("\nYou chose to retrieve a note.")
    
    # COLLECTING THE NOTES:
    user_notes = [note for note in notes 
                  if note["userid"] == userid]
    if not user_notes:
        print("But you don't have any notes yet!")
        return
    
    # SELECT YOUR NOTE:
    while True:
        print("\nYour notes:")
        for i, note in enumerate(user_notes, 1):
            print(f"{i}. {note['subject']} ({note['date']})")

        try:
            index = int(input("\nSelect a note by number or enter 0 to go back: "))
            if index == 0:
                return
            display_note(user_notes[index-1])
        #ERROR: 
        except (ValueError, IndexError):
            print("\nInvalid selection.")

# CHOICE 3:
def logout(userid):
    print("\nYou chose to log out. See you again!\n")
    main()

# CHOICE 4:
def close(userid):
    print("\nYou chose to close this application. See you again!")
    sys.exit(0)

# DISPLAY NOTES:
def display_note(note):
    print("--- --- --- ---")
    print("Subject:", note["subject"])
    print("Date and time:", note["date"])
    print("Text:", note["text"])
    print("--- --- --- ---")

    # DELETE YOUR NOTE:
    while True:
        delete = input("Do you want to delete this note? (Y/N): ")
        if delete.upper() == "Y":
            notes.remove(note)
            print("\nNote deleted successfully.")
            notes_menu(note["userid"])
        elif delete.upper() == "N":
            notes_menu(note["userid"])
        else:
            print("\nInvalid choice.\n")

# WELCOME MESSAGE:
def welcome_message():
    message = "Welcome to the notes application!"
    createdby = "Created by: Jesse Sillman ITMI22SP"
    max_lenght = max(len(message), len(createdby))

    framed_message = f"  {message.center(max_lenght)}  "  
    framed_createdby = f"  {createdby.center(max_lenght)}  " 

    frame = ' ' + '-' * len(framed_message) + ' ' 
    
    print(frame)
    print(framed_message)
    print(framed_createdby)
    print(frame)
  
# START THE APPLICATION:
if __name__ == '__main__':
    sys.exit(main())