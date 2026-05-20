from book import Book
from member import Member
from loan import Loan
from exceptions import *

class LibraryService:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.loans = []
    
    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise BookAlreadyExistsError(f"Book ID {book_id} already exists")
        self.books[book_id] = Book(book_id, title, author)
        return "Book added successfully"
    
    def register_member(self, member_id, name):
        if member_id in self.members:
            raise InvalidInputError(f"Member ID {member_id} already exists")
        self.members[member_id] = Member(member_id, name)
        return "Member registered successfully"
    
    def borrow_book(self, book_id, member_id):
        if book_id not in self.books:
            raise BookNotFoundError(f"Book ID {book_id} not found")
        if member_id not in self.members:
            raise MemberNotFoundError(f"Member ID {member_id} not found")
        if not self.books[book_id].is_available:
            raise BookUnavailableError(f"Book '{self.books[book_id].title}' is already borrowed")
        
        self.books[book_id].is_available = False  # Uses setter
        self.members[member_id].add_borrowed_book(book_id)  # Uses method
        self.loans.append(Loan(book_id, member_id))
        return f"Book '{self.books[book_id].title}' borrowed by {self.members[member_id].name}"
    
    def return_book(self, book_id):
        if book_id not in self.books:
            raise BookNotFoundError(f"Book ID {book_id} not found")
        if self.books[book_id].is_available:
            raise BookUnavailableError(f"Book '{self.books[book_id].title}' is not borrowed")
        
        self.books[book_id].is_available = True  # Uses setter
        # Optional: remove from member's borrowed_books
        for member in self.members.values():
            if book_id in member.borrowed_books:
                member.remove_borrowed_book(book_id)
                break
        
        return f"Book '{self.books[book_id].title}' returned successfully"
    
    def view_books(self):
        if not self.books:
            return "No books in library"
        return "\n".join(str(book) for book in self.books.values())
    
    def view_members(self):
        if not self.members:
            return "No members registered"
        return "\n".join(str(member) for member in self.members.values())
    
    def view_loans(self):
        if not self.loans:
            return "No loan records"
        return "\n".join(str(loan) for loan in self.loans)