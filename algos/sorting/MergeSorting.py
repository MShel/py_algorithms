class MergeSorting:
    sortedArray = []
    resultSplitted = []
    splited_groups = []

    def __init__(self, array_to_sort: list):
        self.sortedArray = self.merge_sort(array_to_sort)

    def merge_sort(self, array_to_sort: list) -> list:
        # splitting initial list in half's
        initial_left_group, initial_right_group = self.split_the_group(array_to_sort)

        # turning list of values into list of lists of values
        self.split(initial_left_group)
        self.split(initial_right_group)

        # now splitting this big list into 2
        left_group_to_sort, right_group_to_sort = self.split_the_group(self.splited_groups)

        # combining our list back into groupd of 2 but sorting them low->high
        combined_group_left = self.combine_group(left_group_to_sort)
        combined_group_right = self.combine_group(right_group_to_sort)

        # actual sorting of the groups
        sorted_left_group = self.sort_group(combined_group_left)
        sorted_right_group = self.sort_group(combined_group_right)
        result = self.sort_group([sorted_left_group, sorted_right_group])

        return result

    def sort_group(self, combined_group: list):
        sorted_group = []
        for i in range(1, len(combined_group)):
            j = i - 1
            if (j % 2 == 0) and not len(sorted_group):
                left_group = combined_group[j]
                right_group = combined_group[i]
                sorted_group = self.sort_with_merge(left_group, right_group)
            elif (j % 2) == 0 and len(sorted_group):
                new_left_group = combined_group[j]
                new_right_group = combined_group[i]
                sorted_group_new = self.sort_with_merge(new_left_group, new_right_group)
                sorted_group = self.sort_with_merge(sorted_group, sorted_group_new)
            elif len(combined_group) % 2 != 0 and i == len(combined_group) - 1:
                left_group = combined_group[i]
                right_group = sorted_group.copy()
                sorted_group = self.sort_with_merge(left_group, right_group)
        return sorted_group

    def sort_with_merge(self, left_group, right_group):
        sorted_group = []
        while len(left_group) or len(right_group):
            if len(left_group) and len(right_group):
                if left_group[0] > right_group[0]:
                    sorted_group.append(right_group[0])
                    right_group.pop(0)
                else:
                    sorted_group.append(left_group[0])
                    left_group.pop(0)
                    # the last element goes into the end of group
            elif len(left_group):
                sorted_group.append(left_group[0])
                left_group.pop(0)
            elif len(right_group):
                sorted_group.append(right_group[0])
                right_group.pop(0)
        return sorted_group

    def combine_group(self, group: list):
        combined_group = []
        extra_group_index = None
        if len(group) % 2 != 0:
            extra_group_index = len(group) - 1
        for i in range(1, len(group)):
            j = i - 1
            if j % 2 == 0:
                if group[j][0] > group[i][0]:
                    combined_group.append([group[i][0], group[j][0]])
                else:
                    combined_group.append([group[j][0], group[i][0]])
        if extra_group_index:
            combined_group.append(group[extra_group_index])
        return combined_group

    def split(self, group: list):
        left_group, right_group = self.split_the_group(group)
        if len(left_group) == 1:
            self.splited_groups.append(left_group)
        else:
            self.split(left_group)

        if len(right_group) == 1:
            self.splited_groups.append(right_group)
        else:
            self.split(right_group)

    def split_the_group(self, group):
        middle_index = round(len(group) / 2)
        left_group = group[:middle_index]
        right_group = group[middle_index:]
        return left_group, right_group
