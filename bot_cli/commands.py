from address_book_classes import Name, Phone, Birthday, Record, AddressBook
from error_handlers import add_contact_error, delete_contact_error, change_contact_error, show_phones_error, contact_not_found_error, add_birthday_error, show_birthday_error, CommandError, ContactAlreadyExistsError, ContactNotFoundError
import os.path
import colorama
from colorama import Fore


# Initialize colorama
colorama.init(autoreset=True)

book: AddressBook
FILE_PATH = "contacts.json"


commands: dict = {
    "help": "shows available commands",
    "hello": "prints 'How can I help you?'",
    "add {user} {phone}": "adds a contact with phone",
    "delete {user}": "deletes contact",
    "change {user} {old_phone} {new_phone}": "changes exist contact's phone number",
    "phone {user}": "shows exist contact's phone numbers",
    "all": "shows all exist contacts",
    "add-birthday {user} {birthday}": "adds birthday to a contact in format [DD.MM.YYYY]",
    "show-birthday {user}": "shows contact's birthday date",
    "birthdays": "shows birthdays on next week",
    "exit": "enter 'close' or 'exit' to close the assistant",
}


def help():
    """
    Prints out available commands
    prints list of bot commands
    """
    sorted_commands = dict(sorted(commands.items(), key=lambda item: item[0]))
    formatted_commands = ""

    for key, value in sorted_commands.items():
        formatted_commands += f">>> {key: <40}: {value: <}\n"

    print(Fore.MAGENTA + formatted_commands)


def parse_input(user_input: str):
    """
    Parse input command
    Prints available commands in case of empty input
    @return - command and arguments
    """
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
    except:
        return "help", ""

    return cmd, *args


@add_contact_error
def add_contact(args: list[str, str]):
    """
    adds a new contact with phone number
    or adds a new phone number to exist contact
    prints command result
    """
    try:
        name, phone = args
        name = Name(name)
    except:
        raise CommandError

    try:
        phone = Phone(phone)
    except:
        raise ValueError

    if book.find(name):
        contact = book.find(name)

        if not phone.value in contact.get_phones():
            record: Record = contact.add_phone(phone)
        else:
            raise ContactAlreadyExistsError
    else:
        record: Record = Record(name, phone)
        book.add_record(record)

    book.save_contacts(FILE_PATH)
    print(Fore.GREEN +
          f"Contact added successfully: {name} {phone}")


@contact_not_found_error
@delete_contact_error
def delete_contact(args):
    """
    delete exist contact
    prints command result
    """
    try:
        name = Name(args[0])
    except:
        raise CommandError

    if (book.find(name)):
        book.delete(name)
    else:
        raise ContactNotFoundError

    book.save_contacts(FILE_PATH)
    print(Fore.GREEN + f"Contact '{name}' deleted successfully")


@contact_not_found_error
@change_contact_error
def change_contact(args: list[str, str, str]):
    """
    change exist contact phone number on new one
    prints command result
    """
    try:
        name, old_phone, new_phone = args
        name = Name(name)
    except:
        raise CommandError
    try:
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)
    except:
        raise ValueError

    if book.find(name):
        record: Record = book.find(name)

        if old_phone.value in record.get_phones():
            record.edit_phone(old_phone, new_phone)
        else:
            raise KeyError

        book.save_contacts(FILE_PATH)
        print(Fore.GREEN +
              f"Contact '{name}' updated successfully")
    else:
        raise ContactNotFoundError


@contact_not_found_error
@show_phones_error
def show_phones(args):
    """
    show exist contact phone numbers
    prints command result
    """
    try:
        name = Name(args[0])
    except:
        raise CommandError

    if book.find(name):
        print(
            Fore.GREEN + f"{name.value}: {', '.join(book.find(name).get_phones())}")
    else:
        raise ContactNotFoundError


@contact_not_found_error
@add_birthday_error
def add_birthday(args):
    """
    add birthday to exist contact
    prints command result
    """
    try:
        name, birthday = args
        name = Name(name)
    except:
        raise CommandError

    try:
        birthday = Birthday(birthday)
    except:
        raise ValueError

    if book.find(name):
        record: Record = book.find(name)
        record.add_birthday(birthday)
    else:
        raise ContactNotFoundError

    book.save_contacts(FILE_PATH)
    print(Fore.GREEN + "Birthday added successfully")


@contact_not_found_error
@show_birthday_error
def show_birthday(args):
    """
    show birthday of exist user
    prints command result
    """
    try:
        name = args[0]
        name = Name(name)
    except:
        raise CommandError

    if book.find(name):
        record: Record = book.find(name)
    else:
        raise ContactNotFoundError

    if record.birthday:
        birthday = record.show_birthday()
    else:
        raise ValueError

    print(Fore.GREEN + f"{name} birthday: {birthday}")


def show_all():
    """
    show all exist contacts
    prints command result
    """
    if book.data:
        result = list()
        for record in book.data.values():
            result.append(str(record))
        print(Fore.LIGHTBLUE_EX + "\n".join(result))
    else:
        print(Fore.LIGHTBLUE_EX + "No contacts have been added yet")


def birthdays():
    get_birthdays_per_week = book.get_birthdays_per_week()

    if get_birthdays_per_week:
        result = "Next week birthdays:\n" + "-" * 10 + "\n"
        result += "\n".join([f"{day}: {celebrate_users}" for day,
                             celebrate_users in get_birthdays_per_week.items()])
        result += "\n" + "-" * 10
        print(Fore.YELLOW + result)
    else:
        print(Fore.YELLOW +
              "There is no one to celebrate birthday next week")


def main():
    """
    Assistant bot helps to collect and manage user contacts.

    To see available commands enter 'help' command
    """
    global book
    # create a new address book or load daya from a file
    book = AddressBook()
    if os.path.exists(FILE_PATH):
        book.load_contacts(FILE_PATH)
        print(Fore.BLUE +
              f"Contacts were loaded from '{FILE_PATH}' file")
    else:
        print(Fore.BLUE + "New address book was created")

    print(Fore.YELLOW + "Welcome to the assistant bot!\nEnter a command or 'help' to see available commands.")

    while True:
        user_input: str = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "help":
                help()
            case "hello":
                print(Fore.BLUE + "How can I help you?")
            case "add":
                add_contact(args)
            case "delete":
                delete_contact(args)
            case "change":
                change_contact(args)
            case "phone":
                show_phones(args)
            case "all":
                show_all()
            case "add-birthday":
                add_birthday(args)
            case "show-birthday":
                show_birthday(args)
            case "birthdays":
                birthdays()
            case "close" | "exit":
                print(Fore.MAGENTA + "Good bye!")
                break
            case _:
                print(Fore.RED + "Invalid command. Please try again")


if __name__ == "__main__":
    main()
