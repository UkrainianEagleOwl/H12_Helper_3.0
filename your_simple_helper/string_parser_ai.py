

from rasa.core.agent import Agent
import asyncio
from commands import commands

def parse_input(input_string):
    agent = Agent.load(
        'D:/Projects/H12_Helper_3.0/your_simple_helper/your_simple_helper/parser_ai/models/nlu-20230630-185023-crimson-burger.tar.gz')
    intent = asyncio.run(agent.parse_message(input_string))
    return intent["intent"]["name"]

def parse_input_get_cmd(input_string):
    parsed_intent = parse_input(input_string)
    return list(filter(lambda cmd: cmd["name"] == parsed_intent, commands))[0]
    


