max_attempts = 3
attempts = 0


def input_age():
    try:
       enter_age = int(input("Enter your age: "))
       if enter_age < 18:
            print("Sorry, You must be 18+ to continue.")
       else:
            print(f"Thank You! Your age is {enter_age}. Proceeding...")
            return True

    except ValueError:
        print("Please enter a valid number.")

    return False



while attempts < max_attempts:
   if input_age():
       break
   attempts = attempts + 1
   if attempts < max_attempts:
       print(f"Attempts left: {max_attempts - attempts}")
   else:
       print("Maximum attempts reached. Exiting")



