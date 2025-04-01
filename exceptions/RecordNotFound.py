from colorama import Fore

class RecordNotFound(Exception):
    def __init__(self, message="Record not found"):
        self.message = f"{Fore.RED}[ERR]{Fore.RESET}" + message
        super().__init__(self.message)