from algorithms.selection_sort import selection_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort

unsorted_list_numbers = [9, 3, 4, 1]
unsorted_list_words = [
    "Zimbabwe",
    "Mongolia",
    "Croatia",
    "New Zealand",
    "Suriname",
    "Canada",
]

sorted_list_numbers = [1, 3, 4, 9]
sorted_list_words = [
    "Canada",
    "Croatia",
    "Mongolia",
    "New Zealand",
    "Suriname",
    "Zimbabwe",
]


def test_selection_sort():
    assert selection_sort(sorted_list_numbers) == sorted_list_numbers
    assert selection_sort(sorted_list_words) == sorted_list_words


def test_bubble_sort():
    assert bubble_sort(sorted_list_numbers) == sorted_list_numbers
    assert bubble_sort(sorted_list_words) == sorted_list_words


def test_insertion_sort():
    assert insertion_sort(sorted_list_numbers) == sorted_list_numbers
    assert insertion_sort(sorted_list_words) == sorted_list_words
