from dataclasses import dataclass, field
from book import Book
@dataclass
class User:
    id : int
    name : str
    book_limit : int = 3
    book_borrowed : list[Book] = field(default_factory=list)    
    def __post_init__(self):
        assert self.id >= 0
        assert len(self.name) > 0, "Name cannot be empty"
        assert self.book_limit == 3
        
    def borrow_book(self, book : Book):
        if book.borrowable:
            self.book_borrowed.append(book)
            self.book_limit -= 1
            book.count -= 1
        else:
            print("Book not available to borrow!")
        book.borrowable = False if book.count == 0 else True
        
                    
    def return_book(self, book : Book):
        if book in self.book_borrowed:
            self.book_borrowed.remove(book)
            self.book_limit += 1
            book.count += 1
        else:
            print("Book not borrowed!")

    @property
    def get_book_borrowed(self):
        return self.book_borrowed
    