import unittest

from translator import english_to_french, english_to_german

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        # Text translation: 3 tests
        self.assertEqual(english_to_french("How are you today?"), "Comment es-tu aujourd'hui?") 
        self.assertEqual(english_to_french("Welcome"), "Bienvenue")
        self.assertEqual(english_to_french("I love to learn"), "J'adore apprendre")
        #test for null input
        self.assertIsNone(english_to_french(), None)
        #test for the translation of the word 'Hello' 
        self.assertEqual(english_to_french("Hello"), "Bonjour")


class TestEnglishToGerman(unittest.TestCase): 
    def test1(self):
        # Text translation: 3 tests
        self.assertEqual(english_to_german("What is your name?"), "Wie lautet Ihr Name?") 
        self.assertEqual(english_to_german("How old are you?"), "Wie alt sind Sie?")
        self.assertEqual(english_to_german("Thank you"), "Danke.")
        #test for null input
        self.assertIsNone(english_to_german(), None)
        #test for the translation of the word 'Hello' 
        self.assertEqual(english_to_german("Hello"), "Hallo")

        
unittest.main()