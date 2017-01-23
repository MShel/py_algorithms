class InsertionSorting:
    sortedArray = []

    def __init__(self, array_to_sort: list):
        self.insertion_sort(array_to_sort)

    def insertion_sort(self, arrayToSort: list):
        for i in range(1, len(arrayToSort)):
            current_element = arrayToSort[i]
            self.swap_members(i, current_element, arrayToSort)
        self.sortedArray = arrayToSort

    def swap_members(self, i: int, current_number: int, arrayToSort: list):
        if i > 0:
            j = i
            while j > 0:
                if current_number < arrayToSort[j - 1]:
                    left_element = current_number
                    right_element = arrayToSort[j - 1]
                    arrayToSort[j - 1] = left_element
                    arrayToSort[j] = right_element
                else:
                    #no need to go more the left we get element that is bigger
                    break
                j -= 1
