'''
    ### **Phase 1: Basic Structure (Week 1-2)**
        **Goal:** Create the basic structure of the system using classes and objects.

        1. **Create a `Book` class:**
        - Attributes: `title`, `author`, `isbn`, `is_available` (boolean).
        - Methods: `check_out()`, `return_book()`.
'''

class Book:
    def __init__(self, author, title, isbn):
        self.author = author 
        self.title = title 
        self.isbn = isbn
        self.is_available = True 

    def check_out(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        self.is_available = True

    def __str__(self):
        return f"Book: {self.title} by {self.author} (ISBN: {self.isbn})"