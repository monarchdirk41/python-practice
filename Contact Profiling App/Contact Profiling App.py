
contacts = {
            "James": {"Email": "test@test.com", "Status": "cold", "Phone": "09171177387"},
            "Chaki": {"Email": "chaki@test.com", "Status": "lead", "Phone": "6849321"},
            "Felicia": {"Email": "felicia@example.com", "Status": "cold"}}


def add_contact():
    enter_name = input("Enter Name: ").title().strip()
    enter_email = input("Enter Email: ").strip()
    enter_status = input("Enter Status (Lead/Customer/Cold) ").lower().strip()
    enter_phone = input("Enter Phone: ")

    contacts[enter_name] = {"Email": enter_email, "Status": enter_status, "Phone": enter_phone}
    print(f"{enter_name} has been added.")


def display_contact():
    print("---Contacts---")
    for name, info in contacts.items():
        print(f"Name: {name.title()}")
        print(f"Email: {info.get('Email', 'N/A')}")
        print(f"Status: {info.get('Status', 'N/A')}")
        print(f"Phone: {info.get('Phone', 'N/A')}")
        print("---")


def search_by():
    try:
        print("--Search a Contact--")
        print("Search a Contact by?")
        print("1. Name")
        print("2. Status")
        print("3. Phone Number")
        print("4. Exit")
        enter_search_input = int(input("Enter selection: "))

        if enter_search_input == 1:
            search_by_name()
        elif enter_search_input == 2:
            search_by_status()
        elif enter_search_input == 3:
            search_by_phone()
        elif enter_search_input == 4:
            return output()
        else:
            print("Please enter a valid input.")
    except ValueError:
        print("Please enter a number value.")

def search_by_name():
    search_name = input("Please enter name to search:").title().strip()
    found = False

    print(f"\nNames Retrieved: {search_name.title()}")
    for name, info in contacts.items():
        if name == search_name:
            print(f"Name: {name.title()}")
            print(f"Email: {info.get('Email', 'N/A')}")
            print(f"Status: {info.get('Status', 'N/A')}")
            print(f"Phone Number: {info.get('Phone', 'N/A')}")
            print("---")
            found = True
    if not found:
        print("No contact found with that name")


def search_by_phone():
    search_phone = input("Please enter phone number: ")
    found = False

    print(f"Phone Number Found: {search_phone}")
    for name, info in contacts.items():
        if info.get("Phone") == search_phone:
            print(f"Name: {name.title()}")
            print(f"Email: {info.get('Email', 'N/A')}")
            print(f"Status: {info.get('Status', 'N/A')}")
            print("---")
            found = True
    if not found:
        print("No contact found with that phone number")



def search_by_status():
    search_contact = input("Enter the status of contact (Lead/Customer/Cold): ").lower().strip()
    found = False

    print(f"\nContacts with status: {search_contact.title()}")
    for name, info in contacts.items():
        if info.get("Status") == search_contact:
            print(f"Name: {name.title()}")
            print(f"Email: {info.get('Email', 'N/A')}")
            print(f"Status: {info.get('Status', 'N/A')}")
            print("---")
            found = True
    if not found:
        print("No contact found with that status.")


def show_phone():
    count = 0
    for name, key in contacts.items():
        if key.get("Phone"):
            count = count + 1

    print(f"{count} contacts have phone numbers.")



def output():
    while True:
        try:

            print("---Contact Profiling---")
            print("1. Add New Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Show Contacts with Phone Numbers")
            print("5. Exit")
            enter_selection = int(input("Enter your selections (1, 2, 3, or 4):"))


            if enter_selection == 1:
                add_contact()
            elif enter_selection == 2:
                display_contact()
            elif enter_selection == 3:
                search_by()
            elif enter_selection == 4:
                show_phone()
            elif enter_selection == 5:
                exit()
            else:
                print("Invalid input, please enter 1, 2, 3 or 4")
        except ValueError:
            print("Please enter a number value.")





output()









