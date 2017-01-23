class SelectionSorting:
    sortedArray = []

    def __init__(self, array_to_sort: list):
        self.selection_sort(array_to_sort)

    def selection_sort(self, arrayToSort: list):
        for i in range(0, len(arrayToSort)):
            possible_element_to_move = arrayToSort[i]
            element, index_to_move_to = self.get_min_element(arrayToSort[i:])
            if element < possible_element_to_move:
                arrayToSort[index_to_move_to + i] = possible_element_to_move
                arrayToSort[i] = element
        self.sortedArray = arrayToSort

    def get_min_element(self, arrayToSort: list) -> tuple:
        i = len(arrayToSort) - 1
        min_element = (arrayToSort[i], i)
        while i > 0:
            if min_element[0] >= arrayToSort[i]:
                min_element = (arrayToSort[i], i)
            i -= 1
        return min_element
