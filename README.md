# Library-Management-System-Project
I am working on this project to become more confident in my OOP coding, as I mainly use functional programming in school. I asked Deepseek AI to help me come up with a project that I can work on to for the next 14 weeks that will allow me to enhance my OOP programming skills. 





This is a **semester-long project** that will help me practice OOP concepts like **classes, objects, inheritance, encapsulation, polymorphism, and abstraction**. The project is broken into phases, so I can build on my skills as I progress.

---

## **Project: Library Management System**

### **Overview**
You’ll create a **Library Management System** that allows users to manage books, members, and borrowing activities. This project will help you practice OOP principles while building a functional application.

---

### **Phase 1: Basic Structure (Week 1-2)**
**Goal:** Create the basic structure of the system using classes and objects.

1. **Create a `Book` class:**
   - Attributes: `title`, `author`, `isbn`, `is_available` (boolean).
   - Methods: `check_out()`, `return_book()`.

2. **Create a `Member` class:**
   - Attributes: `name`, `member_id`, `borrowed_books` (list of books).
   - Methods: `borrow_book(book)`, `return_book(book)`.

3. **Create a `Library` class:**
   - Attributes: `books` (list of books), `members` (list of members).
   - Methods: `add_book(book)`, `add_member(member)`, `find_book(isbn)`, `find_member(member_id)`.

---

### **Phase 2: Inheritance and Encapsulation (Week 3-4)**
**Goal:** Extend the system using inheritance and encapsulation.

1. **Create a `StaffMember` class (inherits from `Member`):**
   - Add an attribute: `staff_id`.
   - Add a method: `add_book_to_library(library, book)` (allows staff to add books to the library).

2. **Encapsulate attributes:**
   - Make attributes private (e.g., `__isbn` for `Book`) and use getters and setters to access them.

---

### **Phase 3: Polymorphism and Abstraction (Week 5-6)**
**Goal:** Use polymorphism and abstraction to make the system more flexible.

1. **Create an abstract class `Person`:**
   - Attributes: `name`, `id`.
   - Abstract method: `display_info()`.

2. **Refactor `Member` and `StaffMember` to inherit from `Person`.**
   - Implement `display_info()` in both classes.

3. **Add a `Transaction` class:**
   - Attributes: `book`, `member`, `transaction_date`.
   - Method: `display_transaction()`.

---

### **Phase 4: Advanced Features (Week 7-8)**
**Goal:** Add advanced features to the system.

1. **Add a `Fine` class:**
   - Attributes: `member`, `book`, `due_date`, `fine_amount`.
   - Method: `calculate_fine()`.

2. **Add a `Search` class:**
   - Methods: `search_by_title(title)`, `search_by_author(author)`.

3. **Add a `Report` class:**
   - Methods: `generate_borrowed_books_report()`, `generate_overdue_books_report()`.

---

### **Phase 5: User Interface (Week 9-10)**
**Goal:** Create a simple command-line interface (CLI) for the system.

1. **Create a `LibraryCLI` class:**
   - Methods: `display_menu()`, `handle_choice(choice)`.
   - Allow users to:
     - Add books and members.
     - Borrow and return books.
     - Search for books.
     - Generate reports.

2. **Use a loop to keep the program running until the user chooses to exit.**

---

### **Phase 6: Testing and Refactoring (Week 11-12)**
**Goal:** Test your code and refactor for better design.

1. **Write unit tests for each class and method.**
   - Use Python’s `unittest` module.

2. **Refactor your code:**
   - Ensure all classes follow the Single Responsibility Principle.
   - Remove duplicate code and improve readability.

---

### **Phase 7: Final Touches (Week 13-14)**
**Goal:** Add final features and polish the project.

1. **Save data to a file:**
   - Use Python’s `pickle` or `json` module to save library data (books, members, transactions) to a file.

2. **Load data from a file:**
   - Load saved data when the program starts.

3. **Add error handling:**
   - Handle invalid user inputs gracefully.

---

### **Bonus Features (Optional)**
- Add a GUI using `tkinter` or `PyQt`.
- Add a database (e.g., SQLite) to store data.
- Implement a web-based interface using Flask or Django.

---

### **How to Proceed**
1. Start with Phase 1 and build incrementally.
2. Test each phase thoroughly before moving to the next.
3. Experiment with new features and refactor as you learn more.
