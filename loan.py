from datetime import datetime

class Loan:
    def __init__(self, book_id, member_id):
        self._book_id = book_id
        self._member_id = member_id
        self._borrow_date = datetime.now()
        self._return_date = None
    
    @property
    def book_id(self):
        return self._book_id
    
    @property
    def member_id(self):
        return self._member_id
    
    @property
    def borrow_date(self):
        return self._borrow_date
    
    @property
    def return_date(self):
        return self._return_date
    
    @return_date.setter
    def return_date(self, value):
        if value and not isinstance(value, datetime):
            raise ValueError("Return date must be a datetime object")
        self._return_date = value
    
    def __str__(self):
        returned = self._return_date.strftime('%Y-%m-%d') if self._return_date else "Not returned"
        return f"Book ID: {self._book_id} | Member ID: {self._member_id} | Borrowed: {self._borrow_date.strftime('%Y-%m-%d')} | Returned: {returned}"