from classes.books import Book
from classes.library import Library
from classes.user import User
if __name__=='__main__':
    book1=Book("tofet", "gersonovitz", "1234")
    book2=Book("aisterk","m.kinan", "5678")
    book=Book("sodot", "rozen","7890")
    user1=User("dan123","daniel",[])
    user2=User("menu567","menacehm", [])
    library=Library
    library.register_user(user1)