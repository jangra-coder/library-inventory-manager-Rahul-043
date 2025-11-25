from Inventory import Inventory

inv = Inventory()

def menu():
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

while True:
    menu()
    ch = input("Enter choice: ")

    if ch == "1":
        t = input("Enter title: ")
        a = input("Enter author: ")
        i = input("Enter ISBN: ")
        inv.add_book(t, a, i)
        print("Book added successfully!")

    elif ch == "2":
        isbn = input("Enter ISBN to issue: ")
        b = inv.search_isbn(isbn)
        if b and b.issue():
            inv.save_data()
            print("Book issued.")
        else:
            print("Book not available or wrong ISBN.")

    elif ch == "3":
        isbn = input("Enter ISBN to return: ")
        b = inv.search_isbn(isbn)
        if b and b.return_book():
            inv.save_data()
            print("Book returned.")
        else:
            print("Invalid operation.")

    elif ch == "4":
        all_books = inv.show_all()
        if len(all_books) == 0:
            print("No books in the library.")
        else:
            for bk in all_books:
                print(bk)

    elif ch == "5":
        key = input("Enter title keyword to search: ")
        res = inv.search_title(key)
        if len(res) == 0:
            print("No matching book found.")
        else:
            for bk in res:
                print(bk)
                # Showing polymorphism example
                print("Info:", bk.get_info())

    elif ch == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice. Try again.")
