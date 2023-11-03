import re
from datetime import datetime
import json
import os.path
from collections import defaultdict, UserDict
from constants import FILE_PATH_CONTACTS


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Name(Field):
    def __init__(self, value: str):
        super().__init__(value.capitalize())

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value.capitalize()


class Phone(Field):
    def __init__(self, phone: str):
        if not re.match(r'\b\d{10}\b', phone):
            raise ValueError(
                f"'{phone}' doesn't match the phone format XXXXXXXXXX(10 digits)")
        super().__init__(phone)


class Birthday(Field):
    def __init__(self, birthday):
        if not re.match(r'\b\d{2}\.\d{2}\.\d{4}\b', birthday):
            raise ValueError(
                f"'{birthday}' doesn't match the birthday format DD.MM.YYYY")
        birthday = datetime.strptime(birthday, '%d.%m.%Y').date()
        super().__init__(birthday)

    def __str__(self):
        return datetime.strftime(self.value, '%d.%m.%Y')


class Email(Field):
    def __init__(self, email):
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
            raise ValueError(
                f"'{email}' is not valid email address")
        self.email = email
        super().__init__(email)

    def __str__(self):
        return str(self.email)


class Address(Field):
    def __init__(self, value):
        if len(value.strip()) > 4:
            super().__init__(value)
        else:
            raise ValueError("Address must be at least 5 symbols")


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = []
        self.birthday = None
        self.address = None
        self.email = None
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone: Phone):
        if not phone in self.phones:
            self.phone = phone
            self.phones.append(self.phone)

    def remove_phone(self, phone: Phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(phone)

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        for p in self.phones:
            if p.value == old_phone.value:
                p.value = new_phone.value
                return
        raise ValueError(f"Phone '{old_phone}' not found in the record")

    def find_phone(self, phone: Phone):
        for p in self.phones:
            if p.value == phone.value:
                return p
        raise ValueError(f"Phone '{phone}' not found in the record")

    def get_phones(self):
        return [phone.value for phone in self.phones]

    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def show_birthday(self):
        return self.birthday

    def add_email(self, email: Email):
        self.email = email

    def add_address(self, address: Address):
        self.address = address

    def show_address(self):
        return self.address

    def show_email(self):
        return self.email

    def __str__(self):
        address_str = f", address: {self.address.value}" if self.address is not None else ""
        birthday_str = f", birthday: {datetime.strftime(self.birthday.value, '%d.%m.%Y')}" if self.birthday is not None else ""
        email_str = f", email: {self.email}" if self.email is not None else ""
        return f"Name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{birthday_str}{email_str}{address_str}"


class AddressBook(UserDict[str, Record]):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: Name) -> Record | None:
        return self.get(name.value)

    def delete(self, name: Name):
        self.__delitem__(name.value)

    def get_records(self) -> list[Record]:
        return self.data.values()

    @classmethod
    def from_json(cls, data):
        address_book = cls()
        for name, record_data in data.items():
            name_field = Name(record_data['name'])
            record = Record(name_field)

            phones = [Phone(phone) for phone in record_data['phones']]
            for phone in phones:
                record.add_phone(phone)

            if record_data['birthday']:
                birthday = Birthday(record_data['birthday'])
                record.add_birthday(birthday)

            if record_data["address"]:
                address = Address(record_data['address'])
                record.add_address(address)

            if record_data['email']:
                email = Email(record_data['email'])
                record.add_email(email)

            address_book.add_record(record)

        return address_book

    def load_contacts(self, path):
        with open(path, "r") as file:
            data = json.load(file)
            address_book = AddressBook.from_json(data)
            self.data = address_book.data

    def save_contacts(self, path):
        with open(path, "w") as file:
            def custom_serializer(obj):
                if isinstance(obj, Record):
                    return {
                        'name': obj.name.value,
                        'phones': [phone.value for phone in obj.phones],
                        'birthday': str(obj.birthday) if obj.birthday else None,
                        'address': obj.address.value if obj.address else None,
                        'email': str(obj.email) if obj.email else None,

                    }
                return obj

            json.dump(self.data, file, default=custom_serializer, indent=4)

    def get_birthdays_per_period(self, period: int = 7) -> dict | None:
        upcoming_birthdays = defaultdict(list)
        current_date = datetime.today().date()

        for user, record in self.data.items():
            if record.birthday:
                birthday = record.birthday.value
                birthday_this_year: datetime = birthday.replace(
                    year=current_date.year)

                if birthday_this_year < current_date:
                    birthday_this_year: datetime = birthday.replace(
                        year=current_date.year + 1)

                delta_days = (birthday_this_year - current_date).days

                if delta_days < period:
                    day_name = birthday_this_year.strftime('%A')
                    birthday_date = datetime.strftime(birthday_this_year, '%A, %d %B')
                    upcoming_birthdays[birthday_date].append(user)
        sorted_data = dict(sorted(upcoming_birthdays.items()))
        return sorted_data


if __name__ == '__main__':
    # Створення нової адресної книги
    address_book = AddressBook()

    if os.path.exists(FILE_PATH_CONTACTS):
        address_book.load_contacts(FILE_PATH_CONTACTS)
        print(f"Contacts were loaded from '{FILE_PATH_CONTACTS}' file")
    else:
        print("New address book was created")

    # Створення запису для John
    john_record = Record(Name("John"), Phone("0987683542"))

    john_record.add_phone(Phone("5555555555"))
    print(john_record.get_phones())
    john_record.add_birthday(Birthday("03.11.1984"))
    john_record.add_email(Email("oo@o.ua"))

    # Додавання запису John до адресної книги
    address_book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record(Name("Jane"), Phone("0876543210"))
    jane_record.add_birthday(Birthday("03.11.1987"))
    address_book.add_record(jane_record)

    print(jane_record.show_birthday())

    # Створення та додавання нового запису для Simon
    simon_record = Record(Name("Simon"), Phone("0811234567"))
    address_book.add_record(simon_record)

    # Виведення всіх записів у книзі
    for name, record in address_book.data.items():
        print(record)

    print('-' * 10)

    # Знаходження та редагування телефону для John
    john = address_book.find(Name("John"))
    john.edit_phone(Phone("5555555555"), Phone("1112223333"))
    print(john)  # Виведення: Contact name: John, phones: 1112223333;

    print('-' * 10)

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone(Phone("1112223333"))
    print(f"{john.name}: {found_phone}")

    print('-' * 10)

    # Пошук всіх телефонів у записі John
    found_phones = john.get_phones()
    print(found_phones)  # ['1112223333', '5555555555']

    # Видалення запису Jane
    # book.delete(Name("Jane"))

    # Видалення телефону "5555555555" із запису John
    john_record.remove_phone(Phone("5555555555"))

    # Додавання адреси
    john_record.add_address(Address("Kyiv city, Khreschatic str, 1"))

    # Виведення адреси по юзеру
    print(f"John address: {john_record.show_address()}")

    print('-' * 10)

    # Виведення всіх записів у книзі
    for name, record in address_book.data.items():
        print(record)

    # Виведення днів нарождення на наступний тиждень
    print(address_book.get_birthdays_per_period())

    # Save data into JSON file
    address_book.save_contacts(FILE_PATH_CONTACTS)
