# Name: Pasin Makcharoen # Student ID: 6810545794

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, title, author):
        this_ = Book(title, author)
        self.__books.append(this_)

    def get_book_count(self):
        return len(self.__books)
    
    def display_books(self):
        temp_ = []
        for a in self.__books:
            temp_.append(f"{a.title} by {a.author}")
        return temp_
    
lib_ = Library()

while True:
    in_ = input("Command (add/view/count/exit): ").strip().lower()
    
    if in_ == "add":
        ti_ = input("Enter title: ")
        auth_ = input("Enter author: ")

        lib_.add_book(ti_, auth_)
        print("Book added.")

    elif in_ == "view":
        print("--- Library Holdings ---")

        db = lib_.display_books()
        for i in db:
            print(i)

        print("------------------------")

    elif in_ == "count":
        print(f"Book count: {lib_.get_book_count()}")

    elif in_ == "exit":
        print("Goodbye.")
        break

    else:
        print("Invalid command.")
        continue