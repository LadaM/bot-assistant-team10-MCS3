from print_util import print_error


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
            print_error(f"Contact '{args[0]}' wasn't found")

    return inner


def add_contact_error(func):
    def inner(args):
        try:
            return func(args)
        except CommandError:
            print_error("Please use format: add {name} {phone}")
        except ValueError:
            print_error("Phone number doesn't match the format XXXXXXXXXX(10 digits)")
        except ContactAlreadyExistsError:
            print_error(f"Contact with same name and phone number already exists")

    return inner


def delete_contact_error(func):
    def inner(*args):
        try:
            return func(*args)
        except CommandError:
            print_error("Please use format: delete {name}")

    return inner


def change_contact_error(func):
    def inner(args):
        try:
            return func(args)
        except CommandError:
            print_error("Please use format: change {name} {old_phone} {new_phone}")
        except ValueError:
            print_error("Phone number doesn't match the format XXXXXXXXXX(10 digits)")
        except KeyError:
            print_error(f"Contact '{args[0].capitalize()}' has not phone number '{args[1]}'")

    return inner


def search_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except CommandError:
            print_error("Invalid search string. Expecting string at least 2 characters long!")

    return inner


def show_phones_error(func):
    def inner(args):
        try:
            return func(args)
        except CommandError:
            print_error("Please use format: phone {name}")

    return inner


def add_birthday_error(func):
    def inner(args):
        try:
            return func(args)
        except CommandError:
            print_error("Please use format: add-birthday {user} {DD.MM.YYYY}")
        except ValueError:
            print_error(f"'{args[1]}' doesn't match the birthday format DD.MM.YYYY")

    return inner


def show_birthday_error(func):
    def inner(args):
        try:
            return func(args)
        except CommandError:
            print_error("Please use format: show-birthday {user}")
        except ValueError:
            print_error(f"Contact has not set birthday yet")

    return inner


def max_period_error(func):
    def inner(args):
        try:
            return func(args)
        except ValueError:
            print_error(f"Period should be int between 1 and 365")

    return inner


def add_address_error(func):
    def inner(args):
        try:
            return func(args)
        except CommandError:
            print_error("Please use format: add-address {user} {address}")
        except ValueError:
            print_error("Address must be at least 5 symbols")

    return inner


def show_address_error(func):
    def inner(args):
        try:
            return func(args)
        except CommandError:
            print_error("Please use format: show-address {user}")
        except ValueError:
            print_error(f"Contact has not set address yet")

    return inner
