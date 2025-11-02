from classes.logger import Logger
from classes.system_admin import SystemAdmin


class Library:
    '''Managing borrowing and returning books'''
    max_borrow_days=int(14)
    def __init__(self,books:dict[str, Book], users:dict[str,User]):
        self.books=books
        self.users=users
    def register_user(self, user:User) -> None:
        print(user)
        print(self.users)
        self.users[user.user_id]=user
    def add_book(self,book:Book):
        self.books[book.isbn] =book
    def perform_borrow(self,user_id:str,isbn:str):
        if user_id in self.users and isbn in self.books:
            self.books[book.is_available]= False
            self.users[user.borrowed_books] = isbn
            Logger.log_action("Borrowing", self.books)
            SystemAdmin.update_transactions_count()
        print("the name/book not in the system...")

    def perform_return(self,user_id:str,isbn:str):
        if user_id in self.users and isbn in self.books:
            if self.books[book.is_available]== False:
                self.books[book.is_available]= True
                self.users[user.borrowed_books] = isbn
                Logger.log_action("Return", self.books)
                SystemAdmin.update_transactions_count()
        print("the name/book not in the system...")
