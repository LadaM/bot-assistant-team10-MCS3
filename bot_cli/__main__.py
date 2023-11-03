import os.path

import commands
from constants import FILE_PATH_CONTACTS, FILE_PATH_NOTES
from print_util import print_error, print_info, print_warn


def main(address_book, notebook):
    """
    Assistant bot helps to collect and manage user contacts.

    To see available commands enter 'help' command
    """

    if os.path.exists(FILE_PATH_CONTACTS):
        address_book.load_contacts(FILE_PATH_CONTACTS)
        print_info(f"Contacts were loaded from '{FILE_PATH_CONTACTS}' file")
    else:
        print_info("New address book was created")

    if os.path.exists(FILE_PATH_NOTES):
        notebook.load_notes(FILE_PATH_NOTES)
        print_info(f"Notes were loaded from '{FILE_PATH_NOTES}' file")
    else:
        print_info("New notebook was created")

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
            case "add-note":
                commands.add_note(notebook, args)
            case "change-note":
                commands.change_note(notebook, args)
            case "remove-note":
                commands.remove_note(notebook, args)
            case "search-note":
                commands.search_note(notebook, args)
            case "add-address":
                commands.add_address(args)
            case "show-address":
                commands.show_address(args)
            case "add-email":
                commands.add_email(args)
            case "show-email":
                commands.show_email(args)
            case "show-note":
                commands.show_note(notebook, args)
            case "all-notes" | "all-note":
                commands.show_all_notes(notebook)
            case "delete-contact":
                commands.delete_contact(args)
            case "change-phone":
                commands.change_phone(args)
            case "show-phone" | "phone":
                commands.show_phones(args)
            case "all-contacts" | "all-contact":
                commands.show_all_contacts()
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
                matching_commands = commands.get_matching_commands(command)
                if len(matching_commands) > 0:
                    print_info("Did you mean this?")
                    print_info('\n'.join(matching_commands))
                else:
                    print_error("Invalid command. Please try again")


if __name__ == "__main__":
    main(commands.address_book, commands.notebook)
