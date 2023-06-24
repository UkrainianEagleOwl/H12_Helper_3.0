from commands import get_command, END_STRING
from string_parser import parse_the_string #, command_work_tulpe


def get_command_input(Input_message=''):
    Input_value = None
    while Input_value is None:
            Input_value = input(f'{Input_message} ')
    return Input_value

def main():
    while True:
        input_string = get_command_input()
        work_tuple = parse_the_string(input_string)
        if isinstance(work_tuple,str):
            print(work_tuple)
        else:
            answer = get_command(work_tuple[0])(work_tuple[1], work_tuple[2])
            if isinstance(answer, list):
                for i in answer: print(i)
            else:
                print(answer)
            if answer == END_STRING:
                break

if __name__ == '__main__':
    main()
