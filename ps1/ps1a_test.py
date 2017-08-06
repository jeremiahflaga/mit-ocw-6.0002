import unittest
from ps1a import *

class TestGlobalMethods(unittest.TestCase):
    
    def test_load_cows(self):
        dict = load_cows('ps1_cow_small_data.txt')
        self.assertDictEqual({ 'Maggie':3, 'Herman':7 }, dict)
        
    def test_greedy_cow_transport_1(self):
        cows_dict = { 'Maggie':3, 'Herman':7 }
        result = greedy_cow_transport(cows_dict, 10)
        self.assertListEqual([['Herman', 'Maggie']], result)
        
    def test_greedy_cow_transport_2(self):
        cows_dict = { 'Maggie':3, 'Herman':7, 'Betsy': 9 }
        result = greedy_cow_transport(cows_dict, 10)
        self.assertListEqual([['Betsy'], ['Herman', 'Maggie']], result)
        
    def test_greedy_cow_transport_4(self):
        cows_dict = { 'Maggie':3, 'Herman':7, 'Betsy': 9, 'Oreo':6 }
        result = greedy_cow_transport(cows_dict, 10)
        self.assertListEqual([['Betsy'], ['Herman', 'Maggie'], ['Oreo']], result)
        
    def test_greedy_cow_transport_5(self):
        cows_dict = { 'Maggie':3, 'Herman':7, 'Betsy': 9, 'Oreo':6, 'Moo Moo':3 }
        result = greedy_cow_transport(cows_dict, 10)
        self.assertListEqual([['Betsy'], ['Herman', 'Maggie'], ['Oreo', 'Moo Moo']], result)
        
    def test_greedy_cow_transport_6(self):
        cows_dict = { 'Jessie':6, 'Maybel':3, 'Callie': 2, 'Maggie':5 }
        result = greedy_cow_transport(cows_dict, 10)
        self.assertListEqual([['Jessie', 'Maybel'], ['Maggie', 'Callie']], result)
        
if __name__ == '__main__':
    unittest.main()