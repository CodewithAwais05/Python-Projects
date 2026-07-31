import json
import os

BOOKS_DATA = "books.json"

if os.path.exists(BOOKS_DATA):
    with open(BOOKS_DATA, "r") as file:
        Books = json.load(file)
else:
    Books = {}

class Book:

    def __init__(self):
        self.book_id = ""
        self.title = ""
        self.author = ""
        self.publisher = ""
        self.category = ""
        self.edition = ""
        self.publication_year = ""
        self.isbn = ""
        self.total_copies = 0
        self.available_copies = 0
        self.status = ""

    def create_book(self):
        self.book_id = input("Enter Book ID:  ")
        self.title = input("Enter book Title:  ")
        self.author = input("Enter Author name:  ")
        self.publisher = input("Enter Publisher name:  ")
        self.category = input("Enter book Category:  ")
        self.edition = input("Enter book Edition:  ")
        self.publication_year = input("Enter Publication Year:  ")
        self.isbn = input("Enter ISBN:  ")
        self.total_copies = int(input("Enter total copies:  "))
        self.available_copies = self.total_copies
        self.status = "Available"

        Books[self.book_id] = self.to_dict()
        print("Book Record created!")

    def to_dict(self):
        return{
            "book_id" : self.book_id,
            "title" : self.title,
            "author" : self.author,
            "publisher" : self.publisher,
            "category" : self.category,
            "edition" : self.edition,
            "publication_year" : self.publication_year,
            "isbn" : self.isbn,
            "total_copies" : self.total_copies,
            "available_copies" : self.available_copies,
            "status" : self.status
        }

class Library:

    def add_book(self):
        book = Book()
        book.create_book()
        self.save_books()

    def update_book(self):
        bookId = input("Enter Book ID:  ")

        if bookId not in Books:
            print("Book not found!")
            return
        
        print("\n1. Change Author")
        print("2. Change Title")
        print("3. Change Publisher")
        print("4. Increase Copies")
        choice = int(input("Enter your choice:  "))

        if choice == 1:
            Books[bookId]["author"] = input("Enter new Author:  ")
        elif choice == 2:
            Books[bookId]["title"] = input("Enter new Title:  ")
        elif choice == 3:
            Books[bookId]["publisher"] = input("Enter new Publisher:  ")
        elif choice == 4:
            new_copies = int(input("Enter number of new copies:  "))
            Books[bookId]["total_copies"] += new_copies
            Books[bookId]["available_copies"] += new_copies
            Books[bookId]["status"] = "Available"
        else:
            print("Invalid Choice!")
            return
        print("Book updated successfully!")

        self.save_books()

    def delete_book(self):
        bookId = input("Enter Book ID:  ")
        if bookId in Books:
            del Books[bookId]
            print("Book deleted successfully!")
        else:
            print("Book not found!")

        self.save_books()

    def display_book(self):
        bookId = input("Enter Book ID:  ")
        if bookId not in Books:
            print("Book not found!")
            return

        book = Books[bookId]
        print("=============== BOOK DETAILS ===============")
        print("Book ID:                  ", book["book_id"])
        print("Book Title:               ", book["title"])
        print("Book Author:              ", book["author"])
        print("Book Publisher:           ", book["publisher"])
        print("Book Category:            ", book["category"])
        print("Book Edition:             ", book["edition"])
        print("Publication Year:         ", book["publication_year"])
        print("ISBN:                     ", book["isbn"])
        print("Total Copies:             ", book["total_copies"])
        print("Available Copies:         ", book["available_copies"])
        print("Book Status:              ", book["status"])

    def borrow_book(self):
        bookId = input("Enter Book ID tp borrow:  ")
        if bookId not in Books:
            print("Book not found!")
            return
        
        if Books[bookId]["available_copies"] > 0:
            Books[bookId]["available_copies"] -= 1
            if Books[bookId]["available_copies"] == 0:
                Books[bookId]["status"] = "Not Available"
            print("Book borrowed successfully!")
        else:
            print("Book is not Available!")

        self.save_books()

    def return_book(self):
        bookId = input("Enter Book ID to return:  ")
        if bookId not in Books:
            print("Book not found!")
            return
        
        if Books[bookId]["available_copies"] < Books[bookId]["total_copies"]:
            Books[bookId]["available_copies"] += 1
            Books[bookId]["status"] = "Available"

            print("Book returned successfully!")
        else:
            print("All copies are already in the Library!")

        self.save_books()

    def save_books(self):
        with open(BOOKS_DATA, "w") as file:
            json.dump(Books, file, indent=4)
        print("Record saved successfully!!!")

def main():
    library = Library()
    while True:
        print("1. Add Book Record")
        print("2. Display Book Record")
        print("3. Update Book Record")
        print("4. Delete Book Record")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        choice = int(input("Enter your Choice:  "))

        if choice == 1:
            library.add_book()
        elif choice == 2:
            library.display_book()
        elif choice == 3:
            library.update_book()
        elif choice == 4:
            library.delete_book()
        elif choice == 5:
            library.borrow_book()
        elif choice == 6:
            library.return_book()
        elif choice == 7:
            print("===============================")
            print("            EXITING            ")
            print("===============================")
            break
        else:
            print("Invalid Choice!!!")
if __name__ == "__main__":
    main()
