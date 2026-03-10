class BookStore:
    def __init__(self, title, author, qty, price):
        self.title = title
        self.author = author
        self.qty = qty
        self.price = price

    def get_data(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Quantity:", self.qty)
        print("Price:", self.price)


books = []

print("How many books you want to enter?")
n = int(input())

for i in range(n):
    print("Enter title, author, quantity and price of book", i+1)

    title = input()
    author = input()
    qty = int(input())
    price = float(input())

    books.append(BookStore(title, author, qty, price))

for book in books:
    print(book.title, book.author, book.qty, book.price)
