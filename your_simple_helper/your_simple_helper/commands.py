

import collections
import sys
from memory import AddressBook,Record
from pathlib import Path


END_STRING = "Good bye!"

address_book = AddressBook()
Person = collections.namedtuple('Person',['name','phone'])

#----------------------------------------
# Save and Load Address book when application begin and end work


def save_address_book(address_book):
    # Get the path of the executable file
    exe_path = Path(sys.executable)

    # Create the "save" folder if it doesn't exist
    save_folder = exe_path.parent / "save"
    save_folder.mkdir(exist_ok=True)

    # Construct the file path for saving the AddressBook
    file_path = save_folder / "address_book.json"

    # Save the AddressBook to the file
    address_book.save_to_json(file_path)

def load_address_book():
    # Get the path of the executable file
    exe_path = Path(sys.executable)

    # Create the "save" folder if it doesn't exist
    save_folder = exe_path.parent / "save"
    if save_folder.exists():
        # Construct the file path for loading the AddressBook
        file_path = save_folder / "address_book.json"

        # Check if the file exists
        if file_path.exists():
            # Load the AddressBook from the file
            address_book = AddressBook.load_from_json(file_path)
            return address_book
        else:
            return None
    else:
        return None


def input_error(func):
        def inner(name, phone):
            try:
                return func(name, phone)
            except KeyError:
                return "Can't find such person in contacts! Check the spelling of the entered name."
            except ValueError:
                return "Give me name and phone please."
        return inner       
        
def greetings(*arg):
    loaded_book = load_address_book()
    if loaded_book:
        global address_book 
        address_book = loaded_book
        s = 'Book was successfully load.'

    return "Hello Master! How can I help you today?" + s

@input_error
def add_new_contact(*arg):
    address_book.add_record(Record(arg[0].capitalize(),arg[1]))
    return 'Contact added.'

@input_error
def change_exist_contact(*arg):
    address_book.get(arg[0]).change_n_phone(0, arg[1])
    return f"Contact's phone was changed."

@input_error
def show_phone(*arg):
    return address_book.get(arg[0]).user_phones

def show_all(*arg):
    return [str(contact) for contact in address_book.values()]

def ending(*arg):
    global address_book
    save_address_book(address_book)
    return END_STRING + 'Book was successfully save.'

COMMANDS = {
    'hello' : greetings,
    'add' : add_new_contact,
    'change' : change_exist_contact,
    'phone' : show_phone,
    'show all': show_all,
    'good bye': ending,
    'close': ending,
    'exit' : ending
}

def get_command(command):
    return COMMANDS[command]
