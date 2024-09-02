from dataclasses import dataclass
@dataclass
class Book:
    id : int
    title : str
    author : str
    count : int
    borrowable : bool = True

    def __post_init__(self):
        self.count = int(self.count)
        self.id = int(self.id)
        
        assert self.count >= 0
        assert self.id >= 0
        
    @property
    def is_borrowable(self):
        return self.borrowable
    
    @is_borrowable.setter
    def is_borrowable(self, value : bool):
        self.borrowable = value
    
    @staticmethod
    def get_books():
        output = {}
        import csv
        with open('books.csv', 'r') as f:
            reader = csv.DictReader(f)
            books = [Book(**d) for d in list(reader)]
        for i, item in enumerate(books, start=1):
            output[i] = item
        return output