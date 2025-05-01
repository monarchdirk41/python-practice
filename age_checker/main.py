
def input_age():
    try:
        enter_age = int(input("Enter your age: "))
        if enter_age <= 0:
            print("Age must be greater than 0.")
        else:
            print(f"Thank You! You entered {enter_age}")
            return True

    except ValueError:
        print("Please enter a valid number.")
    return False



while True:
   if input_age():
       break



