from rasa.nlu.model import Interpreter
import rasa

interpreter = rasa.Interpreter.load('D:/Projects/H12_Helper_3.0/your_simple_helper/your_simple_helper/parser_ai/models/nlu-20230630-185023-crimson-burger.tar.gz')

def parse_input(input_string):
    intent = interpreter.parse(input_string)["intent"]["name"]
    return intent
