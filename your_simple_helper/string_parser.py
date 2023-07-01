import collections


command_work_tulpe = collections.namedtuple(
    'command_work_tulpe', ['command', 'name','phone'])

COMMANDS_CHECK = ('hello','add','change','phone','show','good','close','exit')


def input_error(func):
        def inner(input_string):
            try:
                return func(input_string)
            except:
                "Unknown command. Please try another command."
        return inner

@input_error
def parse_the_string(input_string):
    input_string = input_string.lower()
    words = input_string.split(' ')
    if words[0] in COMMANDS_CHECK:
        if ((words[0] == 'show') or(words[0] == 'good')) and len(words) > 1:
            c = words.pop(0) + ' ' + words.pop(0)
            if c == 'show all' or 'good bye':
                com = c
            else:
                return "Unknown command. Please try another command."
        else:
            com = words.pop(0)
    else:
        return "Unknown command. Please try another command."
    if words:
        name = words.pop(0)
    else:
        name = ''
    if words:
        phone = words.pop(0)
    else:
        phone = ''
    return command_work_tulpe(com,name,phone)
