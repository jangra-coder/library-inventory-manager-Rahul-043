# Parent class to show Inheritance
class Item:
    def __init__(self, title):
        self.title = title

    # This method will be overridden in Book class (Polymorphism)
    def get_info(self):
        return f"Item Name: {self.title}"


# Book class inherits Item class (Inheritance)
class Book(Item):
    def __init__(self, title, author, isbn, status="available"):
        super().__init__(title)   # calling parent class constructor
        self.author = author
        self.isbn = isbn
        self.status = status

    # overriding parent method → Polymorphism
    def get_info(self):
        return f"Book: {self.title} by {self.author}"

    def __str__(self):
        return f"{self.title} | {self.author} | {self.isbn} | {self.status}"

    # used for saving book data in json file
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False
