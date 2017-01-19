class SelectionSorting:

    sortedArray = []

    def __init__(self, array_to_sort: list):
        self.selection_sort(array_to_sort)

    def selection_sort(self, arrayToSort: list):
        for i in range(0, len(arrayToSort)):
            element, index_to_move_to = self.get_min_element(arrayToSort)
            arrayToSort[index_to_move_to] = arrayToSort[0]
            arrayToSort[0] = element

        self.sortedArray = arrayToSort

    def get_min_element(self, arrayToSort:list)->tuple:
        i = len(arrayToSort)-1
        min_element = (arrayToSort[i], i)
        while i > 0:
            if min_element[0] >= arrayToSort[i]:
                min_element = (arrayToSort[i], i)
            i -= 1
        return min_element
