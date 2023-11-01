import os.path

import commands
from constants import FILE_PATH
from print_util import print_error, print_info, print_warn


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
        print_info(f"Contacts were loaded from '{FILE_PATH}' file")
    else:
        print_info("New address book was created")

    print_warn("Welcome to the assistant bot!\nEnter a command or 'help' to see available commands.")

    while True:
        user_input: str = input("Enter a command: ")
        command, *args = commands.parse_input(user_input)

        match command:
            case "help":
                commands.help()
            case "hello":
                print_info("How can I help you?")
            case "add-contact":
                commands.add_contact(args)
            case "delete-contact":
                commands.delete_contact(args)
            case "change-phone":
                commands.change_phone(args)
            case "show-phone" | "phone":
                commands.show_phones(args)
            case "all":
                commands.show_all()
            case "add-birthday":
                commands.add_birthday(args)
            case "show-birthday":
                commands.show_birthday(args)
            case "search-contacts" | "search-contact":
                commands.search_contacts(args)
            case "birthdays":
                commands.birthdays(args)
            case "close" | "exit":
                print_info("Goodbye!")
                break
            case _:
                print_error("Invalid command. Please try again")


if __name__ == "__main__":
    main(commands.address_book)
