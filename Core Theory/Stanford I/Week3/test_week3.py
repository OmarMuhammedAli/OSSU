import unittest
from quicksort import quicksort
from randomizedQuicksort import randomized_quicksort

class TestQuicksort(unittest.TestCase):
    def setUp(self):
        with open('quicksort.txt') as fhand:
            self.test_cases = [int(line) for line in fhand]
    
    def test_num_of_comparisons_for_median_of_three(self):
        self.assertEqual(quicksort(self.test_cases), 138382)
    
    def test_quicksort(self):
        quicksort(self.test_cases)
        self.assertEqual(self.test_cases, sorted(self.test_cases))


class TestRandomizedQuicksort(unittest.TestCase):
    def setUp(self):
        with open('quicksort.txt') as fhand:
            self.test_cases = [int(line) for line in fhand]
    
    def test_quicksort(self):
        quicksort(self.test_cases)
        self.assertEqual(self.test_cases, sorted(self.test_cases))


if __name__ == '__main__':
    unittest.main()