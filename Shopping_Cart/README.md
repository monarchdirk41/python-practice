# 🛒 Python Shopping Cart App (With Quantity & Total Cost)

A beginner-friendly terminal-based shopping cart program written in Python. This interactive app allows users to add items with price and quantity, view their cart with auto-calculated subtotals, remove items, and checkout with a computed total cost.

---

## ✨ Features

- ✅ Add items to cart with price and quantity
- 🔢 View cart with numbered list, showing item × quantity = subtotal
- 🗑️ Remove items by selecting their number (with confirmation)
- 🧮 Checkout calculates total number of items and total price
- 🧠 Input validation for blank inputs, invalid numbers, and prices
- 🔁 Runs continuously until user selects Exit

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

1.Add Item
2.View Cart
3.Remove Item
4.Checkout
5.Exit
Enter Selection 1, 2, 3, 4 or 5: 1

Enter Item To Add: Milk
Enter price of Item: 2.25
Enter Quantity: 3
✅ Added 3 x Milk at $2.25 each.


---

## 🧠 What You'll Practice

- Using multiple lists (`cart`, `price`, `quantity`) in sync
- Looping with `enumerate()` and `zip()`
- Calculating subtotals and overall total
- Validating user inputs using `try/except`
- Removing list items safely by index

---

## ▶️ How to Run

Make sure Python 3 is installed on your system. Then run:

```bash
python shopping_cart.py

🔮 Future Enhancements
💰 Show tax or apply discount logic
🧾 Save and load cart items from a file
🧩 Track stock or product codes
🔄 Undo last action
📊 Show cart summary sorted by total cost


👨‍🎓 Built For Learning
This app was created as a learning project to master Python fundamentals such as lists, loops, function structure, and clean user input handling.

🙋‍♀️ Author
This was created as a learning project while practicing Python fundamentals such as loops, lists, and function control. Perfect for anyone just getting started with coding!
