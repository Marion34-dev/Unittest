import unittest
from myfunc import cap_text, add_numbers, find_max_length_word


class TestMyFunc(unittest.TestCase):

    def test_cap_text_one_word(self):
        text = 'hello'
        result = cap_text(text)
        self.assertEqual(result, 'Hello')

    def test_cap_text_multiple_words(self):
        text = 'welcome home'
        result = cap_text(text)
        self.assertEqual(result, 'Welcome Home')

    def test_cap_text_string_empty(self):
        result = cap_text("")
        self.assertEqual(result, "", "Should be an empty string")


    def test_add_numbers_positive(self):
        result = add_numbers(3, 5)
        self.assertEqual(result, 8, "Should be 8")

    def test_add_numbers_negative(self):
        result = add_numbers(-2, 7)
        self.assertEqual(result, 5, "Should be 5")

    def test_add_numbers_zero(self):
        result = add_numbers(0, 0)
        self.assertEqual(result, 0, "Should be 0")


    def test_find_max_length_word(self):
        result = find_max_length_word("This is a simple test")
        self.assertEqual(result, "simple", "Should be 'simple'")

    def test_find_max_length_word_empty(self):
        result = find_max_length_word("")
        self.assertIsNone(result, "Should be None for an empty string")

    def test_find_max_length_word_multiple_longest(self):
        result = find_max_length_word("Python is better but Java is also great")
        self.assertEqual(result, "Python", "Should be 'Python' as it appears first")


if __name__ == '__main__':
    unittest.main()
