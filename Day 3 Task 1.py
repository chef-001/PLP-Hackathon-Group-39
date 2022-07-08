#Day 3 Task One
from datetime import datetime
now = datetime.now()

password_key = "2022"
password = input("Enter the password: ")

command_1 = 'open'
command_2 = 'close'
command_3 = 'quit'

while password != password_key:
    print("Wrong password please try again!")
    password = input("Enter the password: ")
else:
    print("Welcome!")

print("""
Here are the commands for the door:
1. Open - to open the door
2. close - to close the door
3. quit - to exit the command menu.\n""")

opened = False
while True:
    command = input("Enter a command for the door: ").lower()
    if command == command_1:
        if opened:
            print("The door is already opened.")
        else:
            opened = True
            print("Door Last Open at ",now)
            print("The door is now open.")
    elif command == command_2:
        if not opened:
            print("The door is already locked.")
        else:
            opened = False
            print("The door is now locked")
            print("Door Last Open at ", now)
    elif command == command_3:
        print("Exiting Command Menu")
        break
    else:
        print("Invalid Command.")
