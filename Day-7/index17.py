class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def details(self):
        return f"'{self.title}' by {self.author}, Price: ${self.price}"

book1 = Book("1984", "George Orwell", 15.99)
print(book1.details())
