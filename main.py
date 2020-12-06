# Importing SQLite library and connecting to Database. 
import sqlite3
database = sqlite3.connect('contacts.db')
cursor = database.cursor()

# To ensure that the program keeps running.
running_status = True

# function : To a add contact
def add(name, email):
    cursor.execute(f"INSERT INTO contacts VALUES ('{name}', '{email}')")
    database.commit()

# function : To show all contacts     
def show_all():
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    print("----- Contacts -----\n")
    for contact in contacts:
        print(f"{contact[0]} - {contact[1]}\n")
    database.commit()

# While Loop : For program to run in a loop
while running_status:
    # To take user input as commands
    primary_input = input("> ")
    
    # conditions : To run different commands
    if primary_input == "add":
        name = input("> Enter name : ")
        email = input("> Enter email : ")
        add(name, email)
        
    elif primary_input == "show all":
        show_all()
        
    elif primary_input == "exit":
        running_status = False
        cursor.close()
        
    else:
        print("command is invalid")

