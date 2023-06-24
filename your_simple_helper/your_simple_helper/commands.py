import collections


END_STRING = "Good bye!"

contacts = {}
Person = collections.namedtuple('Person',['name','phone'])


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
    return "How can I help you?"

@input_error
def add_new_contact(*arg):
    contacts[arg[0]] = arg[1]
    return 'Contact added.'

@input_error
def change_exist_contact(*arg):
    old_number = contacts[arg[0]]
    contacts[arg[0]] = arg[1]
    return f"Contact's phone was changed."

@input_error
def show_phone(*arg):
    return contacts[arg[0]]

def show_all(*arg):
    return [f"Name: {key.capitalize()}, Phone: {value}" for key, value in contacts.items()]

def ending(*arg):
    return END_STRING

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
