import unittest
import random
import copy
from algos.sorting import BubbleSorting


class TestStringMethods(unittest.TestCase):

    testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    originalArray = copy.copy(testArray)

    def __init__(self, method):
        super().__init__(method)
        random.shuffle(self.testArray)

    def test_bubble_sorting(self):
        bubbleSortedArray = BubbleSorting.BubbleSorting(self.testArray).sortedArray
        self.assertEqual(bubbleSortedArray, self.originalArray)

    def test

if __name__ == '__main__':
    unittest.main()
