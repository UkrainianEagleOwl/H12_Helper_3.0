

import collections
from save_load_book import load_address_book, save_address_book
from memory import AddressBook, Record
from open_ai_input_assistent import analize_input_activate_func


END_STRING = "Good bye!"
address_book = AddressBook()
Person = collections.namedtuple('Person',['name','phone'])

def get_command_input(Input_message=''):
    Input_value = None
    while Input_value is None:
        Input_value = input(f'{Input_message} ')
    return Input_value

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
    s = ''
    if loaded_book:
        global address_book 
        address_book = loaded_book
        s = 'Book was successfully load.'

    return analize_input_activate_func(command=commands[0]) + s

@input_error
def add_new_contact(*arg):
    address_book.add_record(Record(arg[0].capitalize(),arg[1]))
    #return 'Contact added.'

@input_error
def change_exist_contact(*arg):
    address_book.get(arg[0]).change_n_phone(0, arg[1])
    #return f"Contact's phone was changed."

@input_error
def show_phone(*arg):
    return address_book.get(arg[0]).user_phones

def show_all(*arg):
    return [str(contact) for contact in address_book.values()]

def ending(*arg):
    global address_book
    save_address_book(address_book)
    return analize_input_activate_func(command=commands[5]) + 'Book was successfully save.'

# Define available commands
commands = [
    {
        "id": 1,
        "name": "greet",
        "description": "Greet the user",
        "arguments": [],
        "func":greetings
    },
    {
        "id": 2,
        "name": "add_new_contact",
        "description": "Add a new contact",
        "arguments": ["name", "phone"],
        "func":add_new_contact
    },
    {
        "id": 3,
        "name": "change_exist_contact",
        "description": "Change an existing contact",
        "arguments": ["name"],
        "func":change_exist_contact
    },
    {
        "id": 4,
        "name": "show_phone",
        "description": "Show the phone number of a contact",
        "arguments": ["name"],
        "func":show_phone
    },
    {
        "id": 5,
        "name": "show_all",
        "description": "Show all contacts",
        "arguments": [],
        "func":show_all
    },
    {
        "id": 6,
        "name": "ending",
        "description": "End the conversation",
        "arguments": [],
        "func":ending
    }
    ]

def get_command(id):
    return list(filter(lambda cmd: cmd["id"] == id, commands))[0]
