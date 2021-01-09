import unittest
from mergesort import *
from karatsuba import karatsuba


class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):
        self.assertEqual(merge_sort([9, 8, 3, 7, 4, 1, 5, 6, 3, 7]), [
                         1, 3, 3, 4, 5, 6, 7, 7, 8, 9])


class TestKaratsuba(unittest.TestCase):

    def test_karatsuba(self):
        self.assertEqual(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                                   2718281828459045235360287471352662497757247093699959574966967627), 
                                   8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184)


if __name__ == "__main__":
    unittest.main()
