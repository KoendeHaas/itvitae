contacts = [
    ["piet",
    "124-456",
    "piet@email.nl"]
]
action = ""

while action != "exit":
    print("""
    What to do?
    1. List entries
    2. Add entry
    """)

    action = input()

    # List entries
    match action:
        case "1":
            for contact in contacts:
                print(f"""
                Name: {contact[0]}
                Phone: {contact[1]}
                Email: {contact[2]}
                """)
        # Add entry
        case "2":
            contact = []
            contact.append(input("Please enter name: "))
            contact.append(input("Please enter phone: "))
            contact.append(input("Please enter email: "))
            contacts.append(contact)
        # case "exit":
        #     return