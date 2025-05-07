cart = ['Towel', 'Eggs', 'Bread', 'Butter']
price = [2.00, 1.50, 2.00, 2.50]
quantity = [1, 2, 2, 4]



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
    try:
        item_add = input("Enter Item To Add: ")
        item_price = float(input("Enter price of Item: "))
        item_qty = int(input("Enter Quantity: "))
        if not item_add:
            print(f"Your item is empty, please add items")
        elif item_price <=0 or item_qty <=0:
            print(f"Your item price and quantity is empty, please add price and quantity")
        else:
            cart.append(item_add)
            price.append(item_price)
            quantity.append(item_qty)
            print(f"Added {item_qty} x {item_add} at ${item_price:.2f} each.")
    except ValueError:
        print("Please enter the valid numbers for prince and quantity.")




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
        for i, (item, cost, qty) in enumerate(zip(cart, price, quantity), start=1):
            total = cost * qty
            print(f"{i}.Item: {item} -- ${cost:.2f} x {qty} = ${total:.2f} ")


def checkout():
    items = sum(quantity)
    total = compute_total()
    print(f"You have {items} item(s) number of items.")
    print(f"Total Amount: ${total:.2f}")

def compute_total():
    total = 0
    for index in range(len(price)):
        total += price[index] * quantity[index]
    return total


while True:
    output()


