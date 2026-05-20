class Book:
    def __init__(self, book_id, title, author):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._is_available = True
    
    @property
    def book_id(self):
        return self._book_id
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def is_available(self):
        return self._is_available
    
    # Setters
    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        self._title = value
    
    @author.setter
    def author(self, value):
        if not value:
            raise ValueError("Author cannot be empty")
        self._author = value
    
    @is_available.setter
    def is_available(self, value):
        if not isinstance(value, bool):
            raise ValueError("Availability must be True or False")
        self._is_available = value
    
    def __str__(self):
        status = "Available" if self._is_available else "Borrowed"
        return f"ID: {self._book_id} | {self._title} by {self._author} [{status}]"