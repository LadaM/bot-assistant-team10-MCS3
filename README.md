# CLI Contact assistant app

Presents an implementation of the final project of the Tier 1 Python course implemented by the team 10.

### Requirements

This app requires:

* Python >= 3.10
* Additional packages installed (see [Setup](#setup))


### Setup 

#### Mac OS, Linux distributions, Windows
```shell
git clone git@github.com:LadaM/bot-assistant-team10-MCS3.git
cd bot-assistant-team10-MCS3
pip3 install -r requirements.txt 
```

#### Windows
```shell
git clone git@github.com:LadaM/bot-assistant-team10-MCS3.git
dir bot-assistant-team10-MCS3
pip3 install -r requirements.txt 
```

### Usage

#### Mac OS, Linux distributions

```shell
cd bot_cli
python3 __main__.py
```

#### Windows

```shell
dir bot_cli
python3 __main__.py
```

### Functionality of the CLI

The command should start with the listed string and provide a correct number of valid arguments to be interpreted correctly. Otherwise, error message will be shown.

| Command                                           | Description                                                                                                                                                                                                                |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `hello`                                           | prints a welcome message                                                                                                                                                                                                   |
| `help`                                            | prints all possible commands accessible to the user                                                                                                                                                                        |
| `exit`, `close`                                   | exits the CLI                                                                                                                                                                                                              |
| `add-address <name> <address>`                    | adds an address to the existing contact                                                                                                                                                                                    |
| `add-contact <name> <phone>`                      | creates a new contact, if there is no such name in the address book, raises an error for a duplicate contact if the same name and phone are already stored, otherwise, adds a new phone to the record                      |
| `add-birthday <name> <date(DD.MM.YYYY)>`          | if birthday is provided in the valid format and contact exists, stores birthdays of the user. Usage Example: `add-birthday JohnDoe 01.01.2000`                                                                             |
| `add-email <name> <email>`                        | adds an email to the existing contact, if the contact doesn't have an email and updates it otherwise, email should be a valid email address. Usage Example: `add-email JohnDoe sample.mail@somemail.com`                   |
| `add-note <note_text>`                            | adds a new note to the notes, prints the note with its id. Usage Example: `add-note My simple note`                                                                                                                        |
| `add-tag <note_id> <tag>`                         | adds a new tag to note. Usage Example: `add-tag 1 asap`                                                                                                                                                                    |
| `all-contacts`                                    | presents all the contacts stored in the address book                                                                                                                                                                       |
| `all-notes`                                       | presents all notes                                                                                                                                                                                                         |
| `change-note <note_id> <new_note_text>`           | Updates the existing note with the given id. Usage Example: `change-note 1 My first note is going to be updated with this text`                                                                                            |
| `change-phone <username> <old_phone> <new_phone>` | If the old_phone is found and the new phone is valid, updates the given phone number with the new value                                                                                                                    |
| `delete-contact <name>`                           | Deletes the record with the given name from the address book                                                                                                                                                               |
| `delete-phone <name> <phone>`                     | Deletes the specified phone number associated with the given name                                                                                                                                                          |
| `delete-note <note_id>`                           | Deletes the note with id                                                                                                                                                                                                   |
| `delete-tag <note_id> <tag>`                      | Deletes the note's tag                                                                                                                                                                                                     |
| `search-contacts <search_string>`                 | Searches contact's names and phones, outputs contacts matching. The search string (not empty, more than 2 letters)                                                                                                         |
| `show-phone <name>`                               | Lists all phone numbers stored for the user with the given name, if the record exists                                                                                                                                      |
| `show-email <name>`                               | Shows contact's email                                                                                                                                                                                                      |
| `show-birthday <name>`                            | Shows the birthday of the user                                                                                                                                                                                             |
| `show-address <name>`                             | Shows the address of the user                                                                                                                                                                                              |
| `show-note <note_id>`                             | Shows the note with the specified id                                                                                                                                                                                       |
| `birthdays <period?>`                             | Shows birthdays of users stored in the address book that are coming within the defined period. If `period` is provided, otherwise, it shows birthdays for the next week. `period` must be a positive number less than 365. |
