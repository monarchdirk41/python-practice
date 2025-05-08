# 📇 Python Contact Profiling App

A terminal-based Python application that allows you to manage a list of contacts. This project is designed to help you practice and master the use of Python dictionaries, nested data structures, functions, loops, and input validation—skills that are essential for real-world data management and CRM-like applications.

---

## ✨ Features

- **Add New Contact:**  
  Add a new contact by entering the name, email, status (e.g., Lead, Customer, Cold), and phone number. The app normalizes the input (using `.title()`, `.lower()`, and `.strip()`) before storing it.

- **Display Contacts:**  
  View all contacts with their details in a formatted list.

- **Search Contacts:**  
  Search for contacts by:
  - **Name**
  - **Status**
  - **Phone Number**

- **Delete Contact:**  
  Delete a contact by:
  - **Name**
  - **Email**
  - **Phone**  
  The app asks for confirmation before deletion.

- **Show Contacts with Phone Numbers:**  
  Count and display how many contacts in the system have a phone number listed.

- **Input Validation:**  
  The app employs input validation and error handling using `try/except` to ensure data integrity.

- **Menu-Driven Interface:**  
  A simple menu allows you to choose among various options (add, view, search, delete, show phone count, exit) with clear and user-friendly prompts.

---

## ▶️ How to Run

1. Ensure you have Python 3 installed.
2. Clone or download this repository.
3. In your terminal (or command prompt), navigate to the project directory.
4. Run the following command:

    ```bash
    python contact_profiling.py
    ```

The app will display the main menu and await your input.

---

## 🧾 Sample Output

Below is a sample interaction:

---Contact Profiling---

1. Add New Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Show Contacts with Phone Numbers
6. Exit
Enter your selections (1, 2, 3, 4, 5, or 6): 2

---Contacts---
Name: James
Email: test@test.com
Status: cold
Phone: 09171177387

Name: Chaki
Email: chaki@test.com
Status: lead
Phone: 6849321

Name: Felicia
Email: felicia@example.com
Status: cold
Phone: N/A

---Contact Profiling---

1. Add New Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Show Contacts with Phone Numbers
6. Exit
Enter your selections (1, 2, 3, 4, 5, or 6):




---

## 📚 What You'll Learn

- How to store and manage data using Python dictionaries (including nested dictionaries)
- Using functions to structure your code into reusable components
- Applying input validation and error handling (`try/except`)
- Working with loops and conditional logic to build a menu-driven application
- Basic techniques for searching and modifying a dataset

---

## 🔮 Future Enhancements

- **Edit Contact:** Add functionality to update existing contact details.
- **Data Persistence:** Save and load contacts from a file (e.g., CSV or JSON) for lasting data storage.
- **Advanced Search:** Implement more advanced search features or filters.
- **User Authentication:** Expand the app to include a login system before accessing contacts.

---

## 🙋‍♂️ About This Project

This project was created as a learning tool to improve Python programming skills—especially in handling real-world data management tasks. It is ideal for those looking to build foundational skills before moving on to larger projects like CRM consolidators or data-driven applications.

Enjoy managing your contacts, and happy coding!  

