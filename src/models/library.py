'''
    ### **Phase 1: Basic Structure (Week 1-2)**
        **Goal:** Create the basic structure of the system using classes and objects.

        3. **Create a `Library` class:**
        - Attributes: `books` (list of books), `members` (list of members).
        - Methods: `add_book(book)`, `add_member(member)`, `find_book(isbn)`, `find_member(member_id)`.

        ---
'''
from .member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    def __str__(self):
        return f"Library: {len(self.books)} books, {len(self.members)} members"