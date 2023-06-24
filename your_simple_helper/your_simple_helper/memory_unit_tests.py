import memory
import unittest
from datetime import datetime

def Create_simple_record(name = 'Alex'):
    return memory.Record(name, '+380(50)543-5-391', datetime(year=1970, month=11, day=7))


class AddressBookTest(unittest.TestCase):
    def test_add_record(self):
        address_book = memory.AddressBook()
        record = Create_simple_record()
        address_book.add_record(record)
        self.assertIn(record.user_name.value, address_book.data)

    def test_find_in_values(self):
        address_book = memory.AddressBook()
        record = memory.Record("John Doe", '+380(50)543-5-391',datetime(year=1970, month=11, day=7))
        address_book.add_record(record)
        result = address_book.find_in_values(record)
        self.assertEqual(result, ("John Doe", record))

    def test_address_book_iterator(self):
        address_book = memory.AddressBook()
        record1 = memory.Record("John Doe")
        record2 = memory.Record("Jane Smith")
        record3 = memory.Record("Bob Johnson")
        address_book.add_record(record1)
        address_book.add_record(record2)
        address_book.add_record(record3)

        iterator = iter(address_book)
        self.assertEqual(next(iterator), repr(record1))
        self.assertEqual(next(iterator), repr(record2))
        self.assertEqual(next(iterator), repr(record3))
        self.assertRaises(StopIteration, next, iterator)

class NameTest(unittest.TestCase):
    def test_get_set_value(self):
        name = memory.Name('Alex')            
        with self.assertRaises(memory.SetterValueIncorrect):
            name.value = 123
        self.assertEqual(name.value, 'Alex')

class PhoneTest(unittest.TestCase):
    def test_get_set_value(self):
        phone = memory.Phone('+380(50)543-5-391')
        with self.assertRaises(memory.SetterValueIncorrect):
            phone.value = 123
        with self.assertRaises(memory.SetterValueIncorrect):
            phone.value = 'Anna'
        with self.assertRaises(memory.SetterValueIncorrect):
            phone.value = '380(67)7778-77-776'
        self.assertEqual(phone.value, '+380(50)543-5-391')


class BirthdayTestCase(unittest.TestCase):
    def test_value_property(self):
        # Test the getter and setter of the value property
        birthday = memory.Birthday()

        # Test setting the value with a valid datetime object
        valid_datetime = datetime(year=2000, month=1, day=1)
        birthday.value = valid_datetime
        self.assertEqual(birthday.value, valid_datetime)

        # Test setting the value with a valid string representation
        valid_string = "1 January 2000"
        birthday.value = valid_string
        self.assertEqual(birthday.value, valid_datetime)

        # Test setting the value with an invalid string representation
        invalid_string = "Invalid Date"
        with self.assertRaises(memory.SetterValueIncorrect):
            birthday.value = invalid_string

        # Test setting the value with an invalid type
        invalid_type = 123
        with self.assertRaises(memory.SetterValueIncorrect):
            birthday.value = invalid_type


class RecordTestCase(unittest.TestCase):
    def test_add_phone(self):
        # Test adding a phone to the record
        record = memory.Record("John Doe")
        phone = '+380(50)543-5-391'
        record.add_phone(phone)

        self.assertEqual(len(record.user_phones), 1)
        self.assertEqual(record.user_phones[0].value, phone)

    def test_remove_phone(self):
        # Test removing a phone from the record
        record = memory.Record("John Doe")
        phone = '+380(50)543-5-391'
        record.add_phone(phone)

        record.remove_phone(phone)

        self.assertEqual(len(record.user_phones), 0)

    def test_days_to_birthday(self):
        # Test calculating the number of days to the birthday
        record = memory.Record("John Doe", birthday=datetime.now())

        days = record.days_to_birthday()

        self.assertIsNotNone(days)

    def test_remove_n_phone(self):
        # Test removing a phone at a specified index from the record
        record = memory.Record("John Doe")
        phones = ['+380(50)566-5-391', '+380(93)345-5-391','+380(50)543-8-391']
        for phone in phones:
            record.add_phone(phone)

        index_to_remove = 1
        record.remove_n_phone(index_to_remove)

        self.assertEqual(len(record.user_phones), len(phones) - 1)
        self.assertNotIn(phones[index_to_remove], [
                         phone.value for phone in record.user_phones])

    def test_change_n_phone(self):
        # Test changing a phone at a specified index in the record
        record = memory.Record("John Doe")
        phones = ['+380(50)566-5-391', '+380(93)345-5-391','+380(50)543-8-391']
        for phone in phones:
            record.add_phone(phone)

        index_to_change = 0
        new_phone = '66666666666'
        with self.assertRaises(memory.SetterValueIncorrect):
            record.change_n_phone(index_to_change, new_phone)
        new_phone = '+380(93)666-6-666'
        record.change_n_phone(index_to_change, new_phone)

        self.assertEqual(record.user_phones[index_to_change].value, new_phone)


if __name__ == '__main__':
    unittest.main()
