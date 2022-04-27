from typing import List


def selection_sort(lst: List) -> List:
    """Compare adjacent elements of a list and swap them if the
    higher index value is smaller than the lower index value. O(n -1) since
    only n-1 elements need to be sorted as the nth element will be in order at
    the end of the last iteration.
    Parameters
    ----------
    lst : List
        List of items to be sorted
    """

    for i in range(len(lst) - 1):
        minIndex = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[minIndex]:
                minIndex = j

        if i != minIndex:
            lst[minIndex], lst[i] = lst[i], lst[minIndex]

    return lst
