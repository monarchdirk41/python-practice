cart = ['Towel', 'Eggs', 'Bread', 'Butter']
price = [2.00, 1.50, 2.00, 2.50]



def output():
    try:
        print("----Menu----")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Remove Item")
        print("4. Checkout")
        print("5. Exit")

        enter_input = int(input("Enter Selection 1, 2, 3, 4 or 5: "))
        if enter_input == 1:
            add_item()
        elif enter_input == 2:
            view_cart()
        elif enter_input == 3:
            del_item()
        elif enter_input == 4:
            checkout()
        elif enter_input == 5:
            print("Exiting. Thank you for shopping!")
            exit()
    except ValueError:
        print("Please Enter Numbers only!")



def add_item():
    item_add = input("Enter Item To Add: ")
    item_price = float(input("Enter price of Item: "))
    if not item_add:
        print(f"Your item is empty, please add items")
    elif not item_price:
        print(f"Your item price is empty, please add price")
    else:
        cart.append(item_add)
        price.append(item_price)
        print(f"You added {item_add} with the price of {item_price} to your shopping cart!")




def del_item():
    view_cart()
    delete_item = int(input("Enter the number you want to delete: "))
    remove_number = delete_item - 1
    remove_item = cart[remove_number]
    confirmation = input(f"Are you sure you want to remove {remove_item} in your cart? Y/N: ").capitalize()
    if confirmation.startswith("Y"):
        del cart[remove_number]
        del price[remove_number]
        print(f"You have removed {remove_item} your shopping cart.")
    elif confirmation.startswith("N"):
        return del_item()
    else:
       print("Please Enter the right value")



def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:

        print("Items in your cart:")
        #test = dict(zip(cart, price))
        for i, (item, cost) in enumerate(zip(cart, price), start=1):
            print(f"{i}.Item: {item} -- Price: ${cost}")


def checkout():
    items = len(cart)
    total = compute_total()

    print(f"You have {items} number of items!")
    print(f"Total Amount: ${total:.2f}")

def compute_total():
    return sum(price)


while True:
    output()


