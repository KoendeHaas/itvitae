contacts = [
    {"name":"piet",
    "tel" : "124-456",
    "email": "piet@email.nl"}
]

def list_users():
    for contact in contacts:
        print(f"""
        Name: {contact["name"]}
        Phone: {contact["tel"]}
        Email: {contact["email"]}
        """)

def add_user():
    contact = {}
    contact["name"] = (input("Please enter name: "))
    contact["tel"] = (input("Please enter phone: "))
    contact["email"] = (input("Please enter email: "))
    contacts.append(contact)
 
action = None

while action != "exit":
    # Main menu
    print("""
    What to do?
    1. List entries
    2. Add entry
    3. Exit
    """)

    action = input()
 
    match action:
        # List entries
        case "1":
            list_users()
        # Add entry
        case "2":
            add_user()
        case "3":
            action = "exit"
        case _:
            print("Invalid input")
            
        # case "exit":
        #     return