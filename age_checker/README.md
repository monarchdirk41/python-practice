# 🧓 Age Validator (Python) with Retry Limit

A simple Python program that asks the user for their age, validates the input, and allows access only if the user is 18 or older.  
The program includes a retry limit (3 attempts) to avoid infinite loops or abuse.

---

## 🚀 Features

- 🧠 Input validation with `try/except`
- 🔁 Allows up to 3 attempts before exiting
- 🔞 Enforces minimum age requirement (18+)
- 🧼 Clean function-based logic
- 📝 Console-based interaction

---

## 📋 How It Works

1. The user is prompted to enter their age
2. If the input is not a number, they are asked again
3. If the age is less than 18, access is denied
4. If the age is valid (18+), access is granted
5. If the user enters invalid data 3 times, the program exits

---

## 🖥️ How to Run

Make sure Python is installed, then run:

```bash
python main.py
