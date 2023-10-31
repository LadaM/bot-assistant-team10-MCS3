import os.path
from address_book_classes import AddressBook
from constants import FILE_PATH
from commands import parse_input, add_contact, delete_contact, change_contact, show_phones, show_all, add_birthday, \
    show_birthday, birthdays, address_book, help
from colorama import Fore
import colorama

# Initialize colorama
colorama.init(autoreset=True)


# address_book: AddressBook


def main(address_book):
    """
    Assistant bot helps to collect and manage user contacts.

    To see available commands enter 'help' command
    """
    # global address_book
    # create a new address book or load daya from a file
    # address_book = AddressBook()
    if os.path.exists(FILE_PATH):
        address_book.load_contacts(FILE_PATH)
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
                birthdays(args)
            case "close" | "exit":
                print(Fore.MAGENTA + "Good bye!")
                break
            case _:
                print(Fore.RED + "Invalid command. Please try again")


if __name__ == "__main__":
    main(address_book)
