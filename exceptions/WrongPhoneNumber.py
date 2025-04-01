from colorama import Fore

class WrongPhoneNumber(Exception):
    def __init__(self, message="Wrong number."):
        self.message = f"{Fore.RED}[ERROR]{Fore.RESET} " + message + " Example: +380112223344"
        super().__init__(self.message)