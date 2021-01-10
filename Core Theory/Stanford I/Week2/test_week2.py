import unittest
from counting_inversions import count_inversions

class TestCountingInversions(unittest.TestCase):
    
    def setUp(self):
        self.test_cases = [int(line) for line in open('testcases.txt')]

    def test_count_inversions(self):
        self.assertEqual(count_inversions(self.test_cases), 2407905288)


if __name__ == '__main__':
    unittest.main()