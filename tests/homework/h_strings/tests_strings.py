import unittest
from src.homework.h_strings.strings import Get_Hamming_Distance
from src.homework.h_strings.strings import Get_DNA_Complement
class Test_Config(unittest.TestCase):

   def test_Get_Hamming_Distance(self):
       self.assertEqual(Get_Hamming_Distance('GAGCCTACTAACGGGAT','CATCGTAATGACGGCCT'),7)
    
   def test_Get_DNA_Complement(self):
       self.assertEqual(Get_DNA_Complement('AAAACCCGGT'),'ACCGGGTTTT')