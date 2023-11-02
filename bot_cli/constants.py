MAX_PERIOD = 365
MIN_PERIOD = 1
DEFAULT_PERIOD = 7
COMMANDS: dict = {
    "help": "shows available commands",
    "hello": "prints 'How can I help you?'",
    "add-contact <user> <phone>": "adds a new contact with phone",
    "add-birthday <user> <birthday>": "adds birthday to a contact in format [DD.MM.YYYY]",
    "add-phone <user> <phone>": "adds a phone number to a contact",
    "add-email <user> <email>": "adds email to a contact",
    "add-address <user> <address>": "adds address to a contact",
    "add-note <note>": "adds a new note",
    "all-contacts": "shows all existing contacts",
    "all-notes": "shows all saved notes",
    "birthdays <days?>": "shows birthdays in coming days, or for next week by default",
    "delete-contact <user>": "deletes contact with the username",
    "delete-note <note_id>": "deletes the note with id",
    "change-phone <user> <old_phone> <new_phone>": "changes existing contact's phone number",
    "change-email <user> <email>": "changes existing contact's email",
    "show-address <user>": "shows contact's birthday date",
    "show-birthday <user>": "shows contact's birthday date",
    "show-email <user>": "shows contact's birthday date",
    "show-phone <user>": "shows contact's phone(s)",
    "show-note <note_id>": "shows note with id",
    "exit": "enter 'close' or 'exit' to close the assistant",
    "search-contacts <search_string>": "searches contact's names and phones, outputs contacts matching "
                                       "the search string (not empty, more than 2 letters)",
}
FILE_PATH = "contacts.json"
