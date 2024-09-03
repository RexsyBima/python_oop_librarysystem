from book import Book
from user import User
import csv, time

def read_csv():
    with open("books.csv", "r") as f:
        reader = csv.DictReader(f)
        book1 = list(reader)[0]
        obj_book1 = Book(**book1)
        print(obj_book1)            
        return obj_book1
            

            
def main():
    user1 = User(1,"user1")
    user2 = User(2,"user2")
    user3 = User(3,"user3")
    user4 = User(4,"user4")
    
    books = Book.read_books()
    book1 = books[0]
    user1.borrow_book(book1)
    print(user1.book_borrowed)
    
    user1.return_book(book1)



"""
    user1.borrow_book(book1)
    print(book1.count)
    print(user2.book_borrowed)
    user2.borrow_book(book1)
    user3.borrow_book(book1)
"""    

        


if __name__ == "__main__":
    main()    
    #read_csv()
    #print(Book.read_books())