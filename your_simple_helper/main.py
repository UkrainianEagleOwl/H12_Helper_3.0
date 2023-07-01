

from commands import get_command, END_STRING,greetings
from parser_ai.string_parser_ai import parse_input_get_cmd 
from open_ai_input_assistent import analize_input_activate_func,activate_openai
from commands import get_command_input
from cryptography.fernet import Fernet
from my_secrets import KEY,OPENAI_KEY_ENCRYPTED

def crypt_key():
    fernet = Fernet(KEY)
    return fernet.decrypt(OPENAI_KEY_ENCRYPTED)

def main():
    activate_openai(crypt_key().decode())
    print(greetings())
    while True:
        input_string = get_command_input()
        #parse input function that get back command or None
        command = parse_input_get_cmd(input_string)
        if command:
            if len(command['arguments']) > 0:
                print(analize_input_activate_func(command, input_string))
                input_string = get_command_input()
                list(input_string.split(','))
                cmd_func = get_command(command[id])
                cmd_func(*list)
            if command["name"] == 'exit':
                print(analize_input_activate_func(command))
                break
            else:
                print(analize_input_activate_func(command, iteration_done = True))
        else:
            print(analize_input_activate_func(customer_input=input_string))

if __name__ == '__main__':
    main()
