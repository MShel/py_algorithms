class BubbleSorting:

    sortedArray = []

    def __init__(self, array_to_sort: list):
        self.bubble_sort(array_to_sort)

    def bubble_sort(self, arrayToSort: list):
        for j in range(0, len(arrayToSort)-1):
            i = len(arrayToSort) - 1
            while i > 0:
                if arrayToSort[i] < arrayToSort[i - 1]:
                    move_left = arrayToSort[i]
                    move_right = arrayToSort[i - 1]
                    arrayToSort[i - 1] = move_left
                    arrayToSort[i] = move_right
                i -= 1

        self.sortedArray = arrayToSort
