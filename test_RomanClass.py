import unittest
from RomanClass import *

class RomanNumberTest(unittest.TestCase):
    def test_Compare(self):
        eleven = RomanNumber(11)
        twelve = RomanNumber(12)
        self.assertTrue(eleven<twelve)
        self.assertFalse(twelve<eleven)
        self.assertTrue(twelve > eleven)
    def test_operations(self):
        eleven = RomanNumber(11)
        twelve = RomanNumber(12)
        self.assertEqual(eleven+twelve, RomanNumber(23))
        self.assertEqual(twelve-eleven, RomanNumber(1))
        with self.assertRaises(ValueError):
            eleven - twelve

        