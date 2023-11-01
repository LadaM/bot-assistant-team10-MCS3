"""
нотаток буде мати вигляд насутпний:
{"notes": [
   {
   Note: "text",
   Tags: ['one','two']
   }
]

класи:
Field - базовий
Note(Field) - поле тексту нотатку - нотаток тільки в одннині стрінга
Tag(Field) - теги як масив, тобто тут їх буде декілька
Notes(UserDict) - звичайний словни вигляд матиме такий як зверху формат

важливі зауваження:
{"Note": note, "Tags": tags}  - повертає нотатки в такому вигляді
якщо поле "Tags" - у людини пусте, веррне [] пустий масив, треба на обробнику боті конвертувати в шось інше
якщо команда з Індексо не знайшла шось по індексу, то помилки відловлюєм в боті, я тут не додавав обробник помилок
якшо команда пошуку (по тексту/тегу) не знайшла співпадіння має вертати всюди пустий масив

доступні методи Notes:
- ініт - створюється записничок з базовим форматом {"notes": []}
- add_note(self, note) - додаєм нотаток
- remove_note(self, index) - видалення по індексу (видаляє все і нотаток і його теги)
- replace_note(self, index, new_note): - заміна ТЕКСТУ нотатку, позиція і теги залишаються
- def update_note(self, index, add_note_text): - доповнення нотатку, додається чернз ";"
- def find_note_by_index(self, index): - шукає по індексу , повертатиме все {"Note": note, "Tags": tags} // note- стрінга + tags - список стрінгів
- find_note_by_subtext(self, sub_text): - шукає співпадіня по тексут - мінім 3 літери я не виставив обмеження покишо, повертає ось так [{"Note": note, "Tags": tags} ]
- def show_notes(self): - повертає всі теги notes = [{index: {"Note": note, "Tags": tags}}, {index: {"Note": note, "Tags": tags}}] - обовязково звернути увагу на індекси їх юзати для видачі
- def add_tag(self, index, tag): - додається тег, обовязково треба додати індекс нотатку
- remove_tag(self, note_index, tag): - вказати у якому нотатку який тег видалити 
- change_tag(self): - не писав бо редагування тегів не знаю чи треба - 
"""

from collections import UserDict
from address_book_classes import Field


class Note(Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Tag(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Notes(UserDict):
    def __init__(self):
        super().__init__()
        self.data = {"notes": []}

    def add_note(self, note):
        self.data["notes"].append({"note": Note(note), "tags": []})

    def remove_note(self, index):
        del self.data["notes"][index - 1]

    def replace_note(self, index, new_note):
        self.data["notes"][index - 1]["note"] = Note(new_note)

    def update_note(self, index, add_note_text):
        current_note = self.find_note_by_index(index)
        current_note_text = str(current_note["Note"])
        update_note_text = current_note_text + "; " + add_note_text
        self.replace_note(index, update_note_text)

    def find_note_by_index(self, index):
        data = self.data["notes"][index - 1]
        note = str(data["note"])
        tags = [str(tag) for tag in data["tags"]]
        return {"Note": note.capitalize(), "Tags": tags}

    def find_note_by_subtext(self, sub_text):
        searched_note = []
        for data in self.data["notes"]:
            note = str(data["note"]).casefold()
            tags = [str(tag).casefold() for tag in data["tags"]]
            if sub_text.casefold() in note:
                searched_note.append({"Note": note.capitalize(), "Tags": tags})
        return searched_note

    def show_notes(self):
        notes = []
        for index, data in enumerate(self.data["notes"]):
            note = str(data["note"])
            tags = [str(tag) for tag in data["tags"]]
            notes.append({index: {"Note": note.capitalize(), "Tags": tags}})

        return str(notes)

    def add_tag(self, index, tag):
        self.data["notes"][index - 1]["tags"].append(Tag(tag))

    def remove_tag(self, note_index, tag):
        tags = [str(tag) for tag in self.data["notes"][note_index - 1]["tags"]]
        tag_index = tags.index(tag)
        del self.data["notes"][note_index - 1]["tags"][tag_index]

    def find_notes_by_tag(self, tag):
        searched_note = []
        for data in self.data["notes"]:
            note = str(data["note"]).casefold()
            tags = [str(tag).casefold() for tag in data["tags"]]
            if tag.casefold() in tags:
                searched_note.append({"Note": note.capitalize(), "Tags": tags})
        return searched_note

    def change_tag(self):
        pass  # зробити редагування конретного тега? не впевнений шо треба

    def __str__(self):
        notes = []
        for index, note in enumerate(self.data["notes"]):
            notes.append({index: note["tags"]})
        return str(notes)


if __name__ == "__main__":
    notes = Notes()
    notes.add_note("My first note")
    notes.add_note("My second note")
    notes.add_note("My third note")
    print(notes.show_notes())
    notes.add_tag(1, "TTT")
    notes.add_tag(1, "AAA")
    notes.add_tag(1, "BBB")
    notes.add_tag(2, "BBB")
    print(notes.show_notes())
    notes.remove_tag(1, "TTT")
    print(notes.show_notes())
    notes.update_note(1, "additional info")
    print(notes.show_notes())
    notes.remove_note(1)
    # ++
    print(notes.show_notes())
    print(notes.show_notes())
    print(f"here is your note by index: {notes.find_note_by_index(1)}")
    notes.replace_note(1, "Replaced note")
    print(f"here is your by text: {notes.find_note_by_subtext('third')}")
    print(f"here is your by tag: {notes.find_notes_by_tag('BBB')}")
    print(notes.show_notes())
