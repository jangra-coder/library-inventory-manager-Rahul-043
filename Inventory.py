import json
import os
from Book import Book

class Inventory:
    def __init__(self):
        self.filename = "books.json"
        self.books = []
        self.load_data()

    # loads books from json file
    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    for b in data:
                        new_book = Book(b["title"], b["author"], b["isbn"], b["status"])
                        self.books.append(new_book)
            except:
                self.books = []
        else:
            # create a new empty file if not available
            with open(self.filename, "w") as f:
                json.dump([], f)

    # saves books list to json file
    def save_data(self):
        data = []
        for b in self.books:
            data.append(b.to_dict())
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    # add a new book
    def add_book(self, title, author, isbn):
        b = Book(title, author, isbn)
        self.books.append(b)
        self.save_data()

    # search by title keyword
    def search_title(self, key):
        res = []
        for b in self.books:
            if key.lower() in b.title.lower():
                res.append(b)
        return res

    # search exact isbn
    def search_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    # show all books
    def show_all(self):
        return self.books
