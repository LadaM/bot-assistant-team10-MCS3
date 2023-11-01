# bot-assistant-team10
Presents an implementation of the final project of the Tier 1 Python course implemented by the team 10
# Functionality of the CLI
The command should start with the listed string and provide a correct number of valid arguments to be interpreted correctly. Otherwise, error message will be shown.
1. `hello`- prints a welcome message
1. `help` - prints all possible commands accessible to the user
3. `exit`, `close` - exits the CLI
5. `add-address <name> <address>` - adds an address to the existing contact
5. `add-contact <name> <phone>` - adds a new contact, if there is no such name in the address book, raises an error for a duplicate contact if the same name and phone are already stored, otherwise, adds a new phone to the record
8. `add-birthday <name> <date(DD.MM.YYYY)>` - if birthday is provided in the valid format and record exists, stores birthdays of the user. Usage Example: `add-birthday JohnDoe 01.01.2000`
5. `add-email <name> <email>` - adds an email to the existing contact, if the contact doesn't have an email and updates it otherwise, email should be a valid email address. Usage Example: `add-email JohnDoe sample.mail@somemail.com`
5. `add-note <note_text>` - adds a new note to the notes, prints the note with its id. Usage Example: `add-note My simple note` 
5. `add-phone <name> <phone>` - adds another phone number to an existing contact. Usage Example: `add-contact JohnDoe 1234567890`
2. `all-contacts` - presents all the records stored in the address book
1. `all-notes` - presents all notes
1. `change-address <name> <new_email>` - updates the address of the existing contact
1. `change-birthday <name> <new_birthday(DD.MM.YYYY)>` - updates the birthday of the existing contact if the new date is valid
1. `change-email <name> <new_email>` - updates the email of the existing contact
1. `change-note <note_id> <new_note_text>` - updates the existing note with the id. Usage Example: `change-note 1 My first note is going to be updated with this text`
6. `change-phone <username> <old_phone> <new_phone>` - if the old_phone is found in the records and the new phone is valid, updates the given phone number with the new value
1. `delete-contact <name>` - deletes the record with the given name from the address book
1. `delete-phone <name> <phone>` - deletes 
7. `show-phone <username>` - lists all phone numbers stored for the user with the name, if record exists
9. `show-birthday <name>` - shows birthday of user with the given name, if such contact exists
1. `show-contact <name>` - shows the record of the user with all stored information
1. `show-note <note_id>` - show the note with the id
10. `birthdays <next_x_days>` - shows birthdays of the users stored in the address book that are coming withing the defined period, if user provides `next_x_days` argument, otherwise shows birthdays for the next week. `next_x_days` is a positive number less than 365

