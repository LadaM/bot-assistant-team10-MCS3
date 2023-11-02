# CLI Contact assistant app

Presents an implementation of the final project of the Tier 1 Python course implemented by the team 10.

### Requirements

This app requires:

* Python >= 3.10
* Additional packages installed (see [Setup](#setup))


### Setup 

#### Mac OS, Linux distributions, Windows
```shell
git clone git@github.com:LadaM/bot-assistant-team10.git
cd bot-assistant-team10
pip3 install -r requirements.txt 
```

#### Windows
```shell
git clone git@github.com:LadaM/bot-assistant-team10.git
dir bot-assistant-team10
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
| `add-contact <name> <phone>`                      | adds a new contact, if there is no such name in the address book, raises an error for a duplicate contact if the same name and phone are already stored, otherwise, adds a new phone to the record                         |
| `add-birthday <name> <date(DD.MM.YYYY)>`          | if birthday is provided in the valid format and record exists, stores birthdays of the user. Usage Example: `add-birthday JohnDoe 01.01.2000`                                                                              |
| `add-email <name> <email>`                        | adds an email to the existing contact, if the contact doesn't have an email and updates it otherwise, email should be a valid email address. Usage Example: `add-email JohnDoe sample.mail@somemail.com`                   |
| `add-note <note_text>`                            | adds a new note to the notes, prints the note with its id. Usage Example: `add-note My simple note`                                                                                                                        |
| `add-phone <name> <phone>`                        | adds another phone number to an existing contact. Usage Example: `add-contact JohnDoe 1234567890`                                                                                                                          |
| `all-contacts`                                    | presents all the records stored in the address book                                                                                                                                                                        |
| `all-notes`                                       | presents all notes                                                                                                                                                                                                         |
| `change-address <name> <new_email>`               | updates the address of the existing contact                                                                                                                                                                                |
| `help`                                            | prints a welcome message                                                                                                                                                                                                   |
| `change-birthday <name> <new_birthday>`           | Updates the birthday of the existing contact if the new date is valid. Format: `DD.MM.YYYY`                                                                                                                                |
| `change-email <name> <new_email>`                 | Updates the email of the existing contact                                                                                                                                                                                  |
| `change-note <note_id> <new_note_text>`           | Updates the existing note with the given id. Usage Example: `change-note 1 My first note is going to be updated with this text`                                                                                            |
| `change-phone <username> <old_phone> <new_phone>` | If the old_phone is found and the new phone is valid, updates the given phone number with the new value                                                                                                                    |
| `delete-contact <name>`                           | Deletes the record with the given name from the address book                                                                                                                                                               |
| `delete-phone <name> <phone>`                     | Deletes the specified phone number associated with the given name                                                                                                                                                          |
| `show-phone <username>`                           | Lists all phone numbers stored for the user with the given name, if the record exists                                                                                                                                      |
| `show-birthday <name>`                            | Shows the birthday of the user with the given name, if such contact exists                                                                                                                                                 |
| `show-contact <name>`                             | Shows the record of the user with all stored information                                                                                                                                                                   |
| `show-note <note_id>`                             | Shows the note with the specified id                                                                                                                                                                                       |
| `birthdays <next_x_days>`                         | Shows birthdays of users stored in the address book that are coming within the defined period. If `next_x_days` is provided, it should be a positive number less than 365; otherwise, it shows birthdays for the next week |
