from algorithms.selection_sort import selection_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.linear_search import linear_search
from algorithms.binary_search import binary_search
from algorithms.merge_sort import merge_sort

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
    assert selection_sort(unsorted_list_numbers) == sorted_list_numbers
    assert selection_sort(unsorted_list_words) == sorted_list_words


def test_bubble_sort():
    assert bubble_sort(unsorted_list_numbers) == sorted_list_numbers
    assert bubble_sort(unsorted_list_words) == sorted_list_words


def test_insertion_sort():
    assert insertion_sort(unsorted_list_numbers) == sorted_list_numbers
    assert insertion_sort(unsorted_list_words) == sorted_list_words


def test_linear_search_positive():
    assert linear_search(sorted_list_words, "Suriname") == 4


def test_linear_search_negative():
    assert linear_search(sorted_list_numbers, 2) is None


def test_binary_search_positive():
    assert binary_search(sorted_list_words, "Suriname") == 4


def test_binary_search_negative():
    assert binary_search(sorted_list_numbers, 2) is None

def test_merge_sort():
    assert merge_sort(unsorted_list_numbers) == sorted_list_numbers