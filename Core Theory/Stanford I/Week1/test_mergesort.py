import unittest
from mergesort import *

class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):
        self.assertEqual(merge_sort([9,8,3,7,4,1,5,6,3,7]), [1,3,3,4,5,6,7,7,8,9])

if __name__ == "__main__":
    unittest.main()