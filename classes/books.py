class Book:
    '''Books in the library'''
    def __init__(self,title,author, isbn, is_available: bool = True):
        self.title=str(title)
        self.author=str(author)
        self.isbn=str(isbn)
        self.is_available=is_available
    def get_details(self)-> str:
        return f'Name book: {self.title}, author: {self.author},number ID: {self.isbn} available: {self.is_available}'
