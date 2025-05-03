users = ['James', 'Dirk', 'Jerome', 'Daryl']
age = [38, 41, 39, 50]



def output():
    while True:
        print("-----Menu-----")
        print("1. Add New User")
        print("2. Show Users")
        print("3. Exit")

        input_user = input("Select an option: ")

        if input_user == "1":
            attempts_reached(add_user)
        elif input_user == "2":
            show_user_and_age()
        elif input_user == "3":
            return "exit"
        else:
            print("Invalid choice, Please select 1, 2 or 3")



def verify_user():
    name_input = input("Please Enter Your Name: ").capitalize()
    if not name_input.isalpha():
        print("Name must be a valid name.")
        return False

    try:
        age_input = int(input("Please Enter Your Age: "))
    except ValueError:
        print("Age must be a valid number.")
        return False

    user_data = dict(zip(users, age))
    if user_data.get(name_input) == age_input:
        print("Verification successful!\n")
        return True
    else:
        print("Invalid Credentials.\n")
        return False


def attempts_reached(action_func):

    max_attempts = 3
    for attempts in range(max_attempts):
        success = action_func()
        if success:
            return True
        remaining = max_attempts - attempts - 1
        if remaining > 0:
            print(f"You have {remaining} attempt(s) left. \n")
        else:
            print("Max attempts reached. \n")
    return False


def add_user():
    try:
        new_user = input("Enter Name: ")
        if not new_user.isalpha():
            print("Enter Letters only for Name")
            return False

        new_user_age = int(input("Enter Age: "))
        if new_user_age < 0:
            print("Age must be a positive number")
            return False

        users.append(new_user.capitalize())
        age.append(new_user_age)
        print("User added successfully!\n")
        return True

    except ValueError:
         print("Please Enter the right input")
         return False


def show_user_and_age():
    print("\n--- Users ---")
    user_data = dict(zip(users, age))
    for name, age1 in user_data.items():
        print(f"{name} is {age1} years old.")
    print()




if attempts_reached(verify_user):
    output()
