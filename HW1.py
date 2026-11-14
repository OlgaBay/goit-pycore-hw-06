from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


# Зберігає та перевіряє ім'я контакту
class Name(Field):
    def __init__(self, value: str):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        
        # Передаємо перевірене ім'я до батьківського класу
        super().__init__(value)


# Зберігає та перевіряє номер телефону
class Phone(Field):
    def __init__(self, phone: str):
        if len(phone) != 10 or not phone.isdigit():
            raise ValueError("Invalid phone number")

        #  Передаємо перевірений номер до батьківського класу
        super().__init__(phone)


# Зберігає інформацію про контакт та керує його телефонами
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def edit_phone(self, old_phone: str, new_phone: str):
        found_phone = self.find_phone(old_phone)

        if found_phone is not None:
            validated_phone = Phone(new_phone)
            found_phone.value = validated_phone.value

    # Повертає ім'я контакту та список його телефонів
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


# Зберігає контакти та керує записами адресної книги
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):
        self.data.pop(name, None)


if __name__ == "__main__":

    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    
    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    book.delete("Jane")