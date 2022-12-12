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

def search_user():
    query = input("Please enter an email adress:\n")
    
    for contact in contacts:
        if query in contact["email"]:
            print(contact)
            return True
    
        ("User not found")
    return False
    
action = None

while action != "exit":
    # Main menu
    print("""
    What to do?
    1. List entries
    2. Search entry
    3. Add entry
    4. Exit
    """)

    action = input()
 
    match action:
        # List entries
        case "1":
            list_users()
        # Search entry
        case "2":
            search_user()
        # Add entry
        case "3":
            add_user()
        case "4":
            action = "exit"
        case _:
            print("Invalid input")
            
        # case "exit":
        #     return