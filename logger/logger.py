from colorama import Fore

def log_info(message):
    print(f"{Fore.GREEN}[INFO]: {Fore.RESET}{message}")

def log_error(message):
    print(f"{Fore.RED}[ERROR]: {Fore.RESET}{message}")

def log_warning(message):
    print(f"{Fore.YELLOW}[WARNING]: {Fore.RESET}{message}")

if __name__ == "__main__":
    log_info("This is an info message.")
    log_error("This is an error message.")
    log_warning("This is a warning message.")