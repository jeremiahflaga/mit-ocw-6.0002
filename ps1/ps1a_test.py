import unittest
from ps1a import *
from gen_subsets import genSubsets

class TestLoadCows(unittest.TestCase):    
    def test_load_cows(self):
        dict = load_cows('ps1_cow_small_data.txt')
        self.assertDictEqual({ 'Maggie':3, 'Herman':7 }, dict)
        

class TestGreedyCowsTransport(unittest.TestCase):    
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
        


# NOTE: I think the kind of testing I'm doing with the Brute Force solution has an error in here somewhere
class TestBruteForceCowsTransport(unittest.TestCase):
    
    def test_brute_force_cow_transport_1(self):
        cows_dict = { 'Maggie':3, 'Herman':7 }
        # partitions = get_partitions(cows_dict.keys())
        # print('partitions: ')
        # for partition in partitions:
        #     print(partition)
        result = brute_force_cow_transport(cows_dict, 10)
        self.assertTrue([['Herman', 'Maggie']] == result
                        or [['Maggie', 'Herman']] == result)
        
    def test_brute_force_cow_transport_2(self):
        cows_dict = { 'Maggie':3, 'Herman':7, 'Betsy': 9 }
        result = brute_force_cow_transport(cows_dict, 10)
        self.assertTrue(result in genSubsets([['Betsy'], ['Herman', 'Maggie']])
                        or result in genSubsets([['Betsy'], ['Maggie', 'Herman']]))
        
    def test_greedy_cow_transport_4(self):
        cows_dict = { 'Maggie':3, 'Herman':7, 'Betsy': 9, 'Oreo':6 }
        result = greedy_cow_transport(cows_dict, 10)
        self.assertTrue(result in genSubsets([['Betsy'], ['Herman', 'Maggie'], ['Oreo']])
                        or result in genSubsets([['Betsy'], ['Maggie', 'Herman'], ['Oreo']]))
        
    def test_greedy_cow_transport_5(self):
        cows_dict = { 'Maggie':3, 'Herman':7, 'Betsy': 9, 'Oreo':6, 'Moo Moo':3 }
        result = greedy_cow_transport(cows_dict, 10)
        self.assertTrue(result in genSubsets([['Betsy'], ['Herman', 'Maggie'], ['Oreo', 'Moo Moo']])
                        or result in genSubsets([['Betsy'], ['Maggie', 'Herman'], ['Oreo', 'Moo Moo']])
                        or  result in genSubsets([['Betsy'], ['Herman', 'Maggie'], ['Moo Moo', 'Oreo']])
                        or result in genSubsets([['Betsy'], ['Maggie', 'Herman'], ['Moo Moo', 'Oreo']]))
        
    def test_greedy_cow_transport_6(self):
        cows_dict = { 'Jessie':6, 'Maybel':3, 'Callie': 2, 'Maggie':5 }
        result = greedy_cow_transport(cows_dict, 10)
        self.assertTrue(
            result in genSubsets([
                genSubsets(['Jessie', 'Maybel']), 
                genSubsets(['Maggie', 'Callie'])
            ])
        )
        
    def test_greedy_cow_transport_6(self):
        cows_dict = { 'Jessie':6, 'Maybel':3, 'Callie': 2, 'Maggie':5 }
        result = greedy_cow_transport(cows_dict, 10)
        self.assertTrue(result in genSubsets([['Jessie', 'Maybel'], ['Maggie', 'Callie']])
                        or result in genSubsets([['Maybel', 'Jessie'], ['Maggie', 'Callie']])
                        or result in genSubsets([['Jessie', 'Maybel'], ['Callie', 'Maggie']])
                        or result in genSubsets([['Maybel', 'Jessie'], ['Callie', 'Maggie']])
                        )        


if __name__ == '__main__':
    unittest.main()