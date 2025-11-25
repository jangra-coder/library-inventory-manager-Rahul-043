# library-inventory-manager-Rahul(043)
Rahul(043) Lab assignment 3 submission

# Library Inventory Manager – Mini Project

This is my mini project for the Python subject (Programming for Problem Solving).  
I made a simple Library Inventory System using basic OOP concepts.  
The project helps to manage books in a very simple way like adding, issuing, returning and searching books.

The data of books is saved in a JSON file so that it is available even after closing the program.

---

## Files in the Project

1. Book.py  
   - Contains Item (parent class) and Book (child class)  
   - Shows Inheritance and Polymorphism  
   - Handles book details like title, author, isbn and status  

2. inventory.py  
   - Manages all books  
   - Loads and saves data in books.json  
   - Handles adding, searching and showing books  

3. main.py  
   - This file runs the menu and connects everything  
   - User can choose what action to perform  

> Note: The books.json file is created automatically when the program runs.

---

## OOP Concepts Used in My Project

I have used all four main pillars of Object Oriented Programming:

### 1. Encapsulation
I grouped data and functions inside classes like `Book`, `Item`, and `Inventory`.  
All book details stay inside the class only.

### 2. Abstraction
The user does not see the internal working like how JSON is saved.  
They only use simple functions such as `add_book()`, `issue()`, etc.

### 3. Inheritance
I created a parent class **Item** and a child class **Book** which inherits Item.  
This shows how features can be reused.

### 4. Polymorphism
The parent class has a function `get_info()` and  
the Book class overrides it with its own version.  
Same function name but different output.

---

## How to Run

Keep all Python files in the same folder.  
Then open terminal and run:

python3 main.py

(or `python main.py` depending on your system)

---

## Features

- Add new books  
- Issue and return a book  
- Search using title  
- Show all books  
- Stores data in a JSON file  
- Simple and easy menu based system  

---

## Concepts Used

- Classes and Objects  
- JSON File Handling  
- Lists and Dictionaries  
- Exception Handling  
- OOP (Encapsulation, Abstraction, Inheritance, Polymorphism)  
- CLI (Command Line Interface)
