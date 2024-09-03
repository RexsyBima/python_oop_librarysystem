from dataclasses import dataclass
import csv
from typing import Dict
from datetime import datetime, timedelta
@dataclass
class Book: 
    id : int
    title : str 
    author : str
    count : int
    borrowable : bool = True
    return_dates : Dict[int, datetime] = None
 
    def __post_init__(self):
        if self.return_dates is None:
            self.return_dates = {}
        self.id = int(self.id)
        self.count = int(self.count)
        
    def set_return_date(self, user_id : int, days_to_borrow = 7):
        return_date = datetime.today() + timedelta(days=days_to_borrow)
        self.return_dates[user_id] = return_date
        return return_date
    
    def get_return_date(self, user_id : int):
        return self.return_dates.get(user_id, None)
    
    @staticmethod
    def read_books():
        with open("books.csv", "r") as f:
            reader = csv.DictReader(f)
            books = list(reader)
            return [Book(**b) for b in books]
    