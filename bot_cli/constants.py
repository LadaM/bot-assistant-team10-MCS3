MAX_PERIOD = 365
MIN_PERIOD = 1
DEFAULT_PERIOD = 7
FILE_PATH = "contacts.json"
COMMANDS: dict = {
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
WEEK_DAY_DICT = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}
