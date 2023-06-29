

from commands import get_command, END_STRING,greetings
from string_parser import parse_the_string #, command_work_tulpe
from open_ai_input_assistent import analize_input_activate_func,activate_openai
from commands import get_command_input
from cryptography.fernet import Fernet
from my_secrets import KEY,OPENAI_KEY_ENCRYPTED

def crypt_key():
    fernet = Fernet(KEY)
    return fernet.decrypt(OPENAI_KEY_ENCRYPTED)

def main():
    activate_openai(crypt_key())
    print(greetings())
    while True:
        input_string = get_command_input()
        #here is parse input function that get back command or None
        command = {} #the example of command for next algorithm
        if command:
            if len(command['arguments']) > 0:
                print(analize_input_activate_func(command, input_string))
                input_string = get_command_input()
                #here is parse input for getting arguments belong to command
                cmd_func = get_command(command[id])
                #call the func with arguments that we get from parse
            if command["name"] == 'exit':
                print(analize_input_activate_func(command))
                break
            else:
                print(analize_input_activate_func(command, iteration_done = True))
        else:
            print(analize_input_activate_func(customer_input=input_string))

if __name__ == '__main__':
    main()
