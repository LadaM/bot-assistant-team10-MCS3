import colorama
from colorama import Fore

# Initialize colorama
colorama.init(autoreset=True)


class ContactNotFoundError(Exception):
    pass


class ContactAlreadyExistsError(Exception):
    pass


class CommandError(Exception):
    pass


def contact_not_found_error(func):
    def inner(args):
        try:
            return func(args)
        except ContactNotFoundError:
            print(Fore.RED + f"Contact '{args[0]}' wasn't found")

    return inner


def add_contact_error(func):
    def inner(args):
        try:
            return func(args)
        except CommandError:
            print(Fore.RED + "Please use format: add {name} {phone}")
        except ValueError:
            print(
                Fore.RED + "Phone number doesn't match the format XXXXXXXXXX(10 digits)")
        except ContactAlreadyExistsError:
            print(
                Fore.RED + f"Contact with same name and phone number already exists")

    return inner


def delete_contact_error(func):
    def inner(*args):
        try:
            return func(*args)
        except CommandError:
            print(Fore.RED + "Please use format: delete {name}")

    return inner


def change_contact_error(func):
    def inner(args):
        try:
            return func(args)
        except CommandError:
            print(
                Fore.RED + "Please use format: change {name} {old_phone} {new_phone}")
        except ValueError:
            print(
                Fore.RED + "Phone number doesn't match the format XXXXXXXXXX(10 digits)")
        except KeyError:
            print(
                Fore.RED + f"Contact '{args[0].capitalize()}' has not phone number '{args[1]}'")

    return inner


def show_phones_error(func):
    def inner(args):
        try:
            return func(args)
        except CommandError:
            print(Fore.RED + "Please use format: phone {name}")

    return inner


def add_birthday_error(func):
    def inner(args):
        try:
            return func(args)
        except CommandError:
            print(
                Fore.RED + "Please use format: add-birthday {user} {DD.MM.YYYY}")
        except ValueError:
            print(
                Fore.RED + f"'{args[1]}' doesn't match the birthday format DD.MM.YYYY")

    return inner


def show_birthday_error(func):
    def inner(args):
        try:
            return func(args)
        except CommandError:
            print(Fore.RED + "Please use format: show-birthday {user}")
        except ValueError:
            print(Fore.RED + f"Contact has not set birthday yet")

    return inner


def max_period_error(func):
    def inner(args):
        try:
            return func(args)
        except ValueError:
            print(Fore.RED + f"Period should be int between 1 and 365")

    return inner
