""" Testing for camelCase functions """

import unittest
import camelCase
from unittest import TestCase


class TestCamelCase(TestCase):
    # tests functionality of taking input string and returning in camelCase
    def test_camelcase_sentence(self):
        user_sentence = 'Hello World'
        expected_result = 'helloWorld'
        self.assertEqual(expected_result, camelCase.camelcase(user_sentence))

    # checks to see if any input string returns with only first letter of each word capitalized
    def test_capitalize_first_letters(self):
        potential_inputs = ['HELLO', 'hello', 'heLLO', 'HELlo']
        expected_capitalization = 'HelloHelloHelloHello'
        self.assertEqual(expected_capitalization, camelCase.capitalize_first_letters(potential_inputs))

    # checks if any amount of extra spaces are removed from input string
    def test_remove_all_whitespace_from_input_sentence(self):
        input_sentence = '    The   weather            is    delightful  today     '
        expected_return_string = 'The weather is delightful today'
        self.assertEqual(expected_return_string, camelCase.remove_space(input_sentence))

    if __name__ == '__main__':
        unittest.main()
