import unittest
from translator import english_to_french, french_to_english

''' A class called TestTranslator with two methods that 
    each have two translation tests '''

class TestTranslator (unittest.TestCase):
    def test_english_to_french(self):
        # check that translation of 'Hello' equals 'Bonjour'
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # check that translation of 'two' equals 'deux'
        self.assertEqual(english_to_french('two'), 'deux')

    def test_french_to_english(self):
        # check that translation of 'Bonjour' equals 'Hello'
        self.assertEqual(french_to_english('Bonjour'), 'Hi')
        # check that translation of 'deux' equals 'two'
        self.assertEqual(french_to_english('deux'), 'two')

if __name__=='__main__':
    unittest.main()  
