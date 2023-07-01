import unittest
from your_simple_helper import save_load_book
from memory import AddressBook
from save_load_book import load_address_book,save_address_book
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys


class TestAddressBookFunctions(unittest.TestCase):
    def setUp(self):
        self.address_book = AddressBook()

    def tearDown(self):
        # Remove the save folder after each test
        save_folder = Path(sys.executable).parent / "save"
        if save_folder.exists():
            save_folder.rmdir()

    def test_save_address_book(self):
        # Mock the AddressBook.save_to_json method
        mock_save_to_json = MagicMock()
        self.address_book.save_to_json = mock_save_to_json

        # Call the save_address_book function
        save_address_book(self.address_book)

        # Verify that the AddressBook.save_to_json method was called with the correct file path
        exe_path = Path(sys.executable)
        save_folder = exe_path.parent / "save"
        file_path = save_folder / "address_book.json"
        mock_save_to_json.assert_called_once_with(file_path)

        # Verify that the save folder and file were created
        self.assertTrue(save_folder.exists())
        self.assertTrue(file_path.exists())

    def test_load_address_book(self):
        # Create a temporary save folder and file
        save_folder = Path(sys.executable).parent / "save"
        save_folder.mkdir()
        file_path = save_folder / "address_book.json"
        file_path.touch()

        # Mock the AddressBook.load_from_json method
        mock_load_from_json = MagicMock(return_value=self.address_book)
        AddressBook.load_from_json = mock_load_from_json

        # Call the load_address_book function
        loaded_address_book = load_address_book()

        # Verify that the AddressBook.load_from_json method was called with the correct file path
        mock_load_from_json.assert_called_once_with(file_path)

        # Verify that the loaded address book matches the expected address book
        self.assertEqual(loaded_address_book, self.address_book)

        # Remove the temporary save folder and file
        file_path.unlink()
        save_folder.rmdir()

    def test_load_address_book_no_folder(self):
        # Mock the AddressBook.load_from_json method
        mock_load_from_json = MagicMock()
        AddressBook.load_from_json = mock_load_from_json

        # Call the load_address_book function
        loaded_address_book = load_address_book()

        # Verify that the AddressBook.load_from_json method was not called
        mock_load_from_json.assert_not_called()

        # Verify that None is returned
        self.assertIsNone(loaded_address_book)

    def test_load_address_book_no_file(self):
        # Create a temporary save folder without the file
        save_folder = Path(sys.executable).parent / "save"
        save_folder.mkdir()

        # Mock the AddressBook.load_from_json method
        mock_load_from_json = MagicMock()
        AddressBook.load_from_json = mock_load_from_json

        # Call the load_address_book function
        loaded_address_book = load_address_book()

        # Verify that the AddressBook.load_from_json method was not called
        mock_load_from_json.assert_not_called()

        # Verify that None is returned
        self.assertIsNone(loaded_address_book)

        # Remove the temporary save folder
        save_folder.rmdir()


if __name__ == '__main__':
    unittest.main()


