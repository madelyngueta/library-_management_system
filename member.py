class Member:
    def __init__(self, member_id, name):
        self._member_id = member_id
        self._name = name
        self._borrowed_books = []
    
    @property
    def member_id(self):
        return self._member_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def borrowed_books(self):
        return self._borrowed_books.copy()  
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
    
    def add_borrowed_book(self, book_id):
        self._borrowed_books.append(book_id)
    
    def remove_borrowed_book(self, book_id):
        if book_id in self._borrowed_books:
            self._borrowed_books.remove(book_id)
    
    def __str__(self):
        return f"ID: {self._member_id} | Name: {self._name} | Books: {len(self._borrowed_books)}"