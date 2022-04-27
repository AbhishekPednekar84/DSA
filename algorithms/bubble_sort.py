from typing import List


def bubble_sort(lst: List) -> List:
    """Start with the last element of the list and bubble the value
       to the top of the list. O(n-1)

    Parameters
    ----------
    lst : List
        Unsorted list

    Returns
    -------
    List
        Sorted list
    """
    swap = False
    n = len(lst) - 1

    for i in range(n):
        for j in range(n, i, -1):
            if lst[j] < lst[j - 1]:
                swap = True
                lst[j - 1], lst[j] = lst[j], lst[j - 1]

        # Break if the list is sorted
        if swap == False:
            break

    return lst
