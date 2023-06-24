import re
import json
from datetime import datetime
from collections import UserDict


class SetterValueIncorrect(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class AddressBook(UserDict):
    # Class representing an address book, which is a subclass of UserDict

    def add_record(self, aRecord):
        # Method to add a record to the address book
        self.data[aRecord.user_name.value] = aRecord

    def find_in_values(self, aRecord):
        # Method to find a record in the address book's values
        if aRecord in self.data.values():
            for i in self.data.values():
                if i == aRecord:
                    return (aRecord.user_name.value, aRecord)
        return None

    def find_users(self, search_string):
            # Find users whose name or phone number matches the search string
        matching_users = []
        for record in self.data.values():
            if record.user_name.value.find(search_string) != -1:
                matching_users.append(record)
            else:
                for phone in record.user_phones:
                    if phone.value.find(search_string) != -1:
                        matching_users.append(record)
                        break
        return matching_users
    
    def __iter__(self):
        # Generator function to yield representations of N records
        def record_generator():
            N = 5  # Number of records to yield in each iteration
            count = 0
            for record in self.data.values():
                yield repr(record)
                count += 1
                if count >= N:
                    break

        return record_generator()
    
    def to_dict(self):
        return {
            'data': {
                name: record.to_dict() for name, record in self.data.items()
            }
        }
    
    def from_dict(cls, data):
        address_book = cls()
        records = [Record.from_dict(record_data) for record_data in data['data'].values()]
        for record in records:
            address_book.add_record(record)
        return address_book
    
    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.to_dict(), file, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        address_book = cls()
        records = [Record.from_dict(record_data)
                   for record_data in data['data'].values()]
        for record in records:
            address_book.add_record(record)
        return address_book


class Field():
    # Base class representing a field
    def __eq__(self, other):
        if isinstance(other, Field):
            return self.value == other.value
        return False

    def __init__(self, value = ''):
        # Constructor to initialize the field with a value
        self._value = value


class Name(Field):
    # Class representing a name field, which is a subclass of Field
    @property
    def value(self):
        # Getter method for the value property
        return self._value

    @value.setter
    def value(self, new_value):
        # Setter method for the value property
        if isinstance(new_value,str):
            self._value = new_value
        else:
            raise SetterValueIncorrect('Only string accepted')


class Phone(Field):
    # Class representing a phone field, which is a subclass of Field

    @property
    def value(self):
        # Getter method for the value property
        return self._value

    @value.setter
    def value(self, new_value):
        # Setter method for the value property
        if not isinstance(new_value, str):
            try:
                new_value = str(new_value)
            except TypeError:
                raise SetterValueIncorrect(
                    'Only correct type of phone numbers accepted')
            
        if re.search(r"[+]380[(]\d{2}[)]\d{3}[-]\d{1,2}[-]\d{2,3}(?=.{1,17})", new_value):
            self._value = new_value
        else:
            raise SetterValueIncorrect('Only correct type of phone numbers accepted')


class Birthday(Field):
    # Class representing a birthday field, which is a subclass of Field

    @property
    def value(self):
        # Getter method for the value property
        return self._value

    @value.setter
    def value(self, new_value):
        # Setter method for the value property
        if isinstance(new_value, datetime):
            self._value = new_value
        elif isinstance(new_value, str):
            try:
                self._value = datetime.strptime(new_value, '%d %B %Y')
            except:
                raise SetterValueIncorrect('Incorrect string type of data')
        else:
            raise SetterValueIncorrect('Only string data or datetime accepted')


class Record():
    # Class representing a record

    def __init__(self, name, phone=None, birthday=None):
        # Constructor to initialize the record with a name, phone, and birthday
        self.user_phones = []
        self.user_birthday = birthday

        if isinstance(name, str):
            self.user_name = Name(name)
        elif isinstance(name, Name):
            self.user_name = name
        if phone:
            self.add_phone(phone)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.user_name.value == other.user_name.value
        return False
    
    def to_dict(self):
        return {
            'user_name': self.user_name.value,
            'user_phones': [phone.value for phone in self.user_phones],
            'user_birthday': self.user_birthday.isoformat() if self.user_birthday else None
            }

    @classmethod
    def from_dict(cls, data):
        print(data)
        name = Name(data.get('user_name'))
        phones_data = data.get('user_phones', [])
        phones = [Phone(phone_number) for phone_number in phones_data]
        birthday = datetime.fromisoformat(
            data['user_birthday']) if data['user_birthday'] else None
        record = Record(name, birthday =  birthday)
        for phone in phones:
            record.add_phone(phone)
        return record
    
    def add_phone(self, aPhone):
        # Method to add a phone to the record
        if isinstance(aPhone, str):
            self.user_phones.append(Phone(aPhone))
        elif isinstance(aPhone, Phone):
            self.user_phones.append(aPhone)

    def remove_phone(self, aPhone):
        # Method to remove a phone from the record
        try:
            if isinstance(aPhone, Phone):
                self.user_phones.remove(aPhone)
            elif isinstance(aPhone, str):
                self.user_phones.remove(Phone(aPhone))
        except ValueError:
            print('Not find such phone')

    def remove_n_phone(self, aPhoneIndex):
        # Method to remove the phone at a specified index from the record
        self.user_phones.pop(aPhoneIndex)

    def change_n_phone(self, aPhoneIndex, aNewPhone):
        # Method to change the phone at a specified index to a new phone
        self.user_phones[aPhoneIndex].value = aNewPhone

    def days_to_birthday(self):
        # Method to calculate the number of days to the birthday
        if not self.user_birthday:
            return None

        current_datetime = datetime.now()
        this_year_birthday = datetime(
            year=current_datetime.year, month=self.user_birthday.month, day=self.user_birthday.day)
        return (this_year_birthday - current_datetime).days

