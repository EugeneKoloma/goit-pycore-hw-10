from contextlib import contextmanager
from colorama import Fore
from .entities import AddressBook
import sys

@contextmanager
def book_cxt_mngr():
    try:
        yield AddressBook()
    except Exception as error:
        raise error
    finally:
        sys.exit(0)