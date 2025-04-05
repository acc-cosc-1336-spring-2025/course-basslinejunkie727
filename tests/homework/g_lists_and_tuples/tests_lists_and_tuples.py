import unittest
from src.homework.g_lists_and_tuples.lists import get_highest_number
from src.homework.g_lists_and_tuples.lists import get_lowest_number

def test_get_highest_number(self):
    self.assertEqual(get_highest_number(8,10,1,50,20),50)

def test_get_lowest_number(self):
    self.assertEqual(get_lowest_number(8,10,1,50,20),1)