cart = ['Towel', 'Eggs', 'Bread', 'Butter']

def output():
    try:
        print("----Menu----")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Checkout")
        print("4. Exit")

        enter_input = int(input("Enter Selection 1, 2, 3 or 4: "))
        if enter_input == 1:
            add_item()
        elif enter_input == 2:
            view_cart()
        elif enter_input == 3:
            checkout()
        elif enter_input == 4:
            print("Exiting. Thank you for shopping!")
            exit()
    except ValueError:
        print("Please Enter Numbers only!")



def add_item():
    item_add = input("Enter Item To Add: ").strip()
    if item_add:
        cart.append(item_add)
        print(f"You added {item_add} to your shopping cart!")
    else:
        print("Please enter an item name.")


def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        for i, index in enumerate(cart):
            print(f"{i + 1}. {index}")


def checkout():
    count = 0
    for items in cart:
        count += 1
    print(f"You have {count} number of items!")




while True:
    output()


