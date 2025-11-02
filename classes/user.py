class User:
    '''User card'''
    def __init__(self,user_id, name,borrowed_books:list[Book]):
        self.user_id=str(user_id)
        self.name=str(name)
        self.borrowed_books=borrowed_books
        # return {"user":self.user_id,"name":self.name,"borrowed books":self.borrowed_books}
    def borrow_book(self,book:Book):
        self.borrowed_books=book
    def return_book(self,book:Book):
        self.borrowed_books.remove(book)
