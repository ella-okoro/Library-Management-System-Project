'''
    ### **Phase 1: Basic Structure (Week 1-2)**
        **Goal:** Create the basic structure of the system using classes and objects.

        2. **Create a `Member` class:**
        - Attributes: `name`, `member_id`, `borrowed_books` (list of books).
        - Methods: `borrow_book(book)`, `return_book(book)`.
'''
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