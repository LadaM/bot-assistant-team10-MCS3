from address_book_classes import (
    Name,
    Phone,
    Birthday,
    Record,
    AddressBook,
    Email,
    Address,
)
from error_handlers import (
    add_contact_error,
    delete_contact_error,
    change_contact_error,
    show_phones_error,
    contact_not_found_error,
    add_birthday_error,
    show_birthday_error,
    max_period_error,
    CommandError,
    ContactAlreadyExistsError,
    ContactNotFoundError,
    EmailValidationError,
    search_error,
    add_address_error,
    show_address_error,
    add_email_error,
    show_email_error,
    note_error_handler,
    tag_error_handler,
)
from notes_classes import Notes
import textwrap
from constants import (
    FILE_PATH_CONTACTS,
    FILE_PATH_NOTES,
    MAX_PERIOD,
    MIN_PERIOD,
    DEFAULT_PERIOD,
    COMMANDS,
    MIN_NOTE_LEN,
    TABLE_NOTE_LEN,
    COMMAND_LOOKUP,
)
from print_util import print_warn, print_info, print_success, print_magenta

address_book = AddressBook()
notebook = Notes()


def help():
    """
    Prints out available commands
    prints list of bot commands
    """
    sorted_commands = dict(sorted(COMMANDS.items(), key=lambda item: item[0]))
    formatted_commands = ""

    for key, value in sorted_commands.items():
        formatted_commands += f">>> {key: <45}: {value: <}\n"

    print_magenta(formatted_commands)


def get_matching_commands(command):
    matching_commands = []
    for c in COMMANDS.keys():
        if c.find(command) >= 0:
            matching_commands.append(">>> " + c)
    return matching_commands


def parse_input(user_input: str):
    """
    Parse input command
    Prints available commands in case of empty input
    @return - command and arguments
    """
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
    except ValueError:
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

    if address_book.find(name):
        contact = address_book.find(name)

        if not phone.value in contact.get_phones():
            record: Record = contact.add_phone(phone)
        else:
            raise ContactAlreadyExistsError
    else:
        record: Record = Record(name, phone)
        address_book.add_record(record)

    address_book.save_contacts(FILE_PATH_CONTACTS)
    print_success(f"Contact added successfully: {name} {phone}")


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

    if address_book.find(name):
        address_book.delete(name)
    else:
        raise ContactNotFoundError

    address_book.save_contacts(FILE_PATH_CONTACTS)
    print_success(f"Contact '{name}' deleted successfully")


@contact_not_found_error
@add_email_error
def add_email(args):
    """
    add email for exist user
    prints command result
    """
    try:
        name, email = args
        name = Name(name)
    except:
        raise CommandError
    try:
        email = Email(email)
    except ValueError:
        raise EmailValidationError
    if address_book.find(name):
        record: Record = address_book.find(name)
        record.add_email(email)
    else:
        raise ContactNotFoundError

    address_book.save_contacts(FILE_PATH_CONTACTS)
    print_success("Email added successfully")


@show_email_error
@contact_not_found_error
def show_email(args):
    """
    show email for exist user
    prints command result
    """
    try:
        name = args[0]
        name = Name(name)
    except:
        raise CommandError

    if address_book.find(name):
        record: Record = address_book.find(name)
    else:
        raise ContactNotFoundError

    if record.email:
        email = record.show_email()
    else:
        raise ValueError

    print_success(f"{name} email: {email}")


@contact_not_found_error
@change_contact_error
def change_phone(args: list[str, str, str]):
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

    if address_book.find(name):
        record: Record = address_book.find(name)

        if old_phone.value in record.get_phones():
            record.edit_phone(old_phone, new_phone)
        else:
            raise KeyError

        address_book.save_contacts(FILE_PATH_CONTACTS)
        print_success(f"Contact '{name}' updated successfully")
    else:
        raise ContactNotFoundError


@search_error
def search_contacts(args):
    """Finds all records stored in the address book if any attribute of the record match the search string"""
    try:
        search_str = args[0]
        search_result = []
        for r in address_book.get_records():
            if str(r).casefold().find(search_str) > 0:
                search_result.append(r)
        if len(search_result) > 0:
            print_success("\n".join([str(r) for r in search_result]))
        else:
            print_warn("No results found!")
    except (ValueError, IndexError) as e:
        raise CommandError


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

    if address_book.find(name):
        print_success(
            f"{name.value}: {', '.join(address_book.find(name).get_phones())}"
        )
    else:
        raise ContactNotFoundError


