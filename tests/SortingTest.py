import unittest
import random
import copy
from algos.sorting import BubbleSorting
from algos.sorting import SelectionSorting
from algos.sorting import InsertionSorting


class TestStringMethods(unittest.TestCase):

    testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    originalArray = copy.copy(testArray)

    def test_bubble_sorting(self):
        random.shuffle(self.testArray)
        bubbleSortedArray = BubbleSorting.BubbleSorting(self.testArray).sortedArray
        self.assertEqual(bubbleSortedArray, self.originalArray)

    def test_selection_sort(self):
        random.shuffle(self.testArray)
        selection_sorted_array = SelectionSorting.SelectionSorting(self.testArray).sortedArray
        self.assertEqual(selection_sorted_array, self.originalArray)

    def test_insertion_sort(self):
        random.shuffle(self.testArray)
        insertion_sorted_array = InsertionSorting.InsertionSorting(self.testArray).sortedArray
        self.assertEqual(insertion_sorted_array, self.originalArray)

if __name__ == '__main__':
    unittest.main()
