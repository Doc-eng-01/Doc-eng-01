import unittest
from translator import english_to_french, french_to_english


class TestTranslation(unittest.TestCase):
    def test_english_to_french_first(self):  # checking for correct response
        self.assertEqual(english_to_french('Hello'), "Bonjour")

# checking for correct response
    def test_french_to_english_first(self):
        self.assertEqual(french_to_english('Bonjour'), "Hello")
# checking for empty input

    def test_english_to_french_second(self):
        self.assertNotEqual(english_to_french(''), "None")

# checking for empty input
    def test_french_to_english_second(self):
        self.assertNotEqual(french_to_english(''), "None")


if __name__ == '__main__':
    unittest.main()
