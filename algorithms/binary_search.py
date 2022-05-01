from typing import List, Any


def binary_search(lst: List, search_value: Any) -> Any:
    """Given a sorted list, find the middle element and compare it with the
        search value. If it matches, return the index, or search to the left
        or right of the search value depending of whether the search value is lower
        or higher than mid

    Parameters
    ----------
    lst : List
        A sorted list
    search_value : Any
        Value to be searched

    Returns
    -------
    Any
        Index of the search value (if present)
    """

    low, high = 0, len(lst) - 1

    while low <= high:
        mid = int((low + high) / 2)

        if lst[mid] == search_value:
            return mid
        elif search_value < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1
