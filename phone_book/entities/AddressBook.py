from collections import UserDict
from .Records import Record
from datetime import datetime as dtdt, timedelta as td
from .Fields import Birthday
from typing import Dict

class AddressBook(UserDict):
    def __init__(self):
        self.data: Dict[str, Record] = {}

    def add_record(self, record: Record):
        self.data[record.name._value] = record

    def find(self, name: str) -> Record | None:
        if not name in self.data.keys():
            return None
        return self.data[name]
    
    def delete(self, name):
        self.data.pop(name)

    def find_next_week_bithdays(self):
        if not self.data:
            return "Phone book is empty"
        
        date_format_pattern = Birthday.DATE_FORMAT_PATTERN
        upcomming_congrats: list[str] = []
        today = dtdt.today().date()
        next_seven_days = today + td(7)

        def calculate_week_day(date):
            match date.weekday():
                case 5:
                    date = date + td(2)
                case 6:
                    date = date + td(1)
            return date
        
        for record in self.data.values():
            bd = dtdt.strptime(record.birthday.value, date_format_pattern).date()
            bd_with_year = dtdt(year=today.year, month=bd.month, day=bd.day).date()
            congrats_day = None

            if (bd_with_year < today):
                bd_with_year = bd_with_year.replace(year=(today.year + 1))
                
            congrats_day = calculate_week_day(bd_with_year)

            if  congrats_day >= today and congrats_day <= next_seven_days:
                upcomming_congrats.append(f"{record.name._value} at {congrats_day.strftime(date_format_pattern)}")
        
        return "\n".join(upcomming_congrats)
    

    def __str__(self):
        if not self.data:
            return "Phone book is empty"
        return "\n".join(str(record) for record in self.data.values())