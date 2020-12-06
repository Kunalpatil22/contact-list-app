import sqlite3
database = sqlite3.connect('contacts.db')
cursor = database.cursor()
running_status = True

def add(name, email):
    cursor.execute(f"INSERT INTO contacts VALUES ('{name}', '{email}')")
    database.commit()

def show_all():
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    print("----- Contacts -----\n")
    for contact in contacts:
        print(f"{contact[0]} - {contact[1]}\n")
    database.commit()

while running_status:
    primary_input = input("> ")

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

