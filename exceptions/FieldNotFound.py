from colorama import Fore

class FieldNotFound(Exception):
    def __init__(self, message="Phone not found"):
        self.message = f"{Fore.RED}[ERR]{Fore.RESET}" + "Phone not found: " + message
        super().__init__(self.message)