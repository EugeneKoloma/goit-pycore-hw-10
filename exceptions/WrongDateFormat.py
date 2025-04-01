from colorama import Fore

class WrongDateFormat(Exception):
    def __init__(self, message="Wrong date format."):
        self.message = f"{Fore.RED}[ERROR]{Fore.RESET} " + message + " Example: 01.01.2025 ~ DD.MM.YYYY"
        super().__init__(self.message)