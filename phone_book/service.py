from colorama import Fore
from logger.logger import log_warning, log_info
from decorators import error_handler
from .entities import AddressBook, Record
from exceptions import RecordNotFound, FieldNotFound

class PhoneBookService:
    def __init__(self, book):
        self.__book: AddressBook = book

    @property
    def book(self):
        return self.__book
    
    @book.setter
    def book(self, book: AddressBook):
        self.book = book

    @error_handler
    def add_contact(self, args: list[str]):
        name, phone = args
        record = self.book.find(name)
        if record == None:
            new_record = Record(name)
            new_record.add_phone(phone)
            self.book.add_record(new_record)
            log_info(f"Contact {Fore.GREEN}{name.capitalize()}{Fore.RESET} with phone number {Fore.GREEN}{phone}{Fore.RESET} has been added.")
            return
        
        existing_phone = record.find_phone(phone)
        if existing_phone == None:
            record.add_phone(phone)
            log_info(f"New phone number {Fore.GREEN}{phone}{Fore.RESET} was added to {Fore.GREEN}{name.capitalize()}{Fore.RESET}.")
            return
        
        log_warning(f"Contact {Fore.GREEN}{name.capitalize()}{Fore.RESET} already has this number {Fore.GREEN}{phone}{Fore.RESET}")

    @error_handler
    def change_contacts_phone(self, args) -> None:
        name, old_phone, new_phone = args
        record = self.book.find(name)
        if record == None:
            raise RecordNotFound(f"Record not found for name: {Fore.GREEN}{name}{Fore.RESET}")
        
        phone = record.find_phone(old_phone)
        if phone == None:
            raise FieldNotFound(f"Phone number {Fore.GREEN}{new_phone}{Fore.RESET} not exist. " /
                                f"U can add it by using [{Fore.CYAN}add{Fore.RESET}] command, type help for more info.")
        
        phone.value = new_phone
        log_info(f"Contact {Fore.GREEN}{name.capitalize()}{Fore.RESET} has been updated with new phone number {Fore.GREEN}{phone}{Fore.RESET}.")
        

    @error_handler
    def show_contacts_phones(self, args):
        name = args[0]
        record = self.book.find(name)
        if record == None:
            raise RecordNotFound(f"Record not found with name: {Fore.GREEN}{name}{Fore.RESET}")
        
        print(self.book())

    @error_handler
    def set_birthday(self, args):
        name, date = args
        record = self.book.find(name)
        if record == None:
            raise RecordNotFound(f"Record not found with name: {Fore.GREEN}{name}{Fore.RESET}")
        # add Jane +380991112233
        # add-birthday Jane 03.04.2025
        # show-birthday Jane
        record.add_birthday(date)
        log_info(f"Contact's {Fore.GREEN}{name.capitalize()}{Fore.RESET} birthday was updated: {Fore.GREEN}{date}{Fore.RESET}.")

    @error_handler
    def get_birthday(self, args):
        name = args[0]
        record = self.book.find(name)
        if record == None:
            raise RecordNotFound(f"Record not found with name: {Fore.GREEN}{name}{Fore.RESET}")

        if record.birthday == None:
            log_warning(f"{Fore.GREEN}{name.capitalize()}{Fore.RESET} has not birthday setted.")

        log_info(f"{Fore.GREEN}{name.capitalize()}{Fore.RESET} has a birthday at: {Fore.GREEN}{str(record.birthday)}{Fore.RESET}")
    
    @error_handler
    def show_next_week_birthdays(self):
        self.book.find_next_week_bithdays()

    @error_handler
    def show_all_contacts(self):
        print(self.book)