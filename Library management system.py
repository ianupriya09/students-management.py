class Library:
    def __init__(self):
        self.books = []          # list of all books
        self.borrowed = {}       # book : student

    def add_book(self):
        book = input("Enter book name: ")
        self.books.append(book)
        print("Book added!\n")

    def display_books(self):
        if not self.books:
            print("No books available\n")
            return
        print("\nAvailable Books:")
        for b in self.books:
            print("-", b)
        print()

    def borrow_book(self):
        book = input("Enter book name to borrow: ")
        student = input("Your name: ")

        if book not in self.books:
            print("Error: Book is not available!\n")
        else:
            self.books.remove(book)
            self.borrowed[book] = student
            print("Book borrowed!\n")

    def return_book(self):
        book = input("Enter book name to return: ")

        if book not in self.borrowed:
            print("Error: This book was not borrowed!\n")
        else:
            self.books.append(book)
            del self.borrowed[book]
            print("Book returned!\n")


lib = Library()

while True:
    print("1.Add  2.Display  3.Borrow  4.Return  5.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        lib.add_book()
    elif ch == "2":
        lib.display_books()
    elif ch == "3":
        lib.borrow_book()
    elif ch == "4":
        lib.return_book()
    elif ch == "5":
        break
    else:
        print("Invalid choice\n")
        