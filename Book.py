class Book:
    def __init__(self, title, author, isbn, status="available"):
        # basic details of book
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        # printing book details in readable way
        return f"{self.title} | {self.author} | {self.isbn} | {self.status}"

    def to_dict(self):
        # used for saving data in json file
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
