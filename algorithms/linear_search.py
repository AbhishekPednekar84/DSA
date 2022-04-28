from typing import List, Any

def linear_search(lst: List, search_value: Any) -> int:
    # sourcery skip: use-next
    """Iterate over the list sequentially and return the search value if found

    Parameters
    ----------
    lst : List
        A sorted or unsorted list
    search_value : Any
        A random search value

    Returns
    -------
    Any
        The index of the search value (if found)
    """

    for i in range(len(lst)):
        if lst[i] == search_value:
            return i
    return None