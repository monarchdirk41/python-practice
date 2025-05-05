# 🛒 Python Shopping Cart System

This is a beginner-friendly Python terminal app that simulates a basic shopping experience. Users can add items with prices, view their cart, delete items by number, and checkout — all via a simple numbered menu.

---

## ✨ Features

- ✅ Add items with price to the shopping cart
- 🔢 View cart with auto-numbered items and prices
- 🗑️ Remove items by selecting the number (with confirmation)
- 🧾 Checkout shows how many items are in the cart
- 🧠 Input validation (e.g., no blank item names, price must be a number)
- 🔁 Runs in a loop until user chooses to exit

---

## 📋 Menu Options

1. Add Item
2. View Cart
3. Remove Item
4. Checkout
5. Exit

---

## 🧠 What You’ll Learn

- Using `for` loops and `enumerate()` for numbered lists
- Managing two synced lists (`cart[]` and `price[]`)
- Handling input and errors with `try/except`
- Working with functions for clean, reusable code
- `del` for list element deletion by index

---

## ▶️ How to Run

Make sure Python 3 is installed. Then, run the program:

```bash
python shopping_cart.py


Sample Output

----Menu----
1. Add Item
2. View Cart
3. Remove Item
4. Checkout
5. Exit
Enter Selection 1, 2, 3, 4 or 5: 2

Items in your cart:
1. Item: Towel -- Price: $2.0
2. Item: Eggs -- Price: $1.5

Enter Selection 1, 2, 3, 4 or 5: 3
Enter the number you want to delete: 2
Are you sure you want to remove Eggs from your cart? Y/N: Y
✅ You removed Eggs from your shopping cart.



📌 Future Ideas
-Total cost calculation at checkout
-Quantity per item
-Save cart to a file
-Load previous sessions
-Item category filters


👨‍🎓 Built For Learning
This app was created to strengthen understanding of:
-Python lists
-Input handling
-enumerate(), zip(), and del
-Function-based program flow


🙋‍♀️ Author
This was created as a learning project while practicing Python fundamentals such as loops, lists, and function control. Perfect for anyone just getting started with coding!
