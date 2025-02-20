from models.book import Book
from models.member import Member
from models.library import Library

def main():
    # Create a library
    library = Library()

    # Add a book
    book1 = Book("Python Programming", "John Doe", "123456789")
    library.add_book(book1)

    # Add a member
    member1 = Member("Alice", "M001")
    library.add_member(member1)

    # Borrow a book
    member1.borrow_book(book1)

    # Display library status
    print(library)
    print(book1)
    print(member1)

if __name__ == "__main__":
    main()