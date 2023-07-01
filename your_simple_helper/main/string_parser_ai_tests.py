
import unittest
from unittest.mock import patch
from string_parser_ai import parse_input_get_cmd
from commands import greetings, add_new_contact, change_exist_contact, show_phone, show_all, ending


class TestParseInputGetCmd(unittest.TestCase):
    def test_parse_input_get_cmd_greet(self):
        input_string = "Hello assistant"
        expected_command = {
            "id": 1,
            "name": "greet",
            "description": "Greet the user",
            "arguments": [],
            "func": greetings
        }
        result = parse_input_get_cmd(input_string)
        self.assertEqual(result, expected_command)

    def test_parse_input_get_cmd_add_new_contact(self):
        input_string = "Please, add a new contact"
        expected_command = {
            "id": 2,
            "name": "add_new_contact",
            "description": "Add a new contact",
            "arguments": ["name", "phone"],
            "func": add_new_contact
        }
        result = parse_input_get_cmd(input_string)
        self.assertEqual(result, expected_command)

    def test_parse_input_get_cmd_change_exist_contact(self):
        input_string = "I want to change an existing contact"
        expected_command = {
            "id": 3,
            "name": "change_exist_contact",
            "description": "Change an existing contact",
            "arguments": ["name"],
            "func": change_exist_contact
        }
        result = parse_input_get_cmd(input_string)
        self.assertEqual(result, expected_command)

    def test_parse_input_get_cmd_show_phone(self):
        input_string = "Can you show the phone number of a contact"
        expected_command = {
            "id": 4,
            "name": "show_phone",
            "description": "Show the phone number of a contact",
            "arguments": ["name"],
            "func": show_phone
        }
        result = parse_input_get_cmd(input_string)
        self.assertEqual(result, expected_command)

    def test_parse_input_get_cmd_show_all(self):
        input_string = "I want to see all contacts. Show me"
        expected_command = {
            "id": 5,
            "name": "show_all",
            "description": "Show all contacts",
            "arguments": [],
            "func": show_all
        }
        result = parse_input_get_cmd(input_string)
        self.assertEqual(result, expected_command)

    def test_parse_input_get_cmd_ending(self):
        input_string = "Good bye"
        expected_command = {
            "id": 6,
            "name": "ending",
            "description": "End the conversation",
            "arguments": [],
            "func": ending
        }
        result = parse_input_get_cmd(input_string)
        self.assertEqual(result, expected_command)


if __name__ == '__main__':
    unittest.main()
