MAX_PERIOD = 365
MIN_PERIOD = 1
DEFAULT_PERIOD = 7

COMMAND_LOOKUP: dict = {
    "add-contact": "add-contact <name> <phone>",
    "add-birthday": "add-birthday <name> <birthday>",
    "add-email": "add-email <name> <email>",
    "add-address": "add-address <name> <address>",
    "add-note": "add-note <note>",
    "add-tag": "add-tag <noteId> <tag>",
    "delete-contact": "delete-contact <name>",
    "delete-note": "delete-note <note_id>",
    "delete-tag": "delete-tag <note_id> <tag>",
    "birthdays": "birthdays <period?>",
    "change-phone": "change-phone <name> <old_phone> <new_phone>",
    "change-note": "change-note <note_id> <new_note_text>",
    "show-address": "show-address <name>",
    "show-birthday": "show-birthday <name>",
    "show-email": "show-email <name>",
    "show-phone": "show-phone <name>",
    "show-note": "show-note <note_id>",
}


COMMANDS: dict = {
    "help": "shows available commands",
    "hello": "prints 'How can I help you?'",
    COMMAND_LOOKUP["add-contact"]: "adds a new contact with phone",
    COMMAND_LOOKUP["add-birthday"]: "adds birthday to a contact in format [DD.MM.YYYY]",
    COMMAND_LOOKUP["add-email"]: "adds email to a contact",
    COMMAND_LOOKUP["add-address"]: "adds address to a contact",
    COMMAND_LOOKUP["add-note"]: "adds a new note",
    COMMAND_LOOKUP["add-tag"]: "adds a tag to note",
    "all-contacts": "shows all existing contacts",
    "all-notes": "shows all saved notes",
    COMMAND_LOOKUP["birthdays"]: "shows birthdays in coming days, or for next week by default",
    COMMAND_LOOKUP["delete-contact"]: "deletes contact with the username",
    COMMAND_LOOKUP["delete-note"]: "deletes the note with id",
    COMMAND_LOOKUP["delete-tag"]: "Deletes the tag for note",
    COMMAND_LOOKUP["change-phone"]: "changes existing contact's phone number",
    COMMAND_LOOKUP["change-note"]: "replaces the text of the note with id with the new text",
    COMMAND_LOOKUP["show-address"]: "shows contact's address",
    COMMAND_LOOKUP["show-birthday"]: "shows contact's birthday date",
    COMMAND_LOOKUP["show-email"]: "shows contact's email",
    COMMAND_LOOKUP["show-phone"]: "shows contact's phone(s)",
    COMMAND_LOOKUP["show-note"]: "shows note with id",
    "exit": "enter 'close' or 'exit' to close the assistant",
    "search-contacts <search_string>": "searches contact's names and phones, outputs contacts matching "
                                       "the search string (not empty, more than 2 letters)",
}
FILE_PATH_CONTACTS = "contacts.json"
FILE_PATH_NOTES = "notes.json"

MIN_NOTE_LEN = 2
TABLE_NOTE_LEN = 75
MIN_SEARCH_STR_LEN = 2
