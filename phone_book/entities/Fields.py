import re
from exceptions import WrongPhoneNumber, WrongDateFormat

class Field:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)
    
class Name(Field):
    pass

class Phone(Field):
    __phone_pattern = re.compile(r"^\+?3?8?(0\d{9})$|^0\d{9}$")

    @staticmethod
    def validate_phone_number(phone_number):
        return bool(Phone.__phone_pattern.match(phone_number))
    
    def __init__(self, phone: str):
        self.value = phone

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_phone):
        if not Phone.validate_phone_number(new_phone):
            raise WrongPhoneNumber(f"Wrong phone number {new_phone}.")
        self._value = new_phone

class Birthday(Field):
    date_format_pattern = re.compile(r"^\d{2}\.\d{2}\.\d{4}$")

    @staticmethod
    def validate_date(date: str) -> bool:
        return bool(Birthday.date_format_pattern.match(date))

    def __init__(self, date: str):
        self.value = date
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, date: str):
        if not Birthday.validate_date(date):
            raise WrongDateFormat(f"Wrong date format {date}")
        self._value = date