@contact_not_found_error
@add_birthday_error
def add_birthday(args):
    """
    adds birthday to exist contact
    replaces birthday if already exist
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

    if address_book.find(name):
        record: Record = address_book.find(name)
        record.add_birthday(birthday)
    else:
        raise ContactNotFoundError

    address_book.save_contacts(FILE_PATH_CONTACTS)
    print_success("Birthday added successfully")


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

    if address_book.find(name):
        record: Record = address_book.find(name)
    else:
        raise ContactNotFoundError

    if record.birthday:
        birthday = record.show_birthday()
    else:
        raise ValueError

    print_success(f"{name} birthday: {birthday}")


def show_all_contacts():
    """
    show all exist contacts
    prints command result
    """
    if address_book.data:
        result = list()
        for record in address_book.data.values():
            result.append(str(record))
        print_info("\n".join(result))
    else:
        print_info("No contacts have been added yet")


@max_period_error
def birthdays(args):
    """
    ...upcoming birthdays...
    default period is 7 days
    """
    if args:
        try:
            period = int(args[0])
            if (period < MIN_PERIOD) or (period > MAX_PERIOD):
                raise ValueError
        except:
            raise ValueError
    else:
        period = DEFAULT_PERIOD

    get_birthdays_per_period = address_book.get_birthdays_per_period(period)

    if get_birthdays_per_period:
        formatted_data = []

        for date, users in get_birthdays_per_period.items():
            formatted_key = f'{date}: {", ".join(users)}'
            formatted_data.append(formatted_key)

        formatted_output = ",\n".join(formatted_data)
        result = f"Birthdays for next {period} day(s):\n" + "-" * 10 + "\n"
        result += formatted_output
        result += "\n" + "-" * 10
        print_success(result)
    else:
        print_warn(f"There is no one to celebrate birthday for next {period} day(s)")


@contact_not_found_error
@add_address_error
def add_address(args):
    """
    Adds an address to exist contact
    Replaces the address if it already exists
    """
    try:
        name, *address = args
        name = Name(name)
        address = " ".join(address)
    except:
        raise CommandError

    record: Record = address_book.find(name)
    if not record:
        raise ContactNotFoundError
    record.add_address(Address(address))

    address_book.save_contacts(FILE_PATH_CONTACTS)
    print_success("Address added successfully")


@contact_not_found_error
@show_address_error
def show_address(args):
    try:
        name = args[0]
        name = Name(name)
    except:
        raise CommandError

    record: Record = address_book.find(name)
    if not record:
        raise ContactNotFoundError

    if record.address:
        print_success(f"{name} address: {record.show_address()}")
    else:
        raise ValueError


@note_error_handler
def add_note(notebook: Notes, args):
    text = " ".join(args)
    if text.isspace() or len(text) < MIN_NOTE_LEN:
        raise ValueError(
            f"Note cannot be empty and must be more than {MIN_NOTE_LEN} characters long"
        )
    note_id, _ = notebook.add_note(text)
    notebook.save_notes(FILE_PATH_NOTES)
    print_success(f"Note with id {note_id} created successfully")


@note_error_handler
def show_note(notebook: Notes, args):
    try:
        note_id = int(args[0])
    except (ValueError, IndexError) as e:
        raise CommandError(
            "Expecting command in form " + COMMAND_LOOKUP.get("show-note")
        )
    try:
        res = notebook.find_note_by_index(note_id)
        if res.get("Tags") == []:
            print_info(res.get("Note"))
        else:
            tags = ",".join(res.get("Tags"))
            print_info(f'Note: {res.get("Note")}\nTags: {tags}')
    except IndexError:
        raise ValueError(f"We don't have a note with id {note_id}")


@note_error_handler
def show_all_notes(notebook: Notes):
    all_notes = notebook.show_notes()
    if len(all_notes) > 0:
        ellipsis = "..."
        index_width = 4
        print(f"{'id'.upper():<{index_width}} | {'note'.upper():^{TABLE_NOTE_LEN}}")
        print("-" * (TABLE_NOTE_LEN + index_width + len(ellipsis)))
        for data in all_notes:
            index = list(data.keys())[0]
            note_text = list(data.values())[0].get("Note")
            print(
                f"{index:<5}|{textwrap.shorten(note_text, width=TABLE_NOTE_LEN, placeholder=ellipsis)}"
            )
    else:
        print_warn("We haven't stored any notes yet.")


@note_error_handler
def change_note(notebook: Notes, args):
    """
    change exist notes on new one
    prints command result
    """
    index, text = args[0], " ".join(args[1:])
    notebook.change_note(int(index), text)
    notebook.save_notes(FILE_PATH_NOTES)
    print_success("Note successfully replaced")


@note_error_handler
def remove_note(notebook: Notes, args):
    """
    remove notes by id
    prints command result
    """
    index = args[0]
    notebook.remove_note(int(index))
    notebook.save_notes(FILE_PATH_NOTES)
    print_success("Note successfully removed")


@note_error_handler
def search_note(notebook: Notes, args):
    """
    searching notes by text
    prints list of coincidence
    """
    # find_note_by_subtext
    text = " ".join(args)
    notes = notebook.find_note_by_subtext(text)
    if text.isspace() or len(text) < MIN_NOTE_LEN:
        raise ValueError(
            f"Note cannot be empty and must be more than {MIN_NOTE_LEN} characters long"
        )
    if not notes:
        print_info("No matches found for: '{text}'")
    output = []
    for note in notes:
        if note["Tags"]:
            str_tags = " ".join(note["Tags"])
            note_string = f"Note: {note['Note']}\n Tags:{str_tags}"
        else:
            note_string = f"Note: {note['Note']}"
        output.append(note_string)
    output_string = "\n".join(output)
    print_success(output_string)


@tag_error_handler
def add_tag(notebook: Notes, args):
    """
    Adds tag by note id
    prints command result
    """
    index, tag = args[0], " ".join(args[1:])
    if int(index) < 1:
        raise IndexError
    if tag.isspace() or len(tag) < MIN_NOTE_LEN:
        raise ValueError(
            f"Note cannot be empty and must be more than {MIN_NOTE_LEN} characters long"
        )
    notebook.add_tag(int(index), tag.casefold())
    notebook.save_notes(FILE_PATH_NOTES)
    print_success(f"Note with id {index} successfully update tags")


@tag_error_handler
def delete_tag(notebook: Notes, args):
    """
    remove tag by note id
    prints command result
    """
    index, tag = args[0], " ".join(args[1:])
    if int(index) < 1:
        raise IndexError
    result = notebook.remove_tag(int(index), tag.casefold())
    if result == "-1":
        print_warn("Tag not found.")
    else:
        notebook.save_notes(FILE_PATH_NOTES)
        print_success("Tag successfully deleted")
