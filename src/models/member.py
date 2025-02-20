'''
    ### **Phase 1: Basic Structure (Week 1-2)**
        **Goal:** Create the basic structure of the system using classes and objects.

        2. **Create a `Member` class:**
        - Attributes: `name`, `member_id`, `borrowed_books` (list of books).
        - Methods: `borrow_book(book)`, `return_book(book)`.
'''
from .book import Book

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.check_out():
            self.borrowed_books.append(book)
            return True 
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"
    

'''
    ### **Phase 2: Inheritance and Encapsulation (Week 3-4)**
    **Goal:** Extend the system using inheritance and encapsulation.

    1. **Create a `StaffMember` class (inherits from `Member`):**
    - Add an attribute: `staff_id`.
    - Add a method: `add_book_to_library(library, book)` (allows staff to add books to the library).

    2. **Encapsulate attributes:**
    - Make attributes private (e.g., `__isbn` for `Book`) and use getters and setters to access them.

    ---
'''

class StaffMember(Member):
    def __init__(self, name, member_id, staff_id):
        super().__init__(name, member_id)
        self.staff_id = staff_id

    def add_book_to_library(self, library, book: Book):
        library.add_book(book)
    
    def __str__(self):
        return f"Staff Member: {self.name} (ID: {self.member_id}, Staff ID: {self.staff_id})"