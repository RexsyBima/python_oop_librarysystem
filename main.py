from book import Book
from user import User

def main():

    user1 = User(1, "John")
    user2 = User(2, "Jane")
    user3 = User(3, "Mike")
    user4 = User(4, "Sarah")

    
if __name__ == "__main__":
    books = Book.get_books()
    print(books)