# notes.py - Simple notes application

# modules
import sys
import datetime
import getpass
import sqliteauthenticate as authenticate
import sqldatabase as database
import fetchwebt
import jsonnotes

# main function
def main() -> int:
    # Main loop will run as long as username is not empty.
    while (True):
        # userid is set initially to -1. In this app it means that user is not authenticated.
        userid = -1

        # Login loop
        while (userid == -1):
            print("\nLogin or just press enter to exit the application.\n")
            username = input("Username: ")
            # Exit main function and application if username is empty
            if (username == ""):
                return 0
            password = getpass.getpass()
            userid = authenticate.authenticate(username, password)

        # Empty line
        print()

        # Main menu
        onmainmenu = True
        while (onmainmenu):
            print("Main menu:")
            print("1. Create a note")
            print("2. Retrieve notes")
            print("3. Load a note from a json file")
            print("4. Logout")

            try:
                choice = int(input("Choose and press enter: "))
            except ValueError:
                # if input is not a number
                choice = -1

            # Create a new note
            if choice == 1:
                # Ask for details
                subject = input("Subject: ")
                text = input("Text: ")
                url = input("Web page: ")

                # Get the current time without seconds or milliseconds
                current_time_formatted = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                # Create a new note
                result = database.createnote(userid, subject, current_time_formatted, text, url)

                # Print the result
                print("New note created: " + str(result))

            # List notes of current user and open a new menu to access them
            elif choice == 2:
                # Request list of notes
                usernotes = database.listusernotes(userid)

                # List number
                number = 0

                # Fetch details of each note and show them in menu
                for n in usernotes:
                    print(str(number) + ". " + database.notedetails(n)["subject"])
                    number += 1
                
                # Show details of one note and show note specific menu
                try:
                    selectednote =  int(input("Enter a number of a note of any other number to exit: "))
                except ValueError:
                    # if input is not a number
                    selectednote = -1

                if ((selectednote < len(usernotes)) and (selectednote >= 0)):
                    note = database.notedetails(usernotes[selectednote])
                    print("--- --- ---")
                    print("Subject: " + note["subject"])
                    print("Date: " + str(note["date"]))
                    print("Text: " + note["text"])
                    print("Web page: " + note["url"])
                    print("Web title: " + fetchwebt.fetchtitle(note["url"]))
                    print("--- --- ---")
                    # One new menu loop that is used to delete menu item
                    choice = input("Type \"Delete\" to delete this note or press enter to go back: ")

                    if (choice.lower() == "delete"):
                        database.deletenote(usernotes[int(selectednote)])
                        # Reset choice variable as it is used in other menus
                        choice = 0
                    else:
                        # Reset choice variable as it is used in other menus
                        choice = 0

                else:
                    # Reset choice variable as it is used in other menus
                    choice = 0

            elif choice == 3:
                # This try will cover also fails inside jsonnotes module
                try:
                    filename = input("Filename: ")
                    note = jsonnotes.readjsonfile(filename)
                    note_date = datetime.datetime.strptime(note["date"], "%Y-%m-%d %H:%M:%S") if note["date"] else datetime.datetime.now()
                    database.createnote(userid, note["subject"], note["date"], note["text"], note["www"])
                except Exception as error:
                    print(error)

            # Rest of the answers will log user out
            else:
                onmainmenu = False

# main function entry point
if __name__ == '__main__':
    sys.exit(main())