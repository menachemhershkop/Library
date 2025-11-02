class Library:
    '''Managing borrowing and returning books'''
    max_borrow_days=int(14)
    def __init__(self,books:dict[str, Book], users:dict[str,User]):
        self.books=books
        self.users=users
    def register_user(self, user:User) -> None:
        pass
    def add_book(self,book:Book):
        pass
    def perform_borrow(self,user_id:str,isbn:str):
        pass
    def perform_return(self,user_id:str,isbn:str):
        pass
