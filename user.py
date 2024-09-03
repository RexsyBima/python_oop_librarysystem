from book import Book
from dataclasses import dataclass, field
import csv, datetime
@dataclass
class User:
    id : int
    name : str
    book_limit : int = 3
    book_borrowed : list[Book] = field(default_factory=list)
        
    def borrow_book(self, book : Book):
        """ 
        idea :
        1. if book is borrowable and user can borrow more book:
            then borrow book
            then reduce count of book
            then check if book == 0, book is not borrowable
        """
        if book.borrowable and self.book_limit > 0 and book not in self.book_borrowed:
            now = datetime.datetime.now()
            return_date = now + datetime.timedelta(days=7)
            self.book_borrowed.append(book)
            book.count -= 1
            if book.count == 0:
                book.borrowable = False
            self.book_limit -= 1
            book.set_return_date(self.id, days_to_borrow=7)
            print(f"{book.title} is borrowed by {self.name}!, book must be returned before {return_date}")
        elif book.borrowable is False:
            print(f"book {book.title} is not borrowable, because it is not available")
        elif self.book_limit == 0:
            print(f"User {self.name} can't borrow any book because he/she is already in limit")
        elif book in self.book_borrowed:
            print(f"User {self.name} can't borrow book {book.title} because he/she already borrowed it")
    
    def return_book(self, book : Book):
        if book in self.book_borrowed:
            self.book_borrowed.remove(book)
            book.count += 1
            self.book_limit += 1
            book.borrowable = True if book.count > 0 else False
            book_return_date = book.get_return_date(self.id)
            if book_return_date > datetime.datetime.now():
                print(f"This book is returned on time")
            else:
                print(f"This book is returned not on time")
            print(f"{book.title} is returned by {self.name}!")
        
        else:
            print(f"User {self.name} can't return book {book.title} because he/she doesn't have it")
            
    @staticmethod
    def read_users():
        with open("users.csv", "r") as f:
            reader = csv.DictReader(f)
            users = list(reader)
            return [User(**u) for u in users]   