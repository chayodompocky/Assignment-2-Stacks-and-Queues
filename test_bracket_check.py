def bracket_check(input_string):
    stack = []  # Initialize an empty stack
    errors = []  # Initialize a list to store errors

    # Create a dictionary to map opening and closing brackets
    brackets = {"(": ")", "{": "}", "[": "]"}

    for i, char in enumerate(input_string):
        if char in brackets.keys():
            # Found an opening bracket
            stack.append((char, i))
        elif char in brackets.values():
            # Found a closing bracket
            if not stack:
                errors.append((char, i))
            else:
                top, position = stack.pop()
                if brackets[top] != char:
                    errors.append((top, position))

    while stack:
        top, position = stack.pop()
        errors.append((top, position))

    return errors

import unittest

class MyTestCase(unittest.TestCase):
    def test_no_error(self):
        test_string = '[{(Hello)}]'
        errors = bracket_check(test_string)
        self.assertEqual(errors, [])

    def test_error_1(self):
        test_string = '[{(Hello})]'
        errors = bracket_check(test_string)
        expected_errors = [("'", 8)]
        self.assertEqual(errors, expected_errors)

    def test_error_2(self):
        test_string = '[{(Hello'
        errors = bracket_check(test_string)
        expected_errors = [("'", 7), ("]", 5)]
        self.assertEqual(errors, expected_errors)

    def test_error_3(self):
        test_string = 'Hello)('
        errors = bracket_check(test_string)
        expected_errors = [("'", 5), ("(", 6), ("Hello", 0)]
        self.assertEqual(errors, expected_errors)

    def test_error_4(self):
        test_string = '{}{'
        errors = bracket_check(test_string)
        expected_errors = [("{", 0)]
        self.assertEqual(errors, expected_errors)

if __name__ == '__main__':
    unittest.main()
