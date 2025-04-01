from colorama import Fore

class PhoneAlreadyOwned(Exception):
    def __init__(self, message="Phone already owned"):
        self.message = f"{Fore.RED}[ERR]{Fore.RESET}" + message
        super().__init__(self.message)