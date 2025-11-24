import json
import os
from Book import Book

class Inventory:
    def __init__(self):
        self.filename = "books.json"
        self.books = []
        self.load_data()

    def load_data(self):
        # load existing book data if file exists
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    for b in data:
                        self.books.append(Book(b["title"], b["author"], b["isbn"], b["status"]))
            except:
                # if file is corrupted or empty
                self.books = []
        else:
            # if json file doesn't exist, create empty file
            with open(self.filename, "w") as f:
                json.dump([], f)

    def save_data(self):
        data = [b.to_dict() for b in self.books]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def add_book(self, title, author, isbn):
        newBook = Book(title, author, isbn)
        self.books.append(newBook)
        self.save_data()

    def search_title(self, keyword):
        result = []
        for b in self.books:
            if keyword.lower() in b.title.lower():
                result.append(b)
        return result

    def search_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def show_all(self):
        return self.books
