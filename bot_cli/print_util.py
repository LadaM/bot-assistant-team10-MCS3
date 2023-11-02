import colorama
from colorama import Fore

# Initialize colorama
colorama.init(autoreset=True)


def print_error(msg: str):
    print(Fore.RED + msg)


def print_success(msg: str):
    print(Fore.GREEN + msg)


def print_info(msg: str):
    print(Fore.BLUE + msg)


def print_warn(msg: str):
    print(Fore.YELLOW + msg)


def print_magenta(msg: str):
    print(Fore.MAGENTA + msg)
