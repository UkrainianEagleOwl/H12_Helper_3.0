

import asyncio
import sys

# Define a function to redirect stdout to a file
def redirect_stdout_to_file(file_path):
    sys.stdout = open(file_path, 'w')
# Redirect stdout to a file
redirect_stdout_to_file('rasa_logs.txt')
from rasa.core.agent import Agent
from commands import commands

agent = Agent.load(
    'D:/Projects/H12_Helper_3.0/your_simple_helper/main/models/nlu-20230701-182601-knurled-charlie.tar.gz')


def find_command_by_name(command_name):
    for command in commands:
        if command["name"] == command_name:
            return command
    return None

def parse_input(input_string):
    intent = asyncio.run(agent.parse_message(input_string))
    return intent["intent"]["name"]

def parse_input_get_cmd(input_string):
    parsed_intent = parse_input(input_string)
    command = find_command_by_name(parsed_intent)
    return command

sys.stdout = sys.__stdout__
    


