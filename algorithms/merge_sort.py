from typing import List

def merge(lst1: List, lst2: List) -> List:
    sorted_list = []

    while len(lst1) != 0 and len(lst2) != 0:
        if lst1[0] < lst2[0]:
            sorted_list.append(lst1[0])
            lst1.remove(lst1[0])
        else:
            sorted_list.append(lst2[0])
            lst2.remove(lst2[0])
    
    if len(lst1) == 0:
        sorted_list += lst2
    else:
        sorted_list += lst1
    
    return sorted_list


def merge_sort(lst: List) -> List:
    """Merge sort uses divide and conquer to break down a list until a singleton
        list id obtained. Adjcent elements are then compared and the lists are merged.

    Parameters
    ----------
    lst : List
        Input unsorted list

    Returns
    -------
    List
        Output sorted list
    """

    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        mid = len(lst) // 2
        lst1 = merge_sort(lst[:mid])
        lst2 = merge_sort(lst[mid:])
        return merge(lst1, lst2)