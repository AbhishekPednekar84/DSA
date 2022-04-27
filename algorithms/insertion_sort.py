from typing import List


def insertion_sort(lst: List) -> List:
    """First iteration: Assign the element at index 1 to temp value. Compare it
       with the value at index 0 in a loop. If 0 > 1, make the values at 0 and 1 equal and at the end of the loop insert temp at position 0. Continue with the loop until the list is sorted.

    Parameters
    ----------
    lst : List
        Unsorted list

    Returns
    -------
    List
        Sorted list
    """
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1

        while j >= 0 and lst[j] > temp:
            lst[j + 1] = lst[j]
            j = j - 1

        lst[j + 1] = temp

    return lst